from datetime import date
import random
import string


class Libro():
    
    _isbn_generados = set()  # <-- acá se guardan los ISBN generados
    
    def __init__(self, nombre: str, autor: str = "Unknown", fecha_lanzamiento: date = None):
        self.__nombre = nombre
        self.__autor = autor
        self.__fecha_lanzamiento = fecha_lanzamiento
        self.__isbn = self.generated_code()
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre) -> str:
        self.__nombre = nuevo_nombre

    @property
    def autor(self) -> str:
        return self.__autor
    @autor.setter
    def autor(self, nuevo_autor) -> str:
        self.__autor = nuevo_autor

    @property
    def fecha_lanzamiento(self) -> date:
        return self.__fecha_lanzamiento
    @fecha_lanzamiento.setter
    def fecha_lanzamiento(self, nuevo_fecha_lanzamiento) -> date:
        self.__fecha_lanzamiento = nuevo_fecha_lanzamiento

    @property
    def isbn(self) -> str:
        return self.__isbn


    def generated_code(self):
        """Genera un código ISBN único de 8 caracteres"""
        while True:
            characters = string.ascii_letters + string.digits
            cod = ''.join(random.choice(characters) for _ in range(8))

            # ✅ Usamos el set _isbn_generados
            if cod not in Libro._isbn_generados:
                Libro._isbn_generados.add(cod)
                return cod
        

    def __str__(self):
        return (
            f"Libro: {self.nombre} | Autor: {self.autor or 'Unknown'} | "
            f"Fecha: {self.fecha_lanzamiento} | ISBN: {self.isbn}"
        )
