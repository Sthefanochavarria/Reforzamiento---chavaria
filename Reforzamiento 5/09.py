def saludo_decorator(func):
    def wrapper():
        nombre = input("¿Cuál es tu nombre? ")
        hora = int(input("¿Qué hora es? (0-23) "))
        minutos = int(input("¿Qué minutos son? (0-59) "))
        print("Buenos días {}, son las {} horas con {} minutos.".format(nombre,hora,minutos))
        mensaje = func(nombre)
        print("Hasta luego, que tenga buen día.")
        return mensaje
    return wrapper
@saludo_decorator
def solicitar_mensaje(nombre):
    return "¡Hola, {}! Espero que tengas un excelente día.".format(nombre)
solicitar_mensaje()
