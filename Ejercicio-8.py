# Contador de Vocales
# ==============================================================================
# Autor: David José Rodríguez Menjivar
# ==============================================================================
# Descripción:
# Escribe una función que cuente el número de vocales en una frase ingresada por el
# usuario.
# ==============================================================================
# Instrucciones:
# 1. Implementa la función contar_vocales(frase).
# 2. Pide al usuario que ingrese una frase.
# 3. Utiliza la función para contar las vocales.
# 4. Muestre el número total de vocales.

# Funcion
def contar_vocales(frase):
    vocales = "aeiou"
    contador = 0
    for letra in frase:
        if letra.lower() in vocales:
            contador = contador + 1
    return contador

# Uso de Funcion
print('===========================================================')
frase = input("Ingresa una frase: ")
print(f"Numero total de vocales en la frase: {contar_vocales(frase)}.")
print('===========================================================')