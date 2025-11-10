from datetime import date
from typing import List

from persona import Persona
from lista_lectura import ListaLectura


class Usuario(Persona):
    
    _user_names_existentes = set()
    
    def __init__(self, nombre, apellido, fecha_nacimiento, nro_documento,
            user_name: str, password: str, email: str, fecha_alta: date):
        
        super().__init__(nombre, apellido, fecha_nacimiento, nro_documento)
    

        if not Usuario.validar_user_name_unico(user_name):
            raise ValueError(f"El nombre de usuario '{user_name}' ya está tomado.")  
        
        self.__user_name = user_name
        Usuario._user_names_existentes.add(user_name) 
        
        self.__user_name = user_name
        self.__password = password
        self.__email = email
        self.__fecha_alta = fecha_alta
        self.__listas_lecturas: List[ListaLectura] = []
    
    
    @property
    def user_name(self) -> str:
        return self.__user_name
    
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
    def listas_lecturas(self) -> List[ListaLectura]:
        return self.__listas_lecturas


    @classmethod
    def validar_user_name_unico(cls, user_name: str) -> bool:
        #Retorna True si el user_name esta disponible
        if user_name not in cls._user_names_existentes:
            return True
        return False   

    def validar_credenciales(self, email: str, contra: str) -> bool:
        print("Validando...")
        if email == self.email and contra == self.password:
            print(f"Usuario Validado {self.user_name} [{True}]")
            return True
        print(f"Usuario no encontrado... [{False}]")
        return False
    
    def leyo_libro(self, isbn: str) -> bool:
        for lista in self.listas_lecturas:
            for libro in lista.libros:
                if libro.isbn == isbn:
                    return True
        return False
    
    def add_lista(self, lista: ListaLectura) -> None:
        self.listas_lecturas.append(lista)
    
    def remove_lista(self, lista: ListaLectura):
        if lista in self.listas_lecturas:
            self.listas_lecturas.remove(lista)
    
    def __str__(self):
        return (
            f"{self.nombre} {self.apellido} | UserName {self.user_name} | Email: {self.email} \n"
            f"DNI: {self.nro_documento} \n"
            f"Fecha Nacimiento: {self.fecha_nacimiento} | Edad: {self.edad} \n"
            f"Fecha Alta: {self.fecha_alta}\n"            
            f"{"-" * 20} \n"
        )