from django.urls import path
from .views import ConsultarListaCompletaMoradores, ConsultarVisitantes


urlpatterns = [
    path('', ConsultarListaCompletaMoradores.as_view(), name='asdka'),
    path('visitantes/', ConsultarVisitantes.as_view(), name='akkak'),
]
