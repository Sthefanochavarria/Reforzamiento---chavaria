def acceder_a_persona(clave):
    persona = {'nombre': 'Xavier', 'apellido': 'Rodriguez', 'dni': '63325345'}
    try:
        valor = persona[clave]
        print("El valor de '{}' es: {}".format(clave,valor))
    except KeyError as X:
        print("Error: {}".format(X))
        print("Causa: Intentaste acceder a una clave que no existe en el diccionario.")
        print("Solución: Verifica que la clave que intentas acceder esté en el diccionario.")
    except TypeError as X:
        print("Error: {}".format(X))
        print("Causa: El tipo de dato proporcionado no es válido.")
        print("Solución: Asegúrate de ingresar una cadena como clave.")
clave_usuario = input("Introduce la clave que deseas buscar (nombre, apellido, dni): ")
acceder_a_persona(clave_usuario)