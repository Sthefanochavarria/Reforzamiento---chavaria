from functools import wraps
from datetime import datetime

def conteo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        total_params = len(args) + len(kwargs)
        if total_params > 1:

            result = func(*args, **kwargs)
            print(f"La función '{func.__name__}' fue ejecutada.")
            return result
        else:
            print("La función requiere más de un parámetro para ejecutarse.")
            return None
    return wrapper


@conteo
def registrar_persona(edad, nombre):
    hora_actual = datetime.now().strftime('%H:%M')
    return f"Registro exitoso: {nombre}, {edad} años, registrado a las {hora_actual}."


@conteo
def calcular_media(nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4
    return f"La media de las notas es: {media}"


print(registrar_persona(25, "Rick"))
print(calcular_media(18, 20, 17, 19))
