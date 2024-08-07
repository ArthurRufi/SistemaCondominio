from django.shortcuts import render
from .models import modelsArea, modelsAreaManuntencao, modelsReservasArea
from .serializers import SerializersArea, SerializersManutencao, SerializersReservasArea, SerializersAreaStatus
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from datetime import date


#api que consulta o status de todas as areas
class APIArea(APIView):
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
    
    def delete():
        pass


#api que consulta o status de uma area especifica deve ser usada junto a api de reser a de area
class APISearchArea(APIView):
    def get(self, request, nome):
        convert =  list(nome)
        for i in range(len(convert)):
            if convert[i] == '-':
                convert[i] = ' '
                
        convertname = ''.join(convert)

        if not convertname:
            return Response({'error': 'Nome não fornecido.'}, status=status.HTTP_400_BAD_REQUEST)

        areas = modelsArea.objects.filter(nome=convertname)
        if areas.exists():
            serializer = SerializersAreaStatus(areas, many=True)  # Usar many=True para lidar com múltiplos objetos
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': f'Nenhuma área encontrada com o nome fornecido. {convertname}'}, status=status.HTTP_404_NOT_FOUND)
        

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!arrumar repeticao de codigo        
#api que consulta status da area naquela data
class APISearchReservaDate(APIView):
    def get(self, resquest, dia, mes, ano):
        try:
            date_convert = date(int(ano), int(mes), int(dia))
            reserva = modelsReservasArea.objects.filter(dataReserva=date_convert, data = resquest.data)
            if reserva.exists():
                # Serializa os resultados
                serializer = SerializersReservasArea(reserva, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Não há reserva para a data especificada.'}, status=status.HTTP_404_NOT_FOUND)
        except modelsReservasArea.DoesNotExist:
            return Response({'message': 'Reserva nao encontrada'}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({'message': 'Data inválida.'}, status=status.HTTP_400_BAD_REQUEST)


#api que reserva aquela area para aquele dia x
class APIAddReserva(APIView):
    def post(self, request):
        serializer = SerializersReservasArea(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Salva o novo objeto no banco de dados
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class APIDeleteReserva():
    pass


class ModificarAreas(APIView):
    def post (self, request):
        serializer =  SerializersArea(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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