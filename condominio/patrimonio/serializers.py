from rest_framework import serializers
from patrimonio.models import PatrimonioPrivadoUtensilio


class SerializersPatrimonioPrivado(serializers.Serializer):
    
    nome = serializers.CharField()
    proprietario = serializers.IntegerField()
    tipo_objeto = serializers.CharField()
    emprestado = serializers.BooleanField()
    emprestadoaquem = serializers.IntegerField()


class ObjetoEmprestado(serializers.Serializer):
    codigoObjeto = serializers.IntegerField()
    codigoProprietario = serializers.IntegerField()
    codigoPrestamista = serializers.IntegerField()
    dataehora = serializers.DateTimeField()


class PatrimonioPublico(serializers.Serializer):
    nome = serializers.CharField()