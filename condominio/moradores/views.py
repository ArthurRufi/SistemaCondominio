from django.shortcuts import render
from .models import Moradores, Visitantes
from .serializers import SerializersMorador, SerializersVisitante
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class ConsultarListaCompletaMoradores(APIView):
    def get(self, request):
        moradores = Moradores.objects.all()
        serializers = SerializersMorador(moradores, many = True)
        return Response(serializers.data, status=status.HTTP_200_OK)