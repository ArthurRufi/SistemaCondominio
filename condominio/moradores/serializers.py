from rest_framework import serializers
from .models import Moradores, Visitantes


class SerializersMorador(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    nome = serializers.CharField()
    codigoResidencia = serializers.IntegerField()
    codigoMorador = serializers.IntegerField()


class SerializersVisitante():
    nome = serializers.CharField(max_length=1000)
    codigoMorador = serializers.IntegerField()
    ultimaentrada = serializers.DateTimeField()
    codigoIdentificador = serializers.IntegerField()