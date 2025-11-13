from datetime import date

class Autor():
    def __init__(self, nombre: str, apellido: str, fecha_nacimiento: date):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_nacimiento = fecha_nacimiento

    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre) -> str:
        self.__nombre= nuevo_nombre
    
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
    
    
    def __str__(self):
        return (
            f"Nombre y Apellido: {self.nombre} {self.apellido} - Fecha Nacimiiento: {self.fecha_nacimiento.strftime("%d/%m/%Y")}  \n"
        )