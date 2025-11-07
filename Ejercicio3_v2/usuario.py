from persona import Persona
from libro import Libro

from datetime import date
from typing import List


class Usuario(Persona):
    
    _user_name_utilizados = set()

    def __init__(self, nombre, apellido, fecha_nacimiento, tipo_documento, nro_documento,
            user_name: str, estado: bool, email: str ,password: str, fecha_alta: date, 
            fecha_baja: date = None , administrador: bool = False):
        super().__init__(nombre, apellido, fecha_nacimiento, tipo_documento, nro_documento)
        
        if user_name in Usuario._user_name_utilizados:
            raise ValueError(f"El user name '{user_name}' ya está en uso. Debe ser único.")

        Usuario._user_name_utilizados.add(user_name)
        
        self.__user_name = user_name
        self.__estado = estado
        self.__email = email
        self.__password = password
        self.__fecha_alta = fecha_alta
        self.__fecha_baja = fecha_baja
        self.__administrador = administrador
        
        self.__libros: List[Libro] = []


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
    def email(self) -> str:
        return self.__email
    @email.setter
    def email(self, nuevo_email) -> str:
        self.__email = nuevo_email

    @property
    def password(self) -> str:
        return self.__password
    @password.setter
    def password(self, nuevo_password) -> str:
        self.__password = nuevo_password


    @property
    def fecha_alta(self) -> date:
        return self.__fecha_alta
    
    @property
    def fecha_baja(self) -> date:
        return self.__fecha_baja   
    @fecha_baja.setter
    def fecha_baja(self, nuevo_fecha_baja) -> date:
        self.__fecha_baja = nuevo_fecha_baja


    @property
    def administrador(self) -> bool:
        return self.__administrador
    @administrador.setter
    def administrador(self, nuevo_administrador) -> bool:
        self.__administrador = nuevo_administrador


    @property
    def libros(self) -> List:
        return self.__libros


    def validar_credenciales(self, username: str, contra: str) -> bool:
        print("Validando...")
        if username == self.user_name and contra == self.password:
            print(f"Usuario Validado {self.user_name} [{True}]")
            return True
        print(f"Usuario no encontrado... [{False}]")
        return False

    def add_libro(self, libro: Libro) -> None:
        self.libros.append(libro)

    def remove_libro(self, libro: Libro) -> None:
        if libro in self.libros:
            self.libros.remove(libro)
            
    def leyo_libro(self, isbn: str) -> bool:
        for libro in self.libros:
            if libro.isbn == isbn:
                print(libro)
                return True
        print("No existen libros")
        return False
    
    def baja_usuario(self) -> None:
        self.estado = False
        self.fecha_baja = date.today()
    
    def __str__(self):
        return (
        f"{self.nombre} {self.apellido} \n"
        f"Fecha de Nacimiento: {self.fecha_nacimiento} | Edad: {self.edad} \n"
        f"{self.tipo_documento} -> {self.nro_documento} \n"
        
        f"{"-" * 20}"
        
        f"UserName: {self.user_name} | Email: {self.email} \n"
        f"Estado: {'Activo' if self.estado else 'Baja'} \n"
        f"Fecha Alta: {self.fecha_alta}\n"
        f"Fecha Baja: {self.fecha_baja if self.fecha_baja is not None else ''} \n" 
        f"ADM: {self.administrador } \n"
        )