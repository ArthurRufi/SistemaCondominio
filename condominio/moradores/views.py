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
        

#Consulta de visitantes cadastrados por morador
class ConsultarVisitantesPorMorador(APIView):
    def get(self, request, id):
        try:
            morador = Visitantes.objects.filter(codigoMorador = id)
            serializers = SerializersVisitante(morador)
            return Response(serializers.data, many=True)
        except Visitantes.DoesNotExist:
            return Response({"ERROR": "Morador Não encontrado"}, status=status.HTTP_406_NOT_ACCEPTABLE)


#aqui consulta morador por residencia
class ConsultarMoradorPorResidencia(APIView):
    def post(self, request):
        pass

#------------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------ABAIXO TRATA-SE SOBRE REGISTRO E EXCLUSÃO DE MORADORES E VISITANTES-----------------#

class AdicionarMorador(APIView):
    def post(self, request):
        serializer = SerializersMorador(data= request.data)

        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"detail": "Ocorreu um erro inesperado ao tentar adicionar o morador."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class AdicionarVisitante(APIView):
    pass


class ExcluirMorador(APIView):
    pass


class ExcluirVisitante(APIView):
    pass