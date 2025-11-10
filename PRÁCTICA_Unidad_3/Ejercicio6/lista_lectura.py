from datetime import date
from typing import List
from libro import Libro


class ListaLectura():
    def __init__(self, nombre: str, fecha_alta: date):
        self.__nombre = nombre
        self.__fecha_alta = fecha_alta
        self.__libros: List[Libro] = []
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre) -> str:   
        self.__nombre = nuevo_nombre  

    @property
    def fecha_alta(self) -> date:
        return self.__fecha_alta

    @property
    def libros(self) -> List[Libro]:
        return self.__libros

    def cantidad_libros_leidos(self) -> int:
        return len(self.libros)
    
    def add_libro(self, libro: Libro) -> None:
        self.libros.append(libro)
    
    def remove_libro(self, libro: Libro) -> None:
        if libro in self.libros:
            self.libros.remove(libro)
    
    
    def __str__(self):
        return (
            f"Nombre de Lista Lectura: {self.nombre} \n"
            f"Cantidad libros: [{self.cantidad_libros_leidos()}] \n"
            f"Fecha Alta: {self.fecha_alta} \n"
        )
