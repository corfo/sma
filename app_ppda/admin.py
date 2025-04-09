from django.contrib import admin
from .models import Comuna, Organismo, PpdaOrganismos, Ppda, Indicador, Medida, PpdaMedida, Registro
from .forms import RegistroForm

# Register your models here.
admin.site.register(Comuna)
admin.site.register(Organismo)
admin.site.register(PpdaOrganismos)
admin.site.register(Ppda)
admin.site.register(Indicador)
admin.site.register(Medida)
admin.site.register(PpdaMedida)
#admin.site.register(Registro)

class RegistroAdmin(admin.ModelAdmin):
    form = RegistroForm

admin.site.register(Registro, RegistroAdmin)

