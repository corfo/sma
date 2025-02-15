from django.contrib import admin
from .models import Ppda, Comuna, Medida, Indicador, Organismo, PpdaOrganismo,MedidaIndicador

# Register your models here.

class PpdaOrganismoInline(admin.TabularInline):  # También puedes usar StackedInline
    model = PpdaOrganismo
    extra = 1  # Número de filas vacías para agregar nuevas relaciones

@admin.register(Ppda)
class PpdaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "fecha_creacion")
    filter_horizontal = ("comunas",)  # Esto sí funciona porque no tiene 'through'
    inlines = [PpdaOrganismoInline]  # Agregamos el inline para organismos
#
class MedidaIndicadorInline(admin.TabularInline):
    model = MedidaIndicador
    extra = 1

@admin.register(Medida)
class MedidaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "indicador", "formula_calculo", "medio_verificador", "tipo_medida", "frecuencia")
    inlines = [MedidaIndicadorInline]

#admin.site.register(Ppda)
admin.site.register(Comuna)
#admin.site.register(Medida)
admin.site.register(Indicador)
admin.site.register(Organismo)
#admin.site.register(PpdaOrganismo)
admin.site.register(MedidaIndicador)

