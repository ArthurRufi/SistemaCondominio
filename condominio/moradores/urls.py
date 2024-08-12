from django.urls import path
from .views import ConsultarListaCompletaMorador, ConsultarVisitante


urlpatterns = [
    path('', ConsultarListaCompletaMorador.as_view(), name='moradores'),
    path('visitantes/', ConsultarVisitante.as_view(), name='visitantes-consulta'),
]
