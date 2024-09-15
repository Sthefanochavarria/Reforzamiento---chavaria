from statistics import median

cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))
alumnos_notas = {}
for a in range(cantidad_alumnos):
        nombre = input("Ingrese el nombre del alumno : ".format(a+1))
        nota = float(input("Ingrese la nota de : ".format(nombre)))
        alumnos_notas[nombre] = nota
        print("{} tiene la nota de {}".format(nombre, nota))
media=median(alumnos_notas.values())
print("La media de las notas son: {}".format(media))
