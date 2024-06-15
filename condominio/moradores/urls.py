from django.urls import path
from .views import ConsultarListaCompletaMoradores


urlpatterns = [
    path('', ConsultarListaCompletaMoradores.as_view(), name='asdka')
]
