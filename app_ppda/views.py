from django.shortcuts import render, get_object_or_404
from django.db import transaction
from django.http import HttpResponseForbidden
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from drf_spectacular.utils import extend_schema
from .serializers import IndicadorSerializer
from .models import Indicador, PpdaMedida
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from dal import autocomplete
from django.utils.html import escape
from django.http import HttpResponseForbidden



# Create your views here.
'''
class Add(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        summary="Add indicadores",
        description='endpoint para cargar indicadores a un PPDA',
        request=IndicadorSerializer,
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
        serializer = IndicadorSerializer(data=request.data)
        if serializer.is_valid():
            ppda = get_object_or_404(Ppda, nombre=serializer.validated_data["ppda"])
            print("=========")
            print(f"ppda => {ppda}")
            # Organismo debe ser leido desde el usuario
            ppda_organismo = PpdaOrganismo.objects.filter(ppda=ppda, organismo__nombre="seremi_1").first()
            if ppda_organismo is not None:
                print(f"ppda_organismo => {ppda_organismo}")
                medida = get_object_or_404(Medida, nombre=serializer.validated_data["medida"])
                print(f"medida => pk:{medida.pk} {medida}")
                try:
                    with transaction.atomic():
                        for indicador_nombre in ["charlas_realizadas","charlas_programadas"]:
                            indicador = get_object_or_404(Indicador, nombre=indicador_nombre)
                            print(f"indicador {indicador.pk} {indicador.nombre}")
                            medida_indicador = MedidaIndicador.objects.create(
                                medida=medida,
                                indicador=indicador,
                                valor=serializer.validated_data[indicador.nombre],
                                periodo=serializer.validated_data["periodo"],
                                )
                            print(f"-> {medida_indicador}")
                except Exception as e:
                    print(f"Error: {e}")
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                return Response({"message": f"ok"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

class Healthy(APIView):
    permission_classes = [AllowAny]
    @extend_schema(
        summary="Healthy endpoint - GET",
        description="Este endpoint responde a una solicitud GET con un mensaje de exito 200 OK",
        responses={200: {"type": "string"}},
    )
    def get(self, request):
        return Response({"message": "Estoy aqui"})

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