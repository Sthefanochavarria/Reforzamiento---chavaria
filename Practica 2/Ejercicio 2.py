class Persona:
    def __init__(self, nombre, edad, saldo):
        self.nombre = nombre
        self.edad = edad
        self.__saldo = saldo

    def solicitar_datos(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

    def cumplir_año(self):
        self.edad += 1

    def aumento_sueldo(self):
        self.__saldo *= 1.30

    def mostrar_saldo(self):
        return f"Saldo de {self.nombre}: ${self.__saldo:.2f}"

    def transferencia(self, monto, otra_persona):
        if monto <= 0:
            print("El monto de la transferencia debe ser positivo.")
            return

        if self.__saldo >= monto:
            self.__saldo -= monto
            otra_persona.__saldo += monto
            print(f"Transferencia de ${monto:.2f} realizada a {otra_persona.nombre}.")
        else:
            print("Saldo insuficiente.")

    def edad_en_año(self, año):
        edad_futura = self.edad + (año - 2024)
        return f"En el año {año} tendrá {edad_futura} años"


persona1 = Persona("Sthefano", 22, 2000.00)
persona2 = Persona("Maria", 28, 2300.00)

print(persona1.solicitar_datos())
print(persona1.mostrar_saldo())
print(persona2.solicitar_datos())
print(persona2.mostrar_saldo())

persona1.transferencia(500, persona2)

print(persona1.mostrar_saldo())
print(persona2.mostrar_saldo())

