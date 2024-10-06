# Generador de Contraseñas
# ==============================================================================
# Autor: David José Rodríguez Menjivar
# ==============================================================================Descripción:
# Cree una función que genere una contraseña aleatoria con una longitud especificada
# por el usuario. La contraseña debe contener letras mayúsculas, minúsculas,
# números y símbolos.
# ==============================================================================
# Instrucciones:
# 1. Utilice la clase Random para ayudarse a generar una contraseña segura de
# mínimo 8 caracteres.
# 2. Muestre la contraseña generada.


import random
import string

# Funcion
def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = "".join(random.choice(caracteres) for i in range(longitud))
    return contrasena

# Uso de Funcion
print('===========================================================')
longitud = int(input("Ingrese la longitud de la contraseña: "))
print(f"Contraseña generada: {generar_contrasena(longitud)}")
print('===========================================================')