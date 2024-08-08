from django.urls import path
from .views import ConsultarPatrimonio, ConsultarVeiculo, RegistrarVeiculo

urlpatterns = [
    #confere todas as areas
    path('consultarpatrimonio/', ConsultarPatrimonio.as_view(), name='undifield'),
    path('consultarveiculo/<str:placa>/', ConsultarVeiculo.as_view(), name='isso'),
    path('registrarveiculo/', RegistrarVeiculo.as_view(), name='pia')
    
]
