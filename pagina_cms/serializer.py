from rest_framework import serializers
from .models import noticias, grupos, comentarios, usuarios

class ComentarioSerializer(serializers.ModelSerializer):
    autor_nombre = serializers.SerializerMethodField()
    class Meta:
        model = comentarios
        fields = ['id', 'cuerpo', 'fecha', 'autor','autor_nombre', 'visible']
    def get_autor_nombre(self, obj):
        return obj.autor.nombre

class SerialGrupos(serializers.ModelSerializer):
    class Meta:
        model=grupos
        fields=[
            'id',
            'grupo',
        ]

class SerialNoticias(serializers.ModelSerializer):
    grupo = SerialGrupos()
    class Meta:
        model=noticias
        fields = [
            'id',
            'titulo',
            'fecha',
            'imagen',
            'grupo',
        ]

class SerialDetalleNoticias(serializers.ModelSerializer):
    comentarios = ComentarioSerializer(many=True, read_only=True)
    class Meta:
        model = noticias
        fields = ['id', 'titulo', 'fecha', 'imagen', 'cuerpo', 'autor', 'comentarios']


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuarios
        fields = ['id', 'nombre', 'usuario', 'clave']
        extra_kwargs = {'clave': {'write_only': True}}