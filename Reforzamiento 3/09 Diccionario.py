def mostrar_menu():
    print("Menú de la Agenda")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Salir")

def agregar_contacto(agenda):
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono: ")
        agenda[nombre]= telefono
        print("Contacto {} añadido con éxito.".format(nombre))

def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    if nombre in agenda:
        print("El número de teléfono de {} es: {}".format(nombre, agenda[nombre]))
    else:
        print("No se encuentra registrado.")

def main():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1/2/3): ")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            buscar_contacto(agenda)
        elif opcion == "3":
            print("Saliendo de la agenda.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

if __name__ == "__main__":
    main()