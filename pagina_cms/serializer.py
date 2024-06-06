from rest_framework import serializers
from .models import noticias, grupos

class SerialNoticias(serializers.ModelSerializer):
    class Meta:
        model=noticias
        fields = [
            'id',
            'titulo',
            'fecha',
            'imagen',
        ]

class SerialDetalleNoticias(serializers.ModelSerializer):
    class Meta:
        model=noticias
        fields=[
            'id',
            'titulo',
            'fecha',
            'imagen',
            'cuerpo',
            'autor',
        ]

class SerialGrupos(serializers.ModelSerializer):
    class Meta:
        model=grupos
        fields=[
            'id',
            'grupo',
        ]