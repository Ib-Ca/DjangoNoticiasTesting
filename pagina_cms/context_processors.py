def nivel_usuario(request):
    return {'nivel_usuario': request.session.get('nivel_usuario', None)}
