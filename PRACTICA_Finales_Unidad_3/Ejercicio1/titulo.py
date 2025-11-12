

class Titulo():
    def __init__(self, nombre: str, universidad: str):
        self.__nombre = nombre
        self.__universidad = universidad
    
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre
    
    
    @property
    def universidad(self):
        return self.__universidad
    @universidad.setter
    def universidad(self, nuevo_univarsidad: str) -> str:
        self.__universidad = nuevo_univarsidad
    
    def __str__(self):
        return (
            f"Titulo: {self.nombre} || Universidad: {self.universidad} \n"
        )
