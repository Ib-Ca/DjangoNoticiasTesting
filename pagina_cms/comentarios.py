from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from .models import noticias, comentarios, usuarios

def enviar_comentario(request, noticia_id):
    noticia = get_object_or_404(noticias, pk=noticia_id) 
    if request.method == 'POST': 
        if 'nivel_usuario' in request.session:
            nombre_usuario= request.session['nombre_usuario']
            autor = usuarios.objects.get(nombre=nombre_usuario)
            comentario_cuerpo = request.POST.get('cuerpo')
            comentario = comentarios(cuerpo=comentario_cuerpo, autor=autor, noticia=noticia)
            comentario.save()
        else:
            variables={}
            variables['m_error']='Tiene que estar logueado para poder comentar'
            return render(request,'fullnoti',  variables,noticia_id=noticia_id)
        return redirect('fullnoti', noticia_id=noticia_id)
    else:
        return redirect('fullnoti', noticia_id=noticia_id)
    
    
from django.shortcuts import redirect

def elim_comentario(request, comentario_id):
    #print(comentario_id)
    comentario = comentarios.objects.get(pk=comentario_id)
    comentario.delete()
    return redirect('fullnoti', noticia_id=comentario.noticia.id)

def pass_comentario(request, comentario_id):
    #print(comentario_id)
    comentario = comentarios.objects.get(pk=comentario_id)
    comentario.visible = 'SI'
    comentario.save()
    return redirect('fullnoti', noticia_id=comentario.noticia.id)

