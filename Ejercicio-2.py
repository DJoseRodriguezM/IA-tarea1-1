# Clase Libro
# ==============================================================================
# Autor: David José Rodríguez Menjivar
# ==============================================================================
# Descripción:
# Cree una clase llamada Libro que tenga los siguientes atributos:
# • titulo (str)
# • autor (str)
# • anio_publicacion (int)
# • numero_paginas (int)
# Y un método:
# • mostrar_informacion(): Imprime la información del libro.
# ==============================================================================
# Instrucciones:
# 1. Define la clase Libro con el constructor correspondiente.
# 2. Implementa el método mostrar_informacion.
# 3. Cree una instancia de Libro con información de un libro de tu elección.
# 4. Llama al método mostrar_informacion.


class Libro:
    def __init__(self, titulo, autor, anio_publicacion, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.numero_paginas = numero_paginas

    def mostrar_informacion(self):
        print('Título:', self.titulo)
        print('Autor:', self.autor)
        print('Año de publicación:', self.anio_publicacion)
        print('Número de páginas:', self.numero_paginas)

print('===========================================================')
libro = Libro('Juego de tronos', 'George R. R. Martin', 1996, 672)
libro.mostrar_informacion()
print('===========================================================')
