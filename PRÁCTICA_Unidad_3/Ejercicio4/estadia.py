from datetime import datetime, date, time
import math

from precio import Precio

class Estadia():
    
    _patentes_registradas = set()
    
    def __init__(self, fecha: date, nro_patente: str, estado: str, hora_entrada: time ,hora_salida: time = None, pagado: bool = False):
        
        if nro_patente in Estadia._patentes_registradas:
            raise ValueError(f"La patente '{nro_patente}' ya está registrada.")
        Estadia._patentes_registradas.add(nro_patente)

        
        self.__fecha = fecha
        self.__nro_patente = nro_patente
        self.__estado = estado
        self.__hora_entrada = hora_entrada
        self.__hora_salida = hora_salida
        self.__pagado = pagado
    
    @property
    def fecha(self) -> date:
        return self.__fecha
    @fecha.setter
    def fecha(self, nueva_fecha) -> date:
        self.__fecha = nueva_fecha


    @property
    def nro_patente(self) -> str:
        return self.__nro_patente

           
    @property
    def hora_entrada(self) -> time:
        return self.__hora_entrada
    @hora_entrada.setter
    def hora_entrada(self, nueva_hora_entrada) -> time:
        self.__hora_entrada = nueva_hora_entrada    


    @property
    def hora_salida(self) -> time:
        return self.__hora_salida
    @hora_salida.setter
    def hora_salida(self, nueva_hora_salida) -> time:
        self.__hora_salida = nueva_hora_salida


    @property
    def estado(self) -> str:
        return self.__estado
    @estado.setter
    def estado(self, nueva_estado) -> str:
        self.__estado = nueva_estado


    @property
    def pagado(self) -> bool:
        return self.__pagado
    @pagado.setter
    def pagado(self, nueva_pagado) -> bool:
        self.__pagado = nueva_pagado

    @property
    def cant_horas(self) -> int:
        #Calcula la diferencia de horas redondeando
    
        if not self.hora_salida:
            return 0
    
        entrada_dt = datetime.combine(self.fecha, self.hora_entrada)
        salida_dt = datetime.combine(self.fecha, self.hora_salida)

        diferencia = salida_dt - entrada_dt
        horas = diferencia.total_seconds() / 3600
        
        self._cant_horas = math.ceil(horas)  # redondea hacia arriba
        return self._cant_horas

    
    def registrar_salida(self, hora_salida: time, precio: Precio) -> float:
        self.hora_salida = hora_salida
        self.estado = "FINALIZADA"

        horas_cobradas = self.cant_horas  #property
        importe = precio.calcular_importe(horas_cobradas)

        self.pagado = True
        return importe
    
    def __str__(self):
        return (
            f"Patente: {self.nro_patente} \n"
            f"Estado: {'FINALIZADA' if self.estado == 'FINALIZADA' else 'EN_CURSO'} \n"
            f"Hora entrada: {self.hora_entrada} \n"
            f"Hora salida: {self.hora_salida} \n"
            f"Horas: {self.cant_horas} \n"
            f"Pagado: [{self.pagado}] \n"
        )