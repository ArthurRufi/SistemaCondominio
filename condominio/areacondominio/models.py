from django.db import models

# Create your models here.

class modelsAreas(models.Model):
    nome = models.CharField(max_length=255)
    status = models.BooleanField (default=False)


class modelsReservasAreas(models.Model):
    nome = models.CharField()
    moradorId = models.IntegerField(default=0)
    areaNome = models.CharField()
    dataReserva = models.DateField()
    horarioReserva = models.TimeField()

