from datetime import date, time

from medico import Medico
from paciente import Paciente


class Turno():
    def __init__(self, fecha: date, hora: time, estado: str, autorizado: bool, medico: Medico, paciente: Paciente):
        
        self.__fecha = fecha
        self.__hora = hora
        self.__estado = estado
        self.__autorizado = autorizado
        self.__medico = medico
        self.__paciente = paciente

    @property
    def fecha(self) -> date:
        return self.__fecha
    @fecha.setter
    def fecha(self, nuevo_fecha) -> date:
        self.__fecha = nuevo_fecha


    @property
    def hora(self) -> time:
        return self.__hora
    @hora.setter
    def hora(self, nuevo_hora) -> time:
        self.__hora = nuevo_hora

    @property
    def estado(self) -> str:
        return self.__estado
    @estado.setter
    def estado(self, nuevo_estado) -> str:
        self.__estado = nuevo_estado


    @property
    def autorizado(self) -> bool:
        return self.__autorizado
    @autorizado.setter
    def autorizado(self, nuevo_autorizado) -> bool:
        self.__autorizado = nuevo_autorizado


    @property
    def medico(self) -> Medico:
        return self.__medico


    @property
    def paciente(self) -> Paciente:
        return self.__paciente
    
    def ingresar_paciente(self, token: int) -> bool: #Autoriza el turno y cambia el estado a ingresado
        self.autorizado = True
        self.estado = "Reservado"
        return True

    def cancelar_turno(self) -> str:
        self.estado = "Cancelado"
        return "Turno cancelado correctamente."

    
    def __str__(self):
        return (
            f"Fecha: {self.fecha} - {self.hora} \n"
            f"Paciente: {self.paciente} \n"
            f"{"-" * 20}\n"
            f"Medico: {self.medico} \n"
            f"{"-" * 20}\n"
            f"Estado: {self.estado if "Reservado" else "Cancelado"} | Autorizado: [{self.autorizado}]"
        )