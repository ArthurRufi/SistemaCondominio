from django.db import models

# Create your models here.
class Moradores(models.Model):
    nome = models.CharField(max_length=1000)
    codigoResidencia = models.IntegerField(default= 0)
    codigoMorador = models.IntegerField(default=0)
    responsavel = models.BooleanField(default=False)

class Visitantes(models.Model):
    nome = models.CharField(max_length=1000)
    codigoMorador = models.IntegerField()
    ultimaentrada = models.DateTimeField()
    #informacoes no confindoc
    codigoIdentificador = models.IntegerField()

#LEMBRAR DE CRIAR TABELAS PARA HISTORICO DE VISITAS