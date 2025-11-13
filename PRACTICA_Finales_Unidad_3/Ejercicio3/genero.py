
class Genero():
    def __init__(self, genero: str):
        self.__genero = genero
    
    @property
    def genero(self) -> str:
        return self.__genero
    @genero.setter
    def genero(self, nuevo_genero) -> str:
        self.__genero = nuevo_genero
    
    def __str__(self):
        return (
            f"{self.genero}"
        )