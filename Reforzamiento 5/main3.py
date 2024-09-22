from operaciones2 import generar_numeros_aleatorios, ordenar_numeros, mayor_numeros


def main():
    numeros = generar_numeros_aleatorios()
    numeros_ordenados = ordenar_numeros(numeros)
    mayor = mayor_numeros(numeros_ordenados)
main()