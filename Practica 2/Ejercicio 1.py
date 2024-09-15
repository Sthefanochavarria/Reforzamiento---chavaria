class Persona:
    def __init__(self, nombre, edad, saldo):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
        self.nacionalidad = "Peruana"

    def solicitar_datos(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

    def cumplir_año(self):
        self.edad += 1

    def aumento_sueldo(self):
        self.saldo *= 1.30

    def edad_en_año(self, año):
        edad_futura = self.edad + (año - 2024)
        return f"En el año {año} tendrá {edad_futura} años"

persona1 = Persona("Sthefano", 22, 2000)
persona2 = Persona("Maria", 28, 2300)

print(persona1.solicitar_datos())

persona1.aumento_sueldo()
print(f"Saldo de {persona1.nombre} después del aumento: {persona1.saldo}")
print(persona2.solicitar_datos())
persona2.aumento_sueldo()
print(f"Saldo de {persona2.nombre} después del aumento: {persona2.saldo}")
print(persona1.edad_en_año(2025))
print(persona2.edad_en_año(2025))

