def nivel_usuario(request):
    nivel_usuario = request.session.get('nivel_usuario', None)
    usuario_autenticado = request.session.get('usuario_autenticado', False)
    #nombre_usuario= request.session['nombre_usuario', None]
    #print("Usuario: ", nombre_usuario)
    #print("Nivel de usuario:", nivel_usuario)
    #print("Usuario autenticado:", usuario_autenticado)
    return {
        'nivel_usuario': nivel_usuario,
        'usuario_autenticado': usuario_autenticado,
        #'nombre_usuario': nombre_usuario
    }