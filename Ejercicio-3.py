# Clase CuentaBancaria
# ==============================================================================
# Autor: David José Rodríguez Menjivar
# ==============================================================================
# Descripción:
# Cree una clase CuentaBancaria que modele una cuenta bancaria sencilla. La clase
# debe tener:
# • Atributos:
# o titular (str)
# o saldo (float), inicializado en cero.
# • Métodos:
# o depositar(cantidad): Aumenta el saldo en la cantidad especificada.
# o retirar(cantidad): Disminuye el saldo en la cantidad especificada si hay
# fondos suficientes.
# o mostrar_saldo(): Muestre el saldo actual.
# ==============================================================================
# Instrucciones:
# 1. Define la clase con los atributos y métodos mencionados.
# 2. Cree una instancia de CuentaBancaria para un titular ficticio.
# 3. Realiza algunas operaciones de depósito y retiro.
# 4. Muestre el saldo después de cada operación.

class CuentaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, cantidad):
        self.saldo = cantidad + self.saldo

    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo = self.saldo - cantidad  
        else:
            print('Fondos insuficientes.')

    def mostrar_saldo(self):
        print('Saldo actual:', self.saldo)

print('===========================================================')
cuenta = CuentaBancaria('David Rodríguez')
print('Cuenta bancaria de: ' + cuenta.titular) 
cuenta.mostrar_saldo()
cuenta.depositar(1000)
cuenta.mostrar_saldo()
cuenta.retirar(509)
cuenta.mostrar_saldo()
print('===========================================================')

