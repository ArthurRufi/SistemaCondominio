from django.shortcuts import render
from .models import Moradores, Visitantes
from .serializers import SerializersMorador, SerializersVisitante
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny

#---------------------------------------------------------FALTA AUTENTICACAO CARALHOOOOOOOOOOOOOOOOOOO----------------------------------------------------------------
#classe responsavel por entragar todos os moradores (remover futuramente)
class ConsultarListaCompletaMorador(APIView):
    permission_classes= [AllowAny]
    def get(self, request, codigo):
        moradores = Moradores.objects.filter(codigoCondominio = codigo)
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
    def post(self, request):
        serializers = SerializersMorador(data = request.data)
        try:    
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                {f"ERROR INFO: Algo de errado ocorreu: confira o que é: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

 
class ExcluirMorador(APIView):
     def delete(self, request, id):
        try:
            sinal = Moradores.objects.get(codigoMorador=id)
            sinal.delete()
            return Response(
                {"mensagem": "Morador deletado com sucesso."},
                status=status.HTTP_204_NO_CONTENT
            )
        except Moradores.DoesNotExist:
            return Response(
                {"erro": "Morador não encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"erro": f"Ocorreu um erro ao deletar: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ExcluirVisitante(APIView):
     def delete(self, request, id):
        try:
            sinal = Visitantes.objects.get(codigoVisitante=id)
            sinal.delete()
            return Response(
                {"mensagem": "Visitante deletado com sucesso."},
                status=status.HTTP_204_NO_CONTENT
            )
        except Visitantes.DoesNotExist:
            return Response(
                {"erro": "Visitante não encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"erro": f"Ocorreu um erro ao deletar: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
