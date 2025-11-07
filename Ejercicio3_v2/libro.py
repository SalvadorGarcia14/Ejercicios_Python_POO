from datetime import date

import random
import string

class Libro():
    
    _isbn_generados = set()

    def __init__(self, nombre: str, autor: str, fecha_lanzamiento: str, isbn: str = None):

        self.__nombre = nombre
        self.__autor = autor
        self.__fecha_lanzamiento = fecha_lanzamiento

        # Si el ISBN viene como argumento
        if isbn is not None:
            if isbn in Libro._isbn_generados:
                raise ValueError("El ISBN ya existe, debe ser único.")
            self.__isbn = isbn
            Libro._isbn_generados.add(isbn)

        # Si no viene, se genera uno automáticamente
        else:
            self.__isbn = Libro.generar_ISBN()

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
    
    @classmethod
    def generar_ISBN(cls) -> str:
        characters = string.ascii_letters + string.digits
        
        while True:
            cod = ''.join(random.choice(characters) for _ in range(8))

            if cod not in cls._isbn_generados:
                cls._isbn_generados.add(cod)
                return cod

    
    def __str__(self):
        return (
            f"Titulo: {self.nombre} | Fecha: {self.fecha_lanzamiento} \n"
            f"Autor: {self.autor} | ISBN: {self.isbn} \n"
        )