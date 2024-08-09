from django.urls import path
from .views import ConsultarListaCompletaMorador, ConsultarVisitante


urlpatterns = [
    path('', ConsultarListaCompletaMorador.as_view(), name='asdka'),
    path('visitantes/', ConsultarVisitante.as_view(), name='akkak'),
]
