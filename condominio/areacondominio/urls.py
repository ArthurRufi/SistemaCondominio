from django.urls import path
from .views import APIStatusArea, APISearchArea, APISearchReservaDate, APIAddReserva


urlpatterns = [
    #confere todas as areas
    path('apistatusarea/', APIStatusArea.as_view(), name='undifield'),
    #consulta se a area está disponivel ou não, não em caso de reservas
    path('searcharea/<str:nome>', APISearchArea.as_view(), name='und'),
    #nessa proxima endpoint vai ser referir a areas que não estão com reservas para aquela data e filtrar pelo tipo.
    path('reservas/<str:dia>/<str:mes>/<str:ano>/', APISearchReservaDate.as_view(), name='undi'),
    path('reservar/', APIAddReserva.as_view(), name='no')
]
