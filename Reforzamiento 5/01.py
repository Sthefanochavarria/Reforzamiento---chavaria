def sumar():
    try:
        suma = 80 + "Hola Pythonista"
    except TypeError as X:
        print("Error: {}".format(X))
        print("Causa: Intentaste sumar un número a una cadena de texto.")
        print("Solución: Asegúrate de que ambos operandos sean del mismo tipo, "
              "por ejemplo, convierte la cadena a un número o usa un número en lugar de una cadena.")
sumar()