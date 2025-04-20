from django.shortcuts import render, get_object_or_404
from django.db import transaction
from django.http import HttpResponseForbidden,Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from drf_spectacular.utils import extend_schema
from .serializers import IndicadorSerializer, RegistroDinamicoSerializer, PpdaSerializer
from .models import Indicador, PpdaMedida, Ppda, Registro
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from dal import autocomplete
from django.utils.html import escape
from django.http import HttpResponseForbidden
from rest_framework.generics import ListAPIView
from datetime import datetime
from django.core.exceptions import PermissionDenied
from datetime import datetime


# Create your views here.
class PpdaListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Ppda.objects.all()
    serializer_class = PpdaSerializer

    @extend_schema(
        summary="Sabana de Datos",
        description="Endpoint para ver Sabana completa de PPDA",
        request=None,  # No se espera un cuerpo de solicitud
        responses={
            200: OpenApiResponse(
                response=PpdaSerializer(many=True),
                description="Sabana desplegada"
            ),
            400: OpenApiResponse(
                response=None,  # Solo un mensaje de error, no se necesita un serializer
                description="Error en la solicitud"
            ),
        },
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
            
class Add(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        summary="Add indicadores",
        description='endpoint para cargar indicadores a un PPDA',
        request=RegistroDinamicoSerializer,
        responses={
            201: OpenApiResponse(
                response=serializers.Serializer(
                    {"message": serializers.CharField()}
                ),
                description="Indicadores agregados correctamente"
            ),
            400: OpenApiResponse(
                response=serializers.Serializer(
                    {"error": serializers.CharField()}
                ),
                description="Error en la solicitud"
            ),
        },

    )
    def post(self, request):
        usuario = request.user
        if not request.user.has_perm('app_ppda.add_registro'):
            return Response(
                {"error": "No tienes permiso para agregar registros."},
                status=status.HTTP_403_FORBIDDEN
                )
        serializer = RegistroDinamicoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data
        ppda = get_object_or_404(Ppda, nombre=data['ppda'])
        medida = get_object_or_404(ppda.medidas, nombre__iexact=data['medida'])
        permiso=usuario_tiene_acceso_a_medida(usuario, medida)
        if not permiso:
            raise Http404("Usuario Autenticado, pero aplicando a medias sin permiso")
        ppda_medida = get_object_or_404(PpdaMedida, ppda=ppda, medida=medida)
        #print(f"INDICADORES EN DB: {medida.indicadores.all()}")
        indicadores_esperados = list(medida.indicadores.values_list('nombre', flat=True))
        indicadores_recibidos = [item['nombre'] for item in data['indicadores']]
        print(f"Indicadores Esperado:{indicadores_esperados}")
        print(f"Indicadores Recibidos:{indicadores_recibidos}")
        if set(indicadores_esperados) != set(indicadores_recibidos):
            raise Http404("Inconsistencia en Indicadores")
        print(ppda_medida.id)

        try:
            with transaction.atomic():
                for ind_data in data['indicadores']:
                    print(f"FOR INDICADOR: {ind_data['nombre']}")
                    indicador = get_object_or_404(
                        Indicador,
                        nombre__iexact=ind_data['nombre'],
                        medida=medida
                    )

                    # Crear el registro
            
                    Registro.objects.create(
                        ppda_medida=ppda_medida,
                        indicador=indicador,
                        fecha=data['fecha'],
                        valor=ind_data['valor']
                    )
        except Exception as e:
            print(f"Error: {e}")
            raise Http404("Indicador ya ingresado")            
        return Response({"message": "Registros creados correctamente"}, status=status.HTTP_201_CREATED)

class DeleteRegistrosAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Eliminar registros de una medida en una fecha específica",
        description="Endpoint para eliminar todos los registros asociados a una medida de un PPDA en una fecha específica",
        request=serializers.Serializer(
            {
                "ppda": serializers.CharField(),
                "medida": serializers.CharField(),
                "fecha": serializers.DateField(format="%Y-%m-%d")
            }
        ),
        responses={
            200: OpenApiResponse(
                response=serializers.Serializer(
                    {"message": serializers.CharField()}
                ),
                description="Registros eliminados correctamente"
            ),
            400: OpenApiResponse(
                response=serializers.Serializer(
                    {"error": serializers.CharField()}
                ),
                description="Error en la solicitud"
            ),
            404: OpenApiResponse(
                response=serializers.Serializer(
                    {"error": serializers.CharField()}
                ),
                description="No se encontró la medida o el PPDA"
            ),
        },
    )
    def post(self, request):
        """
        Elimina todos los registros asociados a una medida dentro de un PPDA
        para una fecha específica, usando POST.
        """
        usuario = request.user
        if not request.user.has_perm('app_ppda.delete_registro'):
            return Response(
                {"error": "No tienes permiso para agregar registros."},
                status=status.HTTP_403_FORBIDDEN
                )
        ppda_nombre = request.data.get("ppda")
        medida_nombre = request.data.get("medida")
        fecha_str = request.data.get("fecha")

        if not ppda_nombre or not medida_nombre or not fecha_str:
            return Response({"error": "PPDA, Medida y Fecha son requeridos."}, status=status.HTTP_400_BAD_REQUEST)

        ppda = get_object_or_404(Ppda, nombre=ppda_nombre)
        medida = get_object_or_404(ppda.medidas, nombre__iexact=medida_nombre)

        permiso = usuario_tiene_acceso_a_medida(usuario, medida)
        if not permiso:
            raise Http404("Usuario no autorizado para eliminar registros de esta medida")

        ppda_medida = get_object_or_404(PpdaMedida, ppda=ppda, medida=medida)

        try:
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
        except ValueError:
            raise Http404("Fecha no válida. Debe seguir el formato YYYY-MM-DD.")

        try:
            # Iniciar la transacción
            with transaction.atomic():
                # Eliminar todos los registros relacionados con esta medida y la fecha específica
                registros = Registro.objects.filter(ppda_medida=ppda_medida, fecha=fecha)
                registros.delete()

        except Exception as e:
            # Manejo de errores
            print(f"Error: {e}")
            raise Http404("Error al intentar eliminar los registros")

        return Response({"message": "Registros eliminados correctamente"}, status=status.HTTP_200_OK)
    
class Healthy(APIView):
    permission_classes = [AllowAny]
    @extend_schema(
        summary="Healthy endpoint - GET",
        description="Este endpoint responde a una solicitud GET con un mensaje de exito 200 OK",
        responses={200: {"type": "string"}},
    )
    def get(self, request):
        return Response({"message": "Estoy aqui", "date": datetime.now().isoformat()})

    @extend_schema(
        summary="Healthy endpoint - POST",
        description="Este endpoint responde a una solicitud POST con un mensaje de exito 201 Created",
        request=None,
        responses={201: {"type": "string"}},
    )
    def post(self, request):
        return Response({"message": "Estoy aqui"}, status=201)
    
class IndicadorAutocomplete(autocomplete.Select2QuerySetView):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            return HttpResponseForbidden("No tienes permisos para usar esta vista.")
        return super().dispatch(request, *args, **kwargs)
        
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Indicador.objects.none()

        qs = Indicador.objects.all()

        ppda_medida_id = self.forwarded.get('ppda_medida', None)
        if ppda_medida_id:
            try:
                ppda_medida = PpdaMedida.objects.get(pk=ppda_medida_id)
                qs = qs.filter(medida=ppda_medida.medida)
            except PpdaMedida.DoesNotExist:
                qs = Indicador.objects.none()

        if self.q:
            qs = qs.filter(nombre__icontains=self.q)

        return qs
    
class auth_test(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        summary="endpoint - GET - PARA VALIDACION DE AUTH",
        description="Este endpoint responde a una solicitud GET con un mensaje de exito 200 OK",
        responses={200: {"type": "string"}},
    )
    def get(self, request):
        return Response({"message": "Authenticado!"}, status=200)

    @extend_schema(
        summary="endpoint - POST - PARA VALIDACION DE AUTH",
        description="Este endpoint responde a una solicitud POST con un mensaje de exito 201 Created",
        request=None,
        responses={201: {"type": "string"}},
    )
    def post(self, request):
        return Response({"message": "Authenticado!"}, status=200)

def usuario_tiene_acceso_a_medida(usuario, medida):
    grupos_usuario = usuario.groups.all()
    grupo_organismo = medida.organismo.grupo
    return grupo_organismo in grupos_usuario