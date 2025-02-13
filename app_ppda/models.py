from django.db import models

class Ppda(models.Model):
    nombre = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    comunas = models.ManyToManyField("Comuna", related_name="comunas", blank=True)
    #medidas = models.ManyToManyField("Medida", related_name="medidas", blank=True)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False
    )
    codigo = models.CharField(
        max_length=10,
        unique=True,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.nombre

class Medida(models.Model):
    FRECUENCIA_CHOICES = [
        ('unica', 'Única'),
        ('anual', 'Anual'),
        ('cada_5_anios', 'Cada 5 años'),
    ]
    nombre = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False
    )
    indicador = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False
    )
    formula_calculo = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False
    )
    medio_verificador = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False
    )
    tipo_medida = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False
    )
    frecuencia = models.CharField(
        max_length=20,
        choices=FRECUENCIA_CHOICES,
        default='unica',
        null=False,
        blank=False
    )

    def __str__(self):
        return f"{self.nombre} - {self.get_frecuencia_display()}"

class Indicador(models.Model):
    UNIDAD_CHOICES = [
        ('cantidad', 'cantidad'),
        ('porcentaje', 'Porcentaje'),
    ]
    nombre = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False
    )

    unidad = models.CharField(
        max_length=20,
        choices=UNIDAD_CHOICES,
        default='cantidad',
        null=False,
        blank=False
    )

    def __str__(self):
        return f"{self.nombre} - {self.get_unidad_display()}"
