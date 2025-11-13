from genero import Genero
from autor import Autor

from datetime import date
from typing import List

class Libro():
    def __init__(self, nombre: str, fecha_publicacion: date, genero: Genero,  autor: Autor = None):
        self.__nombre = nombre
        self.__fecha_publicacion = fecha_publicacion
        self.__genero = genero
        self.__autor = autor
        self.__generos:List [Genero] = []
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre) -> str:
        self.__nombre= nuevo_nombre
    
    @property
    def fecha_publicacion(self) -> date:
        return self.__fecha_publicacion

    @property
    def genero(self) -> Genero:
        return self.__genero

    @property
    def autor(self) -> Autor:
        return self.__autor

    @property
    def generos(self) -> List:
        return self.__generos

    def add_genero(self, genero: Genero):
        self.generos.append(genero)

    def remuve_genero(self, genero: Genero):
        if genero in self.genero:
            self.generos.remove(genero)
        else:
            print("El genero no existe en el libro")
    
    def __str__(self):
        generos_str = ",".join(str(genero) for genero in self.generos) if self.generos else "Sin genero"
        
        if self.autor:
            autor_str = f"{self.autor.nombre} {self.autor.apellido}"
        else:
            autor_str = "Unknown"
        return (
            f"Libro: {self.nombre} | Fecha Publicado: {self.fecha_publicacion.strftime("%d/%m/%Y")} || Autor: {autor_str} - Generos: {generos_str} \n"
        )