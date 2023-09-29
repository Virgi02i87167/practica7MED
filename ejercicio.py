class SaldoInsuficienteError(Exception):
    pass

class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def Retirar(self, cantidad):
        try:
            if cantidad <= 0 :
                raise ValueError("La cantidad ingresada debe ser mayor que cero.")
            if cantidad >= self.saldo:
                raise ValueError("Saldo insuficiente en la cuenta")
            
            self.saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")
        
        except ValueError as e:
            print(f"Error: {e}")
        
        except SaldoInsuficienteError as e:
            print(f"Error: {e}")

cuenta = CuentaBancaria(1000)

#cuenta.Retirar(500)
#cuenta.Retirar(-200)
#cuenta.Retirar(1000)
try:
    cantidad_retirar = float(input("Digite la cantidad a retirar: "))
    cuenta.Retirar(cantidad_retirar)
except ValueError as e:
    print(e)