rango= int(input("El tamaño de la lista es de: "))
var1= []

for a in range(rango):
    nombre = input("Ingrese el nombre del alumno {}: ".format(a + 1))
    var1.append(nombre)

print(len(var1),
      "Nombres: {}".format(var1))
