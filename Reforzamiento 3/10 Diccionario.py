def mostrar_facturas(facturas):
    if not facturas:
        print("No hay facturas pendientes.")
    else:
        print("Lista de facturas pendientes:")
        for numero, coste in facturas.items():
            print(f"Número de factura: {numero}, Coste: {coste:.2f}")

def agregar_factura(facturas):
    while True:
        numero_factura = input("Ingrese el número de la nueva factura: ")
        if numero_factura in facturas:
            print("La factura ya existe. Use una factura diferente o pague esta factura antes de agregar una nueva.")
        else:
            break

    while True:
        try:
            coste = float(input("Ingrese el coste de la factura: "))
            if coste < 0:
                print("El coste no puede ser negativo. Inténtalo de nuevo.")
            else:
                break
        except ValueError:
            print("Eso no es un número válido. Inténtalo de nuevo.")

    facturas[numero_factura] = coste
    print(f"Factura {numero_factura} añadida con éxito.")
    mostrar_facturas(facturas)


def pagar_factura(facturas):
    numero_factura = input("Ingrese el número de la factura que fue pagada: ")
    if numero_factura in facturas:
        del facturas[numero_factura]
        print("Factura {} ha sido pagada y eliminada.".format(numero_factura))
    else:
        print("La factura no se encuentra en la lista de pendientes.")
    mostrar_facturas(facturas)


def main():

    facturas = {}

    while True:
        print("Menú de Gestión de Facturas")
        print("1. Añadir nueva factura")
        print("2. Marcar factura como pagada")
        print("3. Salir")

        opcion = input("Seleccione una opción (1/2/3): ")

        if opcion == "1":
            agregar_factura(facturas)
        elif opcion == "2":
            pagar_factura(facturas)
        elif opcion == "3":
            print("Saliendo del sistema de gestión de facturas.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")


if __name__ == "__main__":
    main()