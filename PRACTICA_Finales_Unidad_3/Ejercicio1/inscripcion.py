from aspirante import Aspirante
from carrera import Carrera
from datetime import date
from typing import List

class Inscripcion:
    
    _nro_autoincremental = 1
    
    def __init__(self, fecha_inscripcion: date, inscripcion_activa: bool, aspirante: Aspirante, carrera: Carrera):
        Inscripcion._nro_autoincremental += 1
        self.__nro = Inscripcion._nro_autoincremental
        self.__fecha_inscripcion = fecha_inscripcion
        self.__inscripcion_activa = inscripcion_activa
        self.__aspirante = aspirante
        self.__carrera = carrera
        
    @property
    def nro(self) -> int:
        return self.__nro
    
    @property
    def fecha_inscripcion(self) -> date:
        return self.__fecha_inscripcion

    @property
    def inscripcion_activa(self) -> bool:
        return self.__inscripcion_activa
    @inscripcion_activa.setter
    def inscripcion_activa(self, nuevo_inscripcion_activa: bool) -> None:
        self.__inscripcion_activa = nuevo_inscripcion_activa

    @property
    def aspirante(self) -> Aspirante:
        return self.__aspirante

    @property
    def carrera(self) -> Carrera:
        return self.__carrera

    def __str__(self):
        return (
            f"Numero de Inscripcion: {self.nro} | Aspirante: {self.aspirante}\n"
            f"Carrera: {self.carrera}\n"
            f"Fecha de inscripcion: {self.fecha_inscripcion.strftime('%d/%m/%Y')}\n"
            f"Incripcion Activa: [{'Activa' if self.inscripcion_activa else 'No Activa'}]\n"
        )