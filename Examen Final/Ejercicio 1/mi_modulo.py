import random

def generar_lista_aleatoria():
    lista = [random.randint(1, 100) for _ in range(10)]
    print("Lista aleatoria generada:", lista)
    return lista

def obtener_no_repetidos(lista):
    lista_no_repetidos = list(set(lista))
    print("Números no repetidos:", lista_no_repetidos)
    return lista_no_repetidos

def ordenar_lista(lista):
    lista_mayor_menor = sorted(lista, reverse=True)
    lista_menor_mayor = sorted(lista)
    print("Orden de mayor a menor:", lista_mayor_menor)
    print("Orden de menor a mayor:", lista_menor_mayor)
    return lista_mayor_menor, lista_menor_mayor

def mayor_par(lista):
    pares = [num for num in lista if num % 2 == 0]
    if pares:
        mayor_numero_par = max(pares)
        print("Mayor número par:", mayor_numero_par)
        return mayor_numero_par
    else:
        print("No hay números pares en la lista.")
        return None
