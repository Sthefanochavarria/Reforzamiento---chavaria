def validar_nombre_usuario(nombre_usuario):
    if len(nombre_usuario) < 7:
        return "El nombre de usuario debe contener al menos 7 caracteres."
    elif len(nombre_usuario) > 12:
        return "El nombre de usuario no puede contener más de 12 caracteres."
    elif not nombre_usuario.isalnum():
        return "El nombre de usuario puede contener solo letras y números."
    else:
        return True