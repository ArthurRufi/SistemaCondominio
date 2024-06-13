from .models import modelsAreas, modelsReservasAreas, modelsAreaManuntencao
from rest_framework import serializers

class SerializersArea(serializers.Serializer):
    nome = serializers.CharField()
    status = serializers.BooleanField()
    tipo = serializers.CharField()


class SerializersReservasArea(serializers.Serializer):
    nome = serializers.CharField()
    moradorId = serializers.IntegerField()
    areaNome = serializers.CharField()
    dataReserva = serializers.DateField()
    horarioReserva = serializers.TimeField()
    tempoTotal = serializers.IntegerField()


class SerializersManutencao(serializers.ModelSerializer):
    class Meta:
        model = modelsAreaManuntencao
        fields = ['nome','status', 'ultimamanutencao,' 'proximamanutencao', 'statusServico']