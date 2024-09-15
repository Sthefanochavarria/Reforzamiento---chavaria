def ingresar_lista():
    tamano = int(input("Ingrese el tamaño de la lista: "))
    lista = []
    print("Ingrese los nombres de las compañías de TI:")
    for _ in range(tamano):
        compania = input("- ")
        lista.append(compania)
    return lista

def agregar_repetidos(lista):
    lista_copiada = lista.copy()
    cantidad_repetidos = int(input("¿Cuántos nombres adicionales desea agregar? "))
    print("Ingrese los nombres adicionales (pueden ser repetidos):")
    for _ in range(cantidad_repetidos):
        nombre_repetido = input("- ")
        lista_copiada.append(nombre_repetido)
    return lista_copiada

def obtener_no_repetidos(lista):
    from collections import Counter
    conteo = Counter(lista)
    no_repetidos = [nombre for nombre, count in conteo.items() if count == 1]
    return no_repetidos

def main():
    lista_inicial = ingresar_lista()
    lista_con_repetidos = agregar_repetidos(lista_inicial)
    lista_no_repetidos = obtener_no_repetidos(lista_con_repetidos)
    print("\nLista inicial:")
    print(lista_inicial)
    print("\nLista con nombres no repetidos:")
    print(lista_no_repetidos)
if __name__ == "__main__":
    main()