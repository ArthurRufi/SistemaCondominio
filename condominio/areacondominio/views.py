from django.shortcuts import render
from .models import modelsArea, modelsAreaManuntencao, modelsReservasArea
from .serializers import SerializersArea, SerializersManutencao, SerializersReservasArea
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class APIStatusArea(APIView):
    def get(self, request):
        area = modelsArea .objects.all()
        serializers = SerializersArea(area, many=True)
        return Response(serializers.data, content_type='application/json')
    
    def post(self, request):
        serializer = SerializersArea(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Salva o novo objeto no banco de dados
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class APISearchArea(APIView):
    def get(self, request):
        # Extrair o parâmetro 'nome' da URL
        nome = request.query_params.get('nome')

        if not nome:
            return Response({'error': 'Nome não fornecido.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Tentar encontrar um registro que corresponda ao nome fornecido
            area = modelsArea.objects.get(nome=nome)
            serializer = SerializersArea(area)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except modelsArea.DoesNotExist:
            return Response({'message': 'Registro não encontrado.'}, status=status.HTTP_404_NOT_FOUND) 