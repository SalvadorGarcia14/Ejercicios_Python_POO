from tipo_documento import TipoDocumento
from datetime import date

from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre: str, apellido: str, fecha_nacimiento: date, tipo_documento: TipoDocumento, nro_documento: int):
        
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_nacimiento = fecha_nacimiento
        self.__tipo_documento = tipo_documento
        self.__nro_documento = nro_documento

    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre) -> str:
        self.__nombre = nuevo_nombre


    @property
    def apellido(self) -> str:
        return self.__apellido
    @apellido.setter
    def apellido(self, nuevo_apellido) -> str:
        self.__apellido = nuevo_apellido


    @property
    def fecha_nacimiento(self) -> date:
        return self.__fecha_nacimiento
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, nuevo_fecha_nacimiento) -> date:
        self.__fecha_nacimiento = nuevo_fecha_nacimiento


    @property
    def tipo_documento(self) -> TipoDocumento:
        return self.__tipo_documento


    @property
    def nro_documento(self) -> int:
        return self.__nro_documento
    @nro_documento.setter
    def nro_documento(self, nuevo_nro_documento) -> int:
        self.__nro_documento = nuevo_nro_documento

    
    @property
    def edad(self) -> int:
        hoy = date.today()
        nacimiento = self.fecha_nacimiento
        
        edad = hoy.year - nacimiento.year
        
        ## Si aún no cumplió años este año, se resta uno
        if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
            edad -= 1

        return edad
    












   