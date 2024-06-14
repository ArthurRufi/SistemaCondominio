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
    def get(self, request, nome):
        if not nome:
            return Response({'error': 'Nome não fornecido.'}, status=status.HTTP_400_BAD_REQUEST)

        areas = modelsArea.objects.filter(nome=nome)
        if areas.exists():
            serializer = SerializersArea(areas, many=True)  # Usar many=True para lidar com múltiplos objetos
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Nenhuma área encontrada com o nome fornecido.'}, status=status.HTTP_404_NOT_FOUND)
        
'''
ADICIONAR ISSO NO FUTURO PARA CONVERTER INFORMAÇÕES EM URL
from urllib.parse import quote

# Exemplo de nome de área
nome_area = "Salão de Festas"

# Codificar o nome para uso em URLs
url_nome = quote(nome_area)

# URL final com o nome codificado
url_final = f"http://localhost:8000/areas/searcharea/{url_nome}"
print(url_final)'''