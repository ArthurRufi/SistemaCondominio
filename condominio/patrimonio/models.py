from django.db import models
#----------------------------------------------------REALIZAR CONFIG DO BANCO DE DADOS-------------------------------------------

class PatrimonioPrivadoUtensilio(models.Model):
    nome = models.CharField(max_length=50)
    proprietario = models.IntegerField(default= 0)
    tipo_objeto = models.CharField(max_length=255)
    emprestado = models.BooleanField(default=False)
    emprestadoaquem = models.IntegerField(default=0)
    '''
    ISSO AQUI DEVE SER IMPLEMENTADO
    def emprestar_objeto(request, objeto_id):
    objeto = get_object_or_404(Objeto, id=objeto_id)
    if request.method == 'POST':
        objeto.emprestar(request.user)
        return redirect('pagina_dos_objetos')  # Redireciona para a página que você deseja
    return render(request, 'emprestar_objeto.html', {'objeto': objeto})

@login_required
def devolver_objeto(request, objeto_id):
    objeto = get_object_or_404(Objeto, id=objeto_id)
    if request.method == 'POST':
        objeto.devolver()
        return redirect('pagina_dos_objetos')  # Redireciona para a página que você deseja
    return render(request, 'devolver_objeto.html', {'objeto': objeto})
'''

    def __str__(self) -> str:
        return super().__str__()