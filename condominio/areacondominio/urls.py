from django.urls import path
from .views import APIArea, APISearchArea, APISearchReservaDate, APIAddReserva, APIAdicionarArea


urlpatterns = [
    #confere todas as areas
    path('todas-as-areas/', APIArea.as_view(), name='Areas'),
    #consulta se a area está disponivel ou não, não em caso de reservas
    path('pesquisar-area/<str:nome>', APISearchArea.as_view(), name='pesquisar'),
    #nessa proxima endpoint vai ser referir a areas que não estão com reservas para aquela data e filtrar pelo tipo.
    path('consultar-reservas/<str:dia>/<str:mes>/<str:ano>/', APISearchReservaDate.as_view(), name='consultar'),
    #realiza a reserva da area e caso esteja reservada ela é retornada um badrequest
    path('reservar/', APIAddReserva.as_view(), name='reservar'),
    path('adicionar-area/', APIAdicionarArea.as_view(), name='adicionar')
]
