from operaciones import cargar_numeros, sumar

def main2():
    numeros = cargar_numeros()
    resultado = sumar(numeros[0], numeros[1])
    print("La suma de {} y {} es: {}".format(numeros[0], numeros[1], resultado))
main2()