from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import SerilalizersVeiculos
from .models import Veiculo

class ConsultarPatrimonio(APIView):
    def asda(request):
        return Response(status=status.HTTP_404_NOT_FOUND)
    

class ConsultarVeiculo(APIView):
    def get(self, request, placa):
        placaveiculo=placa.upper()
        veiculo = Veiculo.objects.filter(placa=placaveiculo)
        if veiculo.exists():
            serializer = SerilalizersVeiculos(veiculo, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif not veiculo.exists():
            return Response({'message': f'Veiculo de Placa {placaveiculo} não encontrado'}, status=status.HTTP_400_BAD_REQUEST)


class RegistrarVeiculo(APIView):
    def post(self, request):
        serializer = SerilalizersVeiculos(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        


''' OLHAR NOS MODELS O QUE RESTA PARA INSERIR'''