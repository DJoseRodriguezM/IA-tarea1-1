# Clase Calculadora
# ==============================================================================
# Autor: David José Rodríguez Menjivar
# ==============================================================================
# Descripción:
# Cree una clase Calculadora que pueda realizar las cuatro operaciones matemáticas
# básicas (suma, resta, multiplicación y división).
# Métodos:
# • sumar(a, b)
# • restar(a, b)
# • multiplicar(a, b)
# • dividir(a, b): Debe manejar la división por cero.
# ==============================================================================
# Instrucciones:
# 1. Define la clase Calculadora con los métodos mencionados.
# 2. Cree una instancia de la calculadora.
# 3. Realiza operaciones con números ingresados por el usuario.
# 4. Muestre los resultados de las operaciones.


class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return 'No se puede dividir por cero.'
        else:
            return a / b
        
print('===========================================================')
calculadora = Calculadora()
print('Suma:', calculadora.sumar(20, 2))
print('Resta:', calculadora.restar(20, 2))
print('Multiplicación:', calculadora.multiplicar(20, 2))
print('División:', calculadora.dividir(20, 2))
print('División:', calculadora.dividir(20, 0))
print('===========================================================')