from persona import Persona
from libro import Libro

from datetime import date
from typing import List

class Usuario(Persona):
    
    _user_name_utilizados = set()
    
    def __init__(self, nombre, apellido, fecha_nacimiento, nro_documento, tipo_documento,
                user_name: str, estado: bool, password: str, email: str, fecha_alta: date,
                administrador: bool = False, fecha_baja: date = None):
        
        super().__init__(nombre, apellido, fecha_nacimiento, nro_documento, tipo_documento)
        
        if not Usuario.validar_user_name_unico(user_name):
            raise ValueError(f"El nombre de usuario '{user_name}' ya está tomado.")  
        
        self.__user_name = user_name
        Usuario._user_name_utilizados.add(user_name) 
                   
        self.__estado = estado
        self.__password = password
        self.__email = email
        self.__fecha_alta = fecha_alta
        self.__administrador = administrador
        self.__fecha_baja = fecha_baja
        self.__libros: List = []
    
    @property
    def user_name(self) -> str:
        return self.__user_name
    
    
    @property
    def estado(self) -> bool:
        return self.__estado
    @estado.setter
    def estado(self, nuevo_estado) -> bool:
        self.__estado = nuevo_estado
    
    
    @property
    def password(self) -> str:
        return self.__password
    @password.setter
    def password(self, nuevo_password) -> str:
        self.__password = nuevo_password


    @property
    def email(self) -> str:
        return self.__email
    @email.setter
    def email(self, nuevo_email) -> str:
        self.__email = nuevo_email


    @property
    def fecha_alta(self) -> date:
        return self.__fecha_alta 


    @property
    def administrador(self) -> bool:
        return self.__administrador
    @administrador.setter
    def administrador(self, nuevo_administrador) -> bool:
        self.__administrador = nuevo_administrador


    @property
    def fecha_baja(self) -> date:
        return self.__fecha_baja
    @fecha_baja.setter
    def fecha_baja(self, nuevo_fecha_baja) -> date:
        self.__ffecha_baja = nuevo_fecha_baja

    @property
    def libros(self) -> List:
        return self.__libros 

    @classmethod
    def validar_user_name_unico(cls, user_name: str) -> bool:
        #Retorna True si el user_name esta disponible
        if user_name not in cls._user_name_utilizados:
            return True
        return False    
    
    def validar_credenciales(self, username: str, contra: str) -> bool:
        print("Validando...")
        if username == self.user_name and contra == self.password:
            print(f"Usuario Validado {self.user_name} [{True}]")
            return True
        print(f"Usuario no encontrado... [{False}]")
        return False
    
    def baja_usuario(self) -> None:
        self._estado = False
        self._fecha_baja = date.today()
    
    def add_libro(self, libro: Libro) -> None:
        if libro not in self.libros:
            self.libros.append(libro)

    def remove_libro(self, libro: Libro) -> None:
        if libro in self.libros:
            self.libros.remove(libro)
    
    def leyo_libro(self, isbn: str) -> bool:
        for libro in self.libros:
            if libro.isbn == isbn:
                return True
        return False
            

    def __str__(self):
        return (
            
        f"{self.nombre} {self.apellido} \n"
        f"Fecha de Nacimiento: {self.fecha_nacimiento} | Edad: {self.edad} \n"
        f"Tipo: {self.tipo_documento} -> {self.nro_documento} \n"
        
        f"UserName: {self.user_name} | Email: {self.email} \n"
        f"ADM: {self.administrador } \n"
        f"Estado: {'Activo' if self.estado else 'Baja'}\n"
        f"Fecha Alta: {self.fecha_alta}\n"
        f"Fecha Baja: {self.fecha_baja if self.fecha_baja is not None else ''} \n"        
    )