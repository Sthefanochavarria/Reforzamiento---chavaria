from usuario_validador import validar_nombre_usuario


def main():
    nombre_usuario = input("Introduce el nombre de usuario: ")
    resultado = validar_nombre_usuario(nombre_usuario)

    if resultado is True:
        print("El nombre de usuario es válido.")
    else:
        print(resultado)

main()