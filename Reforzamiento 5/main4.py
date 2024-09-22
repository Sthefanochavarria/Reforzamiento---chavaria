from operaciones3 import cargar_valor, mostrar_raiz_cuadrada, calcular_potencias
def main():
    valor = cargar_valor()
    mostrar_raiz_cuadrada(valor)
    potencias = calcular_potencias(valor)
    print("El cuadrado de {} es: {}".format(valor, potencias['cuadrado']))
    print("El cubo de {} es: {}".format(valor, potencias['cubo']))
main()