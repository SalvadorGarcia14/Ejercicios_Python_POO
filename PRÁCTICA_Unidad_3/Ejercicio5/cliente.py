from datetime import date
from localidad import Localidad

class Cliente():
    
    _nuo_cliente_increment = 1
    
    def __init__(self, nombre: str, direccion: str, localidad: Localidad ,fecha_alta: date, fecha_baja: date = None):
        
        
        self.__nro_cliente = Cliente._nuo_cliente_increment
        Cliente._nuo_cliente_increment += 1
        
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__fecha_alta = fecha_alta
        self.__fecha_baja = fecha_baja
    
    
    @property
    def nro_cliente(self) -> int:
        return self.__nro_cliente
    
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre) -> str:
        self.__nombre = nuevo_nombre


    @property
    def direccion(self) -> str:
        return self.__direccion
    @direccion.setter
    def direccion(self, nuevo_direccion) -> str:
        self.__direccion = nuevo_direccion
        

    @property
    def localidad(self) -> Localidad:
        return self.__localidad
    
    
    @property
    def fecha_alta(self) -> date:
        return self.__fecha_alta
    
    
    @property
    def fecha_baja(self) -> date:
        return self.__fecha_baja
    @fecha_baja.setter
    def fecha_baja(self, nuevo_fecha_baja) -> date:
        self.__fecha_baja = nuevo_fecha_baja


    def reactivar_cliente(self):
        self.fecha_baja = None

    def eliminar_cliente(self):
        self.fecha_baja = date.today()    


    def __str__(self):
        return (
            f"Nro: {self.nro_cliente} | Nombre: {self.nombre} \n"
            f"Direccion: {self.direccion} - Localidad: {self.localidad}  \n"
            f"Estado: {"Activo" if self.fecha_baja is None else "Inactivo"} \n"
            f"Fecha Alta: {self.fecha_alta} \n"
            f"Fecha Baja: {"" if self.fecha_baja is None else self.fecha_baja}\n"
        )