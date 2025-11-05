from datetime import date
from typing import List

class Usuario():
    def __init__(self, user_name: str, estado: bool, email: str, password: str, 
                nombre: str, apellido: str, fecha_alta: date, fecha_baja: date):
        
        self.__user_name = user_name
        self.__estado = estado
        self.__email = email
        self.__password = password
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_alta = fecha_alta
        self.__fecha_baja = fecha_baja

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
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre) -> str:
        self.__nombre = nuevo_nombre
        
        
    @property
    def apellido(self) -> str:
        return self.__apellido
    @apellido.setter
    def apellido(self, nuevo_apellido) -> str:
        self.__apellido = nuevo_apellido


    @property
    def fecha_alta(self) -> date:
        return self.__fecha_alta
    @fecha_alta.setter
    def fecha_alta(self, nuevo_fecha_alta) -> date:
        self.__fecha_alta = nuevo_fecha_alta


    @property
    def fecha_baja(self) -> date:
        return self.__fecha_baja
    @fecha_baja.setter
    def fecha_baja(self, nuevo_fecha_baja) -> date:
        self.__fecha_baja = nuevo_fecha_baja
        

    def validar_credenciales(self, usuario: str, contra: str) -> bool:
        print("Validando...")
        if usuario == self.user_name and contra == self.password:
            print(f"Usuario Validado {self.user_name} [{True}]")
            return True
        print(f"Usuario no encontrado... [{False}]")
        return False

    def baja_usuario(self, lista_usuarios):
        usuario_ingresado = input("Ingrese el usuario a dar de baja: ")
         
        for usuario in lista_usuarios:
            if usuario.user_name == usuario_ingresado:
                usuario.estado = False
                usuario.fecha_baja = date.today()
                print(f"✅ Usuario -{usuario.user_name}- dado de baja correctamente.")
                return
        
        print("Usuario no encontrado...")
    
    def __str__(self):
        return (
            f"User Name: {self.user_name} | {self.nombre} {self.apellido}\n"
            f"Estado: {'Activo' if self.estado else 'Baja'}\n"
            f"Email: {self.email}\n"
            f"Fecha Alta: {self.fecha_alta}\n"
            f"Fecha Baja: {self.fecha_baja if self.fecha_baja is not None else ''}"
        )