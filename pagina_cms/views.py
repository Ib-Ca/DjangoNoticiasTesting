from django.shortcuts import render
from rest_framework import generics
from .serializer import SerialNoticias, SerialDetalleNoticias, SerialGrupos
from .models import noticias, grupos

# Create your views here.
class NoticiasAPILista(generics.ListAPIView):
    queryset=noticias.objects.all()
    serializer_class=SerialNoticias

class NoticiasAPIDetalle(generics.RetrieveAPIView):
    lookup_field='id'
    queryset=noticias.objects.all()
    serializer_class=SerialDetalleNoticias

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