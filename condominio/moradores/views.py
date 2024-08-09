from django.shortcuts import render
from .models import Moradores, Visitantes
from .serializers import SerializersMorador, SerializersVisitante
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

#classe responsavel por entragar todos os moradores (remover futuramente)
class ConsultarListaCompletaMorador(APIView):
    def get(self, request):
        moradores = Moradores.objects.all()
        serializers = SerializersMorador(moradores, many = True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
#aqui consulta visitantes 
class ConsultarVisitante(APIView):
    def get(self, request):
        visitantes = Visitantes.objects.all()
        serializers = SerializersVisitante(visitantes, many= True)
        return Response(serializers.data, status=status.HTTP_200_OK)

#aqui consulta um visitante em especifico
class ConsultarVisitante(APIView):
    def get(self, request):
        pass

#aqui consulta morador por residencia
class ConsultarMoradorPorResidencia(APIView):
    def get(self, request):
        pass