from rest_framework import serializers
from patrimonio.models import PatrimonioPrivadoCompartilhaveis, ObjetoEmprestado, PatrimonioPublico, Veiculo


class SerializersPatrimonioPrivado(serializers.ModelSerializer):    
    class Meta:
        model = PatrimonioPrivadoCompartilhaveis
        fields = ['nome', 'proprietario', 'tipo_objeto', 'emprestado', 'emprestadoaquem']


class SerializersObjetoEmprestado(serializers.ModelSerializer):
    class Meta: 
        model = ObjetoEmprestado
        fields = ['codigoObjeto', 'codigoProprietario', 'codigoPrestamista', 'dataehora']


class SerializersPatrimonioPublico(serializers.ModelSerializer):
    class Meta:
        model = PatrimonioPublico
        fields = ['nome']


class SerilalizersVeiculos(serializers.ModelSerializer):
    class Meta: 
        model = Veiculo
        fields = ['modelo','placa', 'cor', 'tipo', 'codigoMorador']