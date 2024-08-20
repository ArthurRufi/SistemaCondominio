from django.db import models
#lembrar de criar o modelo escalavel para milhoes de dados

    
#essa classe se refere a todas as areas do condominio
class modelsArea(models.Model):
    nome = models.CharField(max_length=255)
    #se status for marcado false significa que nao disponivel (usar em casos de manutenção ou fechamento, nunca em caso de reserva)
    status = models.BooleanField (default=False)
    #se refere a tipo: quadras, churrasqueiras, piscinas, area de lazer ou area de eventos
    tipo = models.CharField(max_length=1000)
    #utiliza o codigo do condominio para filtrar na base de dados
    condominioCodigo = models.IntegerField(db_index=True, default=0)

#essa classe se refere as areas reservadas do condominio em um determinado periodo de tempo
class modelsReservasArea(models.Model):
    nome = models.CharField(max_length=255)
    moradorId = models.IntegerField(default=0)
    areaNome = models.CharField(max_length=255)
    dataReserva = models.DateField()
    horarioReserva = models.TimeField()
    tempoTotal = models.IntegerField(default=3)
    tiporeserva = models.CharField(max_length=255, default=' ')
    condominioCodigo = models.IntegerField(db_index=True, default=0)


#essa classe se refere a manutencao de areas
class modelsAreaManuntencao(models.Model):
    nome = models.CharField(max_length=1000)
    status = models.CharField (max_length=255)
    ultimamanutencao = models.DateField()
    proximamanutencao = models.DateField()
    statusServico = models.CharField(max_length=255)
    condominioCodigo = models.IntegerField(db_index=True, default=0)
