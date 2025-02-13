from django.db import models

class PpdaOrganismo(models.Model):
    ppda = models.ForeignKey("Ppda", on_delete=models.CASCADE)
    organismo = models.ForeignKey("Organismo", on_delete=models.CASCADE)
    medidas = models.ManyToManyField("Medida", related_name="medidas", blank=True)

    def __str__(self):
        return f"{self.ppda.nombre} - {self.organismo.nombre}"

class Ppda(models.Model):
    nombre = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    comunas = models.ManyToManyField("Comuna", related_name="comunas", blank=True)
    organismos = models.ManyToManyField("Organismo", through="PpdaOrganismo", related_name="organismos", blank=True)

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
    indicadores = models.ManyToManyField(
        Indicador,
        through="MedidaIndicador",
        related_name="medidas",
        blank=True
    )

    def __str__(self):
        return f"{self.nombre} - {self.get_frecuencia_display()}"

class MedidaIndicador(models.Model):
    medida = models.ForeignKey(Medida, on_delete=models.CASCADE)
    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    periodo = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return f"{self.medida.nombre} - {self.indicador.nombre} ({self.periodo})"

class Organismo(models.Model):
    nombre = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False
    )

    def __str__(self):
        return f"{self.nombre}"
