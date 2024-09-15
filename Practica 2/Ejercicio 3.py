class BilleteraElectronica:
    TASA_CONVERSION = 3.50

    def __init__(self, nombre, apellido, saldo_soles, saldo_dolares):
        self.nombre = nombre
        self.apellido = apellido
        self.saldo_soles = saldo_soles
        self.saldo_dolares = saldo_dolares

    def transferir(self, monto, desde_moneda, hacia_moneda):
        if desde_moneda == "soles" and hacia_moneda == "dolares":
            if self.saldo_soles >= monto:
                monto_dolares = monto / BilleteraElectronica.TASA_CONVERSION
                self.saldo_soles -= monto
                self.saldo_dolares += monto_dolares
                print(f"Transferencia realizada: S/.{monto:.2f} a ${monto_dolares:.2f}")
            else:
                print("Saldo insuficiente en soles para realizar la transferencia.")

        elif desde_moneda == "dolares" and hacia_moneda == "soles":
            if self.saldo_dolares >= monto:
                monto_soles = monto * BilleteraElectronica.TASA_CONVERSION
                self.saldo_dolares -= monto
                self.saldo_soles += monto_soles
                print(f"Transferencia realizada: ${monto:.2f} a S/.{monto_soles:.2f}")
            else:
                print("Saldo insuficiente en dólares para realizar la transferencia.")

        else:
            print("Tipo de transferencia no soportado.")

    def retirar(self, monto, moneda):
        if moneda == "soles":
            if self.saldo_soles >= monto:
                self.saldo_soles -= monto
                print(f"Retiro realizado: S/.{monto:.2f}")
            else:
                print("Saldo insuficiente en soles para realizar el retiro.")

        elif moneda == "dolares":
            if self.saldo_dolares >= monto:
                self.saldo_dolares -= monto
                print(f"Retiro realizado: ${monto:.2f}")
            else:
                print("Saldo insuficiente en dólares para realizar el retiro.")

        else:
            print("Moneda no soportada.")

billetera1 = BilleteraElectronica("Ricardo", "Soliz", 1000.00, 300.00)
billetera2 = BilleteraElectronica("Maria", "Martínez", 1500.00, 500.00)
billetera3 = BilleteraElectronica("Elizabeth", "Tomako", 2000.00, 1000.00)

billetera1.transferir(500, "soles", "dolares")
billetera2.transferir(200, "dolares", "soles")
billetera3.transferir(100, "dolares", "soles")

billetera1.retirar(200, "soles")
billetera2.retirar(100, "dolares")
billetera3.retirar(1500, "soles")
