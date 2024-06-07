from django.shortcuts import render, redirect, get_object_or_404
from .models import grupos
from django.contrib import messages

def ver_grupos(request):
    if request.method == 'GET':
        if 'nivel_usuario' in request.session:
            if request.session['nivel_usuario'] == 'ADMINISTRADOR':
                lista_grupos = grupos.objects.all()
                variables = {'request': request, 'grupos': lista_grupos}
                return render(request, 'ver_grupo.html', variables)
            else:
                variables = {'nombre_usuario': request.session.get('nombre_usuario', '')}
                return render(request, 'panel.html', variables)
        else:
            return redirect('acceder')


def nuevo_grupo(request):
    if request.method == 'GET':
        return render(request, 'grupo_nuevo.html')
    elif request.method == 'POST':
        nombre_grupo = request.POST.get('grupo')
        nuevo_grupo = grupos(grupo=nombre_grupo)
        nuevo_grupo.save()
        return redirect('ver_grupos')

def modificar_grupo(request, id):
    grupo = get_object_or_404(grupos, pk=id)
    if request.method == 'POST':
        nuevo_nombre_grupo = request.POST.get('grupo')
        grupo.grupo = nuevo_nombre_grupo
        grupo.save()
        return redirect('ver_grupos')
    else:
        return render(request, 'grupo_modify.html', {'grupo': grupo})


def borrar_grupo(request, id):
    try:
        grupo_para_borrar = get_object_or_404(grupos, pk=id)
        grupo_para_borrar.delete()
        messages.success(request, 'El grupo ha sido eliminado correctamente.')
    except Exception as e:
        messages.error(request, f'Error al eliminar el grupo')

    return redirect('ver_grupos')

