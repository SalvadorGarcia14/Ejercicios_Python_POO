from abc import abstractmethod, ABC
from datetime import datetime

class Persona(ABC):
    def __init__(self, nombre: str, apellido: str, fecha_nacimiento: datetime, nro_documento: int):
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
    def fecha_nacimiento(self) -> datetime:
        return self.__fecha_nacimiento
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, nuevo_fecha_nacimiento) -> datetime:
        self.__fecha_nacimiento = nuevo_fecha_nacimiento

    @property
    def nro_documento(self) -> int:
        return self.__nro_documento

    @property
    def edad(self) -> int:
        hoy = datetime.today().date()
        nacimiento = self.fecha_nacimiento  # ya es date()

        return hoy.year - nacimiento.year - (
            (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day)
        )


    def __str__(self):
        return (
            f"{self.nombre} {self.apellido} \n"
            f"Fecha Nacimiento: {self.fecha_nacimiento} | Edad: {self.edad} \n"
            f"DNI: {self.nro_documento} \n"
        )
