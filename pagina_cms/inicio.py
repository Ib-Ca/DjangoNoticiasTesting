from django.shortcuts import render, redirect
from .models import usuarios, noticias

def inicio(request):
   # return render(request, 'inicio.html')
    vernoticias = noticias.objects.all().order_by('-fecha')
    return render(request, 'noticia_ver.html', {'noticias': vernoticias})

def acceder(request):
    if request.method=='GET':
        if 'codigo_usuario' in request.session:
        #if request.session['codigo_usuario']>0:
            variables = {
                'nombre_usuario': request.session['nombre_usuario'],
                'nivel_usuario': request.session['nivel_usuario']
            }
            return render(request,'panel.html', variables)
        else:
            return render(request,'acceder.html')
    
    if request.method=='POST':
        v_usuario=request.POST.get('usuario')
        v_clave=request.POST.get('clave')
        verificar_usuario=usuarios.objects.filter(usuario=v_usuario, estado='ACTIVO')
        print(verificar_usuario)
        variables={}
        if verificar_usuario.count()>0:
            if verificar_usuario[0].clave==v_clave:
                request.session['codigo_usuario']=verificar_usuario[0].id
                request.session['nombre_usuario']=verificar_usuario[0].nombre
                request.session['nivel_usuario']=verificar_usuario[0].nivel
                variables['nombre_usuario']= request.session['nombre_usuario']
                return render(request,'panel.html', variables)
            else:
                variables['m_error']='La contraseña es incorrecta'
                return render (request, 'acceder.html', variables)
        else:
            variables['m_error']='El usuario no esta registrado'
            return render (request, 'acceder.html', variables)

def salir(request):
    #request.session['codigo_usuario']=0
    #request.session['nombre_usuario']=''
    #request.session['nivel_usuario']=''
    del request.session['codigo_usuario']
    del request.session['nombre_usuario']
    del request.session['nivel_usuario'] 
    return redirect('inicio')