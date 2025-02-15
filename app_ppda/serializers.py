from rest_framework import serializers

class IndicadorSerializer(serializers.Serializer):
    medida = serializers.CharField(max_length=100, required=True)
    ppda = serializers.CharField(max_length=100, required=True)
    periodo = serializers.CharField(max_length=100, required=True)
    charlas_realizadas = serializers.CharField(max_length=100, required=True)
    charlas_programadas = serializers.CharField(max_length=100, required=True)