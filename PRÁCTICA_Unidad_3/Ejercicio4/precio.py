

class Precio():
    def __init__(self, precio_hora: float):
        self.__precio_hora = precio_hora
    
    @property
    def precio_hora(self) -> float:
        return self.__precio_hora
    @precio_hora.setter
    def precio_hora(self, nuevo_precio_hora) -> float:
        self.__precio_hora = nuevo_precio_hora
    
    
    def calcular_importe(self, cant_horas: int) -> float:
        return cant_horas * self.precio_hora
    