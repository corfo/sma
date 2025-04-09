from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group

class Comuna(models.Model):
    nombre = models.CharField(max_length=100, unique=True, null=False, blank=False)
    codigo = models.CharField(max_length=10,  unique=True, null=False, blank=False)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
    class Meta:
        db_table = 'comuna'

class Organismo(models.Model):
    nombre = models.CharField(max_length=100, unique=True, null=False, blank=False)
    grupo = models.OneToOneField(Group, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f"{self.nombre}"
    class Meta:
        db_table = 'organismo'

class PpdaOrganismos(models.Model):
    ppda = models.ForeignKey("Ppda", on_delete=models.CASCADE)
    organismo = models.ForeignKey("Organismo", on_delete=models.CASCADE)

    def __str__(self):
        return f"pk:{self.pk} {self.ppda.nombre} - {self.organismo.nombre}"
    class Meta:
        db_table = 'ppda_organismos'
        unique_together = ('ppda', 'organismo')


class Ppda(models.Model):
    nombre = models.CharField(max_length=100, unique=True, null=False, blank=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    comunas = models.ManyToManyField("Comuna", related_name="comunas", blank=True)
    organismos = models.ManyToManyField("Organismo", through="PpdaOrganismos", related_name="organismos", blank=True)
    medidas = models.ManyToManyField("Medida", through="PpdaMedida", related_name="medidas", blank=True)


    def __str__(self):
        return f"ppda_nombre:{self.nombre} ppda_fecha_creacion:{self.fecha_creacion}"
    class Meta:
        db_table = 'ppda'

class Indicador(models.Model):
    UNIDAD_CHOICES = [ ('cantidad', 'cantidad'), ('porcentaje', 'Porcentaje')]
    nombre = models.CharField(max_length=100, unique=True, null=False, blank=False)
    unidad = models.CharField(max_length=20, choices=UNIDAD_CHOICES, default='cantidad', null=False, blank=False)
    medida = models.ForeignKey('Medida', on_delete=models.CASCADE, related_name='indicadores')

    def __str__(self):
        return f"{self.nombre} - {self.get_unidad_display()}"
    class Meta:
        db_table = 'indicador'

class Medida(models.Model):
    FRECUENCIA_CHOICES = [('unica', 'Única'), ('anual', 'Anual'), ('cada_5_anios', 'Cada 5 años')]
    nombre = models.CharField(max_length=100, unique=True, null=False, blank=False)
    indicador = models.CharField(max_length=100, unique=True, null=False, blank=False)
    formula_calculo = models.CharField(max_length=100, unique=True, null=False, blank=False )
    medio_verificador = models.CharField( max_length=100, unique=True, null=False, blank=False)
    tipo_medida = models.CharField(max_length=100, unique=True, null=False, blank=False)
    frecuencia = models.CharField(max_length=20, choices=FRECUENCIA_CHOICES, default='unica', null=False, blank=False)
    organismo = models.ForeignKey('Organismo', on_delete=models.CASCADE, related_name='organismo', null=False, blank=False)

    def __str__(self):
        return f"{self.nombre} - {self.get_frecuencia_display()}"
    class Meta:
        db_table = 'medida'

class PpdaMedida(models.Model):
    ppda = models.ForeignKey("Ppda", on_delete=models.CASCADE)
    medida = models.ForeignKey("Medida", on_delete=models.CASCADE)
    fecha_asignacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.ppda.nombre} {self.medida.nombre}"
    class Meta:
        db_table = 'ppda_medidas'
        unique_together = ('ppda', 'medida')

class Registro(models.Model):
    ppda_medida = models.ForeignKey("PpdaMedida", on_delete=models.CASCADE, related_name="registros")
    indicador = models.ForeignKey("Indicador", on_delete=models.CASCADE, related_name="registros")

    fecha = models.DateField()
    valor = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = 'registro'
        unique_together = ('ppda_medida', 'indicador', 'fecha')

    def __str__(self):
        return f"{self.ppda_medida.ppda.nombre} - {self.indicador.nombre} @ {self.fecha}: {self.valor} {self.indicador.medida.nombre} {self.indicador.medida.indicador} {self.indicador.medida.organismo.nombre}"

    def clean(self):
        # Validación de integridad: el indicador debe pertenecer a la medida del ppda_medida
        if self.indicador.medida_id != self.ppda_medida.medida_id:
            raise ValidationError("El indicador no pertenece a la medida asignada al PPDA.")
