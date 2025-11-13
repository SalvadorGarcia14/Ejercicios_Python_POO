from libro import Libro

import random 
import string
from typing import List


class ListaLectura():
    
    _codigos_utilizados = set()
    
    def __init__(self, nombre: str):
        
        self.__codigo = ListaLectura.generador_codigos_unicos()
        self.__nombre = nombre
        self.__libros: List[List] = []
    
    @property
    def codigo(self) -> int:
        return self.__codigo
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre) -> str:
        self.__nombre= nuevo_nombre

    @property
    def libros(self) -> List:
        return self.__libros
    
    @property
    def cantidad_libros(self) -> int:
        return len(self.libros)
        
    @classmethod
    def generador_codigos_unicos(cls) -> int:
        while True:
            # ✅ CORREGIDO: random.choices (no random.choice)
            codigo = int("".join(random.choices(string.digits, k=4)))
            if codigo not in cls._codigos_utilizados:
                cls._codigos_utilizados.add(codigo)
                print(f"Código único generado exitosamente: {codigo}")
                return codigo
    
    def add_libro(self, libro: Libro):
        if libro not in self.libros:
            self.libros.append(libro)
        else:
            print("El libro ya existe")

    def remuve_libro(self, libro: Libro):
        if libro in self.libros:
            self.libros.remove(libro)
        else:
            print("El libro no existe en la lista")
    
    def __str__(self):
        return (
            f"Codigo: {self.codigo} || Nombre de Lista Lectura: {self.nombre} - Cantidad de Libros: [{self.cantidad_libros}] \n"
        )