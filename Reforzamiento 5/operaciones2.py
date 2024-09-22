import random
def generar_numeros_aleatorios():
    numeros = [random.randint(0, 100) for _ in range(30)]
    print("Números aleatorios generados:")
    print(numeros)
    return numeros

def ordenar_numeros(numeros):
    numeros_ordenados = sorted(numeros)
    print("Números ordenados:")
    print(numeros_ordenados)
    return numeros_ordenados

def mayor_numeros(numeros):
    mayor = max(numeros)
    print("El mayor número es: {}".format(mayor))
    return mayor