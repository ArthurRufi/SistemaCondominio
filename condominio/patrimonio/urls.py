from django.urls import path
from .views import ConsultarPatrimonio

urlpatterns = [
    #confere todas as areas
    path('consultarpatrimonio/', ConsultarPatrimonio.as_view(), name='undifield'),
]
