from abc import abstractmethod, ABC
from tipodocumento import TipoDocumento
from datetime import date


class Persona(ABC):
    def __init__(self, nombre: str, apellido: str, fecha_nacimiento: date, nro_documento: int, tipo_documento: TipoDocumento):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_nacimiento = fecha_nacimiento
        self.__nro_documento = nro_documento
        self.__tipo_documento = tipo_documento

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
    def nro_documento(self) -> str:
        return self.__nro_documento

    @property
    def edad(self) -> date:
        hoy = date.today()
        nacimiento = self.fecha_nacimiento  # ya es date()

        return hoy.year - nacimiento.year - (
            (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day)
        )
    
    @property
    def tipo_documento(self) -> TipoDocumento:
        return self.__tipo_documento

    
    def __str__(self):
        pass
        # return (
        #     # f"{self.nombre} {self.apellido}"
        #     # f"Fecha de Nacimiento: {self.fecha_nacimiento} | Edad: {self.edad}"
        #     # f"DNI: {self.nro_documento}"
        # )