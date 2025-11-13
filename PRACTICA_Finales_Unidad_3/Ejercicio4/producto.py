import string
import random

class Producto():
    
    _codigos_utilizados = set()
    
    def __init__(self, nombre: str, precio_unitario: float):
        
        
        self.__nombre = nombre
        self.__codigo = Producto.generador_codigos_unicos()
        self.__precio_unitario = precio_unitario


    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre) -> str:
        self.__nombre= nuevo_nombre
    
    @property
    def codigo(self) -> str:
        return self.__codigo

    @property
    def precio_unitario(self) -> float:
        return self.__precio_unitario
    @precio_unitario.setter
    def precio_unitario(self, nuevo_precio_unitario) -> float:
        self.__precio_unitario = nuevo_precio_unitario


    @classmethod
    def generador_codigos_unicos(cls) -> str:
        while True:
            codigo = "".join(random.choices(string.ascii_letters + string.digits, k=6))
            if codigo not in cls._codigos_utilizados:
                cls._codigos_utilizados.add(codigo)
                print(f"Código único generado exitosamente: {codigo}")
                return codigo
        
    
    def __str__(self):
        return (
            f"COD: {self.codigo} | {self.nombre} - Precio: ${self.precio_unitario:.2f}"
        )