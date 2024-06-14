from .models import modelsArea, modelsReservasArea, modelsAreaManuntencao
from rest_framework import serializers

class SerializersArea(serializers.Serializer):
    nome = serializers.CharField()
    status = serializers.BooleanField()
    tipo = serializers.CharField()

    def create(self, validated_data):
        return modelsArea.objects.create(**validated_data)


class SerializersReservasArea(serializers.Serializer):
    nome = serializers.CharField()
    moradorId = serializers.IntegerField()
    areaNome = serializers.CharField()
    dataReserva = serializers.DateField()
    horarioReserva = serializers.TimeField()
    tempoTotal = serializers.IntegerField()

    def create(self, validated_data):
        return modelsReservasArea.objects.create(**validated_data)

class SerializersManutencao(serializers.ModelSerializer):
    class Meta:
        model = modelsAreaManuntencao
        fields = ['nome', 'status', 'ultimamanutencao', 'proximamanutencao', 'statusServico']