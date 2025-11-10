from abc import ABC, abstractmethod
from datetime import date


class Persona(ABC):

    _nro_documentos_registrados = set()

    def __init__(self, nombre: str, apellido: str, fecha_nacimiento: date, nro_documento: int):

        # Validación: documento único
        if nro_documento in Persona._nro_documentos_registrados:
            raise ValueError(f"El documento '{nro_documento}' ya está registrado. ")

        Persona._nro_documentos_registrados.add(nro_documento)

        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_nacimiento = fecha_nacimiento
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
    def nro_documento(self) -> int:
        return self.__nro_documento


    @property
    def edad(self) -> int:
        hoy = date.today()
        nacimiento = self.fecha_nacimiento
        
        edad = hoy.year - nacimiento.year
        
        if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
            edad -= 1
        
        return edad