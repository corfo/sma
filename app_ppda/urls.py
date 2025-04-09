from django.urls import path
from .views import Healthy, Add, IndicadorAutocomplete, auth_test, PpdaListAPIView

urlpatterns = [
    path('healthy/', Healthy.as_view(), name='healthy'),
    path('add/', Add.as_view(), name='add'),
    path('auth_test/', auth_test.as_view(), name='auth_test'),
    path('all/', PpdaListAPIView.as_view(), name='all'),
    path('indicador-autocomplete/', IndicadorAutocomplete.as_view(), name='indicador-autocomplete'),
]

