def acceder_a_lista(indice):
    lista = [2, 6, 10, 4, 5, 23, 1]
    try:
        valor = lista[indice]
        print("El valor en el índice {} es: {}".format(indice, valor))
    except IndexError as X:
        print("Error: {}".format(X))
        print("Causa: Intentaste acceder a un índice que está fuera del rango de la lista.")
        print("Solución: Asegúrate de que el índice esté entre 0 y", len(lista) - 1)
acceder_a_lista(10)