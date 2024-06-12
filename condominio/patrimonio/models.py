from django.db import models
#----------------------------------------------------REALIZAR CONFIG DO BANCO DE DADOS-------------------------------------------
#se refere aos patrimonios compartilhaveis
class PatrimonioPrivadoUtensilio(models.Model):
    nome = models.CharField(max_length=50)
    proprietario = models.IntegerField(default= 0)
    tipo_objeto = models.CharField(max_length=255)
    emprestado = models.BooleanField(default=False)
    emprestadoaquem = models.IntegerField(default=0)

    def emprestar(self, usuario):
        if not self.esta_emprestado:
            self.esta_emprestado = True
            self.emprestado_para = usuario
            self.save()


    def devolver(self):
        if self.esta_emprestado:
            self.esta_emprestado = False
            self.emprestado_para = None
            self.save()


    def __str__(self) -> str:
        return super().__str__()
    