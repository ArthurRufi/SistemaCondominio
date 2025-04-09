from django.shortcuts import render
from .models import Moradores, Visitantes
from .serializers import SerializersMorador, SerializersVisitante
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny




#classe responsavel por entragar todos os moradores (remover futuramente)
class ConsultarListaCompletaMorador(APIView):
    permission_classes= [AllowAny]
    def get(self, request):
        moradores = Moradores.objects.all()
        serializers = SerializersMorador(moradores, many = True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
#aqui consulta visitantes 
class ConsultarVisitantes(APIView):
    def get(self, request):
        visitantes = Visitantes.objects.all()
        serializers = SerializersVisitante(visitantes, many= True)
        return Response(serializers.data, status=status.HTTP_200_OK)

#aqui consulta um visitante em especifico
class ConsultarVisitante(APIView):
    def get(self, request, user_id):
        try:
            user = Visitantes.objects.get(codigoIdentificador=user_id)
            serializers = SerializersVisitante(user) 
            return Response(serializers.data, status=status.HTTP_200_OK)
        except Visitantes.DoesNotExist:
            return Response ({"error": "Usuario nao encontrado"}, status=status.HTTP_406_NOT_ACCEPTABLE)
#aqui consulta morador por residencia
class ConsultarMoradorPorResidencia(APIView):
    def get(self, request):
        pass