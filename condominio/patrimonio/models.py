from django.db import models
#----------------------------------------------------REALIZAR CONFIG DO BANCO DE DADOS-------------------------------------------
#se refere aos patrimonios compartilhaveis
class PatrimonioPrivadoCompartilhaveis(models.Model):
    nome = models.CharField(max_length=50)
    proprietario = models.IntegerField(default= 0)
    tipo_objeto = models.CharField(max_length=255)
    emprestado = models.BooleanField(default=False)
    emprestadoaquem = models.IntegerField(default=0)


class ObjetoEmprestado(models.Model):
    codigoObjeto = models.IntegerField()
    codigoProprietario = models.IntegerField()
    codigoPrestamista = models.IntegerField()
    dataehora = models.DateTimeField()


class PatrimonioPublico(models.Model):
    nome = models.CharField(max_length=255)
    

class Veiculo(models.Model):
    modelo = models.CharField(max_length=255)
    placa = models.IntegerField()
    cor = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    codigoMorador = models.IntegerField()
    