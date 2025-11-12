from titulo import Titulo
from datetime import date
from typing import List


class Carrera():
    def __init__(self, nombre: str, comiendozo: date):
        self.__nombre = nombre
        self.__comiendozo = comiendozo
        self.__cantidad_titlos_requeridos = 0
        self.__titulos: List[Titulo] = []

    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> str:
        self.__nombre = nuevo_nombre


    @property
    def comiendozo(self) -> date:
        return self.__comiendozo
    @comiendozo.setter
    def comiendozo(self, nuevo_comiendozo: date) -> date:
        self.__comiendozo = nuevo_comiendozo

    @property
    def cantidad_titlos_requeridos(self) -> int:
        return self.__cantidad_titlos_requeridos
    @cantidad_titlos_requeridos.setter
    def cantidad_titlos_requeridos(self, nuevo_cantidad_titlos_requeridos: int) -> int:
        self.__cantidad_titlos_requeridos = nuevo_cantidad_titlos_requeridos
        
    @property
    def cantidad_titulos_requeridos(self) -> int:
        return len(self.__titulos)

    @property
    def titulos(self) -> List[Titulo]:
        return self.__titulos
    
    @property
    def titulos(self) -> List:
        return self.__titulos

    def add_titulo_requerido(self, titulo: Titulo):
        if titulo not in self.titulos:
            self.titulos.append(titulo)
    
    def remove_titulo_requerido(self, titulo: Titulo):
        if titulo in self.titulos:
            self.titulos.remove(titulo)
    
    
    def __str__(self):
        return (
            f"Carrera: {self.nombre} \n"
            f"Comiendo: {self.comiendozo.strftime('%m/%Y')} - Títulos Requeridos: [{self.cantidad_titulos_requeridos}]\n \n"
        )