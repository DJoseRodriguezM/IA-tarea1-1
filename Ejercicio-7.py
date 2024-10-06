# Tabla de Multiplicar
# ==============================================================================
# Autor: David José Rodríguez Menjivar
# ==============================================================================
# Descripción:
# Escribe un programa que genere la tabla de multiplicar de un número ingresado por el
# usuario.
# ==============================================================================
# Instrucciones:
# 1. Pide al usuario que ingrese un número entero.
# 2. Utiliza un ciclo for o while para generar la tabla del 1 al 10.
# 3. Muestre la tabla en el formato "n x i = resultado".
# ==============================================================================
# Ejemplo de salida:
# Ingrese un número: 5
# Tabla de multiplicar del 5:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50


print('===========================================================')
n = int(input("Ingrese el número: "))
print(f"Tabla de multiplicar del {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
print('===========================================================')
