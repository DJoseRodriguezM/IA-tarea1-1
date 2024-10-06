# Clase Rectángulo
# ==============================================================================
# Autor: David José Rodríguez Menjivar
# ==============================================================================
# Descripción:
# Cree una clase llamada Rectangulo que represente un rectángulo. La clase debe
# tener los siguientes atributos:
# • base (float)
# • altura (float)
# Y los siguientes métodos:
# • area(): Calcula y devuelve el área del rectángulo.
# • perimetro(): Calcula y devuelve el perímetro del rectángulo.
# ==============================================================================
# Instrucciones:
# 1. Define la clase Rectangulo con el constructor __init__ que inicialice base y
# altura.
# 2. Implementa los métodos area y perimetro.
# 3. Cree una instancia de Rectangulo con base 5 y altura 3.
# 4. Muestre el área y el perímetro del rectángulo.

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)
    
rectangulo = Rectangulo(20, 10)
print('Área:', rectangulo.area())
print('Perímetro:', rectangulo.perimetro())
