from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from .serializer import SerialNoticias, SerialDetalleNoticias, SerialGrupos, UsuarioSerializer, ComentarioSerializer
from .models import noticias, grupos, comentarios, usuarios
import logging
from rest_framework.exceptions import ValidationError
logger = logging.getLogger(__name__)
# Create your views here.
class NoticiasAPILista(generics.ListAPIView):
    queryset=noticias.objects.all()
    serializer_class=SerialNoticias

class NoticiasAPIDetalle(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = noticias.objects.all()
    serializer_class = SerialDetalleNoticias
    def get_object(self):
        noticia = get_object_or_404(noticias, id=self.kwargs['id'])
        comentarios_noticia = comentarios.objects.filter(noticia=noticia)
        noticia.comentarios = comentarios_noticia
        return noticia

class GruposAPILista(generics.ListAPIView):
    queryset=grupos.objects.all()
    serializer_class=SerialGrupos

class GruposAPINuevo(generics.CreateAPIView):
    queryset=grupos.objects.all()
    serializer_class=SerialGrupos

class GruposAPIModificar(generics.RetrieveUpdateAPIView):
    lookup_field='id'
    queryset=grupos.objects.all()
    serializer_class=SerialGrupos

class GruposAPIBorrar(generics.DestroyAPIView):
    lookup_field='id'
    queryset=grupos.objects.all()
    
class UsuarioRegistroAPI(generics.CreateAPIView):
    queryset = usuarios.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioLoginAPI(generics.GenericAPIView):
    serializer_class = UsuarioSerializer
    def post(self, request, *args, **kwargs):
        usuario = request.data.get('usuario')
        clave = request.data.get('clave')
        verificar_usuario = usuarios.objects.filter(usuario=usuario, clave=clave, estado='ACTIVO').first()
        if verificar_usuario:
            request.session['codigo_usuario'] = verificar_usuario.id
            request.session['nombre_usuario'] = verificar_usuario.nombre
            request.session['nivel_usuario'] = verificar_usuario.nivel
            request.session['usuario_autenticado'] = True
            return JsonResponse({
                'mensaje': 'Inicio de sesión exitoso',
                'id_usuario': verificar_usuario.id,
                'nombre_usuario': verificar_usuario.nombre,
                'nivel_usuario': verificar_usuario.nivel
            })
        else:
            return JsonResponse({'error': 'Credenciales inválidas'}, status=401)
        

class PublicarComentarioAPI(generics.CreateAPIView):
    serializer_class = ComentarioSerializer

    def post(self, request, *args, **kwargs):
        if 'cuerpo' not in request.data or 'autor' not in request.data or 'noticia' not in request.data or 'visible' not in request.data:
            return Response({'detail': 'Todos los campos son requeridos: cuerpo, autor, noticia, visible.'}, status=status.HTTP_400_BAD_REQUEST)
        
        cuerpo = request.data.get('cuerpo')
        autor_id = request.data.get('autor') 
        noticia_id = request.data.get('noticia')
        visible = request.data.get('visible')
     
        autor = get_object_or_404(usuarios, pk=autor_id)
        noticia = get_object_or_404(noticias, pk=noticia_id)
        comentario = comentarios.objects.create(cuerpo=cuerpo, autor=autor, noticia=noticia, visible=visible)

        return Response({'message': 'Comentario creado correctamente'}, status=status.HTTP_201_CREATED)

class RegistrarUsuarioAPI(generics.CreateAPIView):
    serializer_class = UsuarioSerializer
    def post(self, request, *args, **kwargs):
        if 'nombre' not in request.data or 'usuario' not in request.data or 'clave' not in request.data:
            return Response({'detail': 'Todos los campos son requeridos: nombre, usuario, clave.'}, status=status.HTTP_400_BAD_REQUEST)  
        nombre = request.data.get('nombre')
        usuario = request.data.get('usuario')
        clave = request.data.get('clave')
        estado = 'ACTIVO'
        nivel = 'LECTOR'

        usuario_nuevo = usuarios.objects.create(nombre=nombre, usuario=usuario, clave=clave, estado=estado, nivel=nivel)

        return Response({'message': 'Usuario creado correctamente'}, status=status.HTTP_201_CREATED)