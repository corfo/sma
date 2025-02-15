from django.urls import path
from .views import Healthy, Add

urlpatterns = [
    path('healthy/', Healthy.as_view(), name='healthy'),
    path('add/', Add.as_view(), name='add'),
]

