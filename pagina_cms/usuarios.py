from django.shortcuts import render, redirect, get_object_or_404
from .models import usuarios

def ver(request):
    if request.method=='GET':
        if 'nivel_usuario' in request.session:
            if request.session['nivel_usuario']=='ADMINISTRADOR':
                lista=usuarios.objects.all()
                variables={}
                variables['request']=request
                variables['lista']=lista
                return render(request, 'usuario_ver.html', variables)
            else:
                variables={}
                variabes={}
                variables['nombre_usuario']= request.session['nombre_usuario']
                return render(request,'panel.html', variables)
        else:
            return redirect('acceder')
    
def nuevo(request):
    if request.method=='GET':
        return render(request, 'usuario_nuevo.html')
    
    if request.method=='POST':
        f_nombre=request.POST.get('nombre')
        f_usuario=request.POST.get('usuario')
        f_clave=request.POST.get('clave')
        f_estado=request.POST.get('estado')
        f_nivel=request.POST.get('nivel')
        nuevousuario=usuarios(
            nombre=f_nombre,
            usuario=f_usuario,
            clave=f_clave,
            estado=f_estado,
            nivel=f_nivel
        )        
        nuevousuario.save()
        return redirect ('verusuario')
    
def modificar(request, id):
    usuario = get_object_or_404(usuarios, pk=id)
    if request.method == 'POST':
        f_estado=request.POST.get('estado')
        f_nivel=request.POST.get('nivel')
        usuario.estado=f_estado
        usuario.nivel=f_nivel
        usuario.save()
        return redirect ('verusuario')
    else:
         return render(request, 'usuario_modify.html', {'usuario': usuario})
    
def borrar(request, id):
    para_borrar=usuarios.objects.get(pk=id)
    para_borrar.delete()
    return redirect ('verusuario')
