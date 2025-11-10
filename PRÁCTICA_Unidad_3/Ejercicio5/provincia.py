from localidad import Localidad
from typing import List

class Provincia():
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__localidades: List[Localidad] = []
    
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre) -> str:
        self.__nombre = nuevo_nombre
    
    @property
    def localidades(self) -> Localidad:
        return self.__localidades

    def add_localidad(self, localidad: Localidad):
        if localidad not in self.localidades:
            self.localidades.append(localidad)

    def remove_localidad(self, localidad: Localidad):
        if localidad in self.localidades:
            self.localidades.remove(localidad)
    
    
    def __str__(self):
        return (
            f"{self.nombre}\n"
        )