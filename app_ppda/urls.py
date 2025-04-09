from django.urls import path
from .views import Healthy, IndicadorAutocomplete

urlpatterns = [
    path('healthy/', Healthy.as_view(), name='healthy'),
    #path('add/', Add.as_view(), name='add'),
    path('indicador-autocomplete/', IndicadorAutocomplete.as_view(), name='indicador-autocomplete'),
]

