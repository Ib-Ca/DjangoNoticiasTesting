from django.urls import path
from . import inicio, usuarios, noticias

urlpatterns = [
    path('', inicio.inicio, name='inicio'),
    path('verusuario', usuarios.ver, name='verusuario'),
    path('nueusuario', usuarios.nuevo, name='nueusuario'),
    path('modusuario/<id>', usuarios.modificar, name='modusuario'),
    path('borusuario/<id>', usuarios.borrar, name='borusuario'),
    path('add_noti', noticias.agregar_noticia, name='addnoti'),
    path('ver_noti', noticias.ver_noticias, name='vernoti'),
    path('full_noti/<int:noticia_id>', noticias.ver_noticia_completa, name='fullnoti'),
    path('acceder', inicio.acceder, name='acceder'),
    path('salir', inicio.salir, name='salir'),
]