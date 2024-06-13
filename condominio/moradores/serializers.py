from rest_framework import serializers
from .models import Moradores, Visitantes


class SerializersMorador(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    nome = serializers.CharField()
    codigoResidencia = serializers.IntegerField()
    codigoMorador = serializers.IntegerField()