from django.urls import path
from .views import APIStatusArea, APISearchArea


urlpatterns = [
    path('apistatusarea/', APIStatusArea.as_view(), name='undifield'),
    path('searcharea/', APISearchArea.as_view(), name='und')
]
