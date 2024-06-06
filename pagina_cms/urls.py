from django.urls import path
from . import inicio, usuarios, noticias, comentarios, views

urlpatterns = [
    path('', inicio.inicio, name='inicio'),
    path('verusuario', usuarios.ver, name='verusuario'),
    path('nueusuario', usuarios.nuevo, name='nueusuario'),
    path('createuser', usuarios.nuevo, name='createuser'),
    path('modusuario/<id>', usuarios.modificar, name='modusuario'),
    path('borusuario/<id>', usuarios.borrar, name='borusuario'),
    path('add_noti', noticias.agregar_noticia, name='addnoti'),
    path('ver_noti', noticias.ver_noticias, name='vernoti'),
    path('full_noti/<int:noticia_id>', noticias.ver_noticia_completa, name='fullnoti'),
    path('acceder', inicio.acceder, name='acceder'),
    path('create', inicio.create, name='create'),
    path('salir', inicio.salir, name='salir'),
    path('enviar_comentario/<int:noticia_id>', comentarios.enviar_comentario, name='enviar_comentario'),
    path('elim_comentario/<int:comentario_id>', comentarios.elim_comentario, name='elim_comentario'),
    path('pass_comentario/<int:comentario_id>', comentarios.pass_comentario, name='pass_comentario'),
    path('listanoticias', views.NoticiasAPILista.as_view(), name='listanoticias'),
    path('listanoticias/<int:id>', views.NoticiasAPIDetalle.as_view(), name='detallenoticias'),
    path('listagrupos', views.GruposAPILista.as_view(), name='listagrupos'),
    path('nuevogrupo', views.GruposAPINuevo.as_view(), name='nuevogrupo'),
]