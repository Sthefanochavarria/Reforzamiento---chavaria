def decorador_multiplicacion(func):
    def wrapper(*args, **kwargs):
        print("Está por ejecutarse la función.")
        resultado = func(*args, **kwargs)
        print("La función ha sido ejecutada correctamente.")
        return resultado
    return wrapper

@decorador_multiplicacion
def multiplicar_numeros(a, b, c, **kwargs):
    d = kwargs.get('d', 1)
    e = kwargs.get('e', 1)
    f = kwargs.get('f', 1)
    resultado = a * b * c * d * e * f
    return resultado

if __name__ == "__main__":
    resultado = multiplicar_numeros(2, 3, 4, d=5, e=6, f=7)
    print("El resultado de la multiplicación es: {}".format(resultado))