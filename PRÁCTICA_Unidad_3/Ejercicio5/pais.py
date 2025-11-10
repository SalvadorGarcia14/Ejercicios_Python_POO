from provincia import Provincia
from typing import List


class Pais():
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__provincias: List[Provincia] = []

    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre) -> str:
        self.__nombre = nuevo_nombre
    
    @property
    def provincias(self) -> Provincia:
        return self.__provincias
    
    def add_provincia(self, provincia: Provincia):
        if provincia not in self.provincias:
            self.provincias.append(provincia)

    def remove_provincia(self, provincia: Provincia):
        if provincia in self.provincias:
            self.provincias.remove(provincia)

    def __str__(self):
        return (
            f"{self.nombre}\n"
        )