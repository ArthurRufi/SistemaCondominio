from django.urls import path
from .views import APIstatusArea


urlpatterns = [
    path('apistatusarea/<int:id>/', APIstatusArea.as_view(), name='undifield')
]
