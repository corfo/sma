from dal import autocomplete
from django import forms
from .models import Registro

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = '__all__'
        widgets = {
            'indicador': autocomplete.ModelSelect2(
                url='indicador-autocomplete',
                forward=['ppda_medida'],  # se envía este campo como contexto al autocomplete
            )
        }
