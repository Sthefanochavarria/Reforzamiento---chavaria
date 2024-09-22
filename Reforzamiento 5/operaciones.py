def cargar_numeros():
    numeros = []
    for X in range(3):
        while True:
            try:
                num = int(input("Ingrese el número entero {}: ".format(X+1)))
                numeros.append(num)
                break
            except ValueError:
                print("Error: Debe ingresar un valor numérico entero.")
    return numeros
def sumar(a, b):
    return a + b