from django.db import models

# Create your models here.

class modelsArea(models.Model):
    nome = models.CharField(max_length=255)
    status = models.BooleanField (default=False)
    tipo = models.CharField(max_length=1000)



class modelsReservasArea(models.Model):
    nome = models.CharField()
    moradorId = models.IntegerField(default=0)
    areaNome = models.CharField()
    dataReserva = models.DateField()
    horarioReserva = models.TimeField()
    tempoTotal = models.IntegerField(default=3)


class modelsAreaManuntencao(models.Model):
    nome = models.CharField(max_length=1000)
    status = models.CharField (max_length=255)
    ultimamanutencao = models.DateField()
    proximamanutencao = models.DateField()
    statusServico = models.CharField(max_length=255)

