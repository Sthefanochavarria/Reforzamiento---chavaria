def decorador_argumentos(func):
    def wrapper(*args, **kwargs):
        cantidad_args = len(args) + len(kwargs)
        print("La cantidad de argumentos que tiene la función es:")
        print(cantidad_args)
        resultado = func(*args, **kwargs)
        print("La función decoradora terminó de ejecutarse correctamente.")
        return resultado
    return wrapper

@decorador_argumentos
def suma(*args):
    return sum(args)

if __name__ == "__main__":
    resultado = suma(4, 1, 10, 2, 50, 64)
    print("El resultado de la suma es: {}".format(resultado))
