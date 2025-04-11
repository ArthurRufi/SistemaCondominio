from django.db import models

# Create your models here.
class Moradores(models.Model):
    nome = models.CharField(max_length=1000)
    codigoResidencia = models.IntegerField(default= 0)
    codigoMorador = models.IntegerField(default=0)
    responsavel = models.BooleanField(default=False)
    codigoCondominio = models.IntegerField(default=0)


class Visitantes(models.Model):
    nome = models.CharField(max_length=1000)
    codigoMorador = models.IntegerField()
    ultimaentrada = models.DateTimeField()
    #informacoes no confindoc
    codigoIdentificador = models.IntegerField()
    codigoCondominio = models.IntegerField(default=0)

#LEMBRAR DE CRIAR TABELAS PARA HISTORICO DE VISITAS