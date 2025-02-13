from django.contrib import admin
from .models import Ppda, Comuna, Medida, Indicador, Organismo, PpdaOrganismo,MedidaIndicador

# Register your models here.

admin.site.register(Ppda)
admin.site.register(Comuna)
admin.site.register(Medida)
admin.site.register(Indicador)
admin.site.register(Organismo)
admin.site.register(PpdaOrganismo)
admin.site.register(MedidaIndicador)

