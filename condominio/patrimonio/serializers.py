from rest_framework import serializers
from patrimonio.models import PatrimonioPrivadoUtensilio


class SerializersPatrimonioPrivado(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    