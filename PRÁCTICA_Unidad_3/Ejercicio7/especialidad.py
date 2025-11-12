from medico import Medico
from typing import List

import random
import string

class Especialidad():
    
    _codigos_registrados = set()
    
    def __init__(self, nombre: str, codigo: int):
        self.__nombre = nombre
        # Si no se pasa un código, se genera automáticamente
        self.__codigo = codigo if codigo is not None else Especialidad.crear_codigo_random()
        self.__medicos: List[Medico] = []
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre) -> str:
        self.__nombre = nuevo_nombre
    
    @property
    def codigo (self) -> int:
        return self.__codigo 
    
    @property
    def medicos (self) -> List[Medico]:
        return self.__medicos
    
    @classmethod
    def crear_codigo_random(cls): #Genera un código numérico aleatorio de 6 dígitos y se asegura de que sea único.
        while True:
            codigo = random.randint(100000, 999999)  # 6 dígitos numéricos
            if codigo not in cls._codigos_registrados:
                cls._codigos_registrados.add(codigo)
                return codigo
    
    def add_medico(self, medico: Medico):
        self.medicos.append(medico)
    
    def remuve_medico(self, medico: Medico):
        if medico in self.medicos:
            self.medicos.remove(medico)
    
    
    def __str__(self):
        return (
            f"Especialidad: {self.nombre} | Codigo: {self.codigo} \n"
        )