def cargar_valor():
    while True:
        try:
            valor = int(input("Ingrese un número entero: "))
            return valor
        except ValueError:
            print("Error: Debe ingresar un valor numérico entero.")

def mostrar_raiz_cuadrada(valor):
    raiz = valor ** 0.5
    print("La raíz cuadrada de {} es: {}".format(valor, raiz))

def calcular_potencias(valor):
    return {
        "cuadrado": valor ** 2,
        "cubo": valor ** 3
    }