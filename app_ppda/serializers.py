from rest_framework import serializers
from .models import Ppda, Medida, Registro, Indicador, Organismo, PpdaMedida

class IndicadorSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    valor = serializers.DecimalField(max_digits=12, decimal_places=2)

class RegistroDinamicoSerializer(serializers.Serializer):
    ppda = serializers.CharField()
    medida = serializers.CharField()
    fecha = serializers.DateField()
    indicadores = IndicadorSerializer(many=True)

###### Serializadores para view all ######

class RegistroSerializer(serializers.ModelSerializer):
    indicador = serializers.CharField(source='indicador.nombre')

    class Meta:
        model = Registro
        fields = ['fecha', 'valor', 'indicador']

class MedidaSerializer(serializers.ModelSerializer):
    organismo = serializers.CharField(source='organismo.nombre')
    registros = serializers.SerializerMethodField()

    class Meta:
        model = Medida
        fields = ['nombre', 'organismo', 'frecuencia', 'registros']

    def get_registros(self, medida):
        ppda = self.context.get('ppda')
        ppda_medida = medida.ppdamedida_set.filter(ppda=ppda).first()
        if ppda_medida:
            registros = ppda_medida.registros.all()
            return RegistroSerializer(registros, many=True).data
        return []

class PpdaSerializer(serializers.ModelSerializer):
    medidas = serializers.SerializerMethodField()

    class Meta:
        model = Ppda
        fields = ['nombre', 'fecha_creacion', 'medidas']

    def get_medidas(self, ppda):
        medidas = ppda.medidas.all()
        return MedidaSerializer(medidas, many=True, context={'ppda': ppda}).data