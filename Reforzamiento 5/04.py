def saludo_usuario():
    try:
        nombre = input("Por favor, ingrese su nombre: ")
        dia = input("Ingrese el día (en formato 2 dígitos, ej. 04): ")
        mes = input("Ingrese el mes (por ejemplo, Mayo): ")
        año = input("Ingrese el año (ej. 2024): ")

        string = "Hello {}, hoy estamos {} de {} del {}".format(nombre, dia, mes, año)

        print(string/ 0)
    except ZeroDivisionError:
        print("Error: Se intentó dividir por cero. Asegúrese de que no haya operaciones que puedan provocar este error.")
    except Exception as X:
        print("Ocurrió un error: {}. Por favor, revise su entrada.".format(X))
saludo_usuario()