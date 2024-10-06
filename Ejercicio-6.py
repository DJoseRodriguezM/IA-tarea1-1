# Secuencia de Fibonacci
# ==============================================================================
# Autor: David José Rodríguez Menjivar
# ==============================================================================
# Descripción:
# Escribe una función llamada fibonacci(n) que imprima los primeros n números de la
# secuencia de Fibonacci.
# ==============================================================================
# Instrucciones:
# 1. Implementa la función fibonacci(n).
# 2. Pide al usuario que ingrese el valor de n.
# 3. Llama a la función para mostrar la secuencia.
# ==============================================================================
# Ejemplo de salida:
# Ingrese el número de términos: 7
# Secuencia de Fibonacci:
# 0, 1, 1, 2, 3, 5, 8

# Funcion
def fibonacci(n):
    x = 0
    y = 1
    aux = 0
    for i in range(n):
        print(x, end=", ")
        aux = x
        x = y
        y = aux + y
    print()

# Uso de Funcion
print('===========================================================')
n = int(input("Ingrese el número de términos: "))
print("Secuencia de Fibonacci:")
fibonacci(n)
print('===========================================================')