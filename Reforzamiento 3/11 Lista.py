BD=["MySQL", "PostgreSQL", "SQLite", "Oracle", "SQL Server"]
print("Base de datos:{} ".format(BD))
nombre_BD= input("Ingrese el nombre de la base de datos a eleminar o agregar: ")
if nombre_BD in BD:
    BD.remove(nombre_BD)
    print("Ha sido elminado de la lista: {}".format(nombre_BD))
else:
    BD.append(nombre_BD)
    print("Ha sido agregado a la lista: {}".format(nombre_BD))

print("Lista actualizada: {}".format(BD))

