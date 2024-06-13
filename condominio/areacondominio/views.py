from django.shortcuts import render
from .models import modelsArea, modelsAreaManuntencao, modelsReservasArea
from .serializers import SerializersArea, SerializersManutencao, SerializersReservasArea
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView

class APIstatusArea(APIView):
    def get(self, request):
        area=modelsArea.objects.all()
        serializers = SerializersArea(area, many=True)