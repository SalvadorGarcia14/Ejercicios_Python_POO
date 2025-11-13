

class Descuento():
    def __init__(self, porcentaje_descuento_comunidad: float):
        self.__porcentaje_descuento_comunidad = porcentaje_descuento_comunidad
    
    @property
    def porcentaje_descuento_comunidad(self) -> float:
        return self.__porcentaje_descuento_comunidad
    @porcentaje_descuento_comunidad.setter
    def porcentaje_descuento_comunidad(self, nuevo_porcentaje_descuento_comunidad) -> float:
        self.__porcentaje_descuento_comunidad = nuevo_porcentaje_descuento_comunidad

    def calcular_monto_descuento_comunidad(self, monto: float) -> float:
        return monto * (self.porcentaje_descuento_comunidad / 100)