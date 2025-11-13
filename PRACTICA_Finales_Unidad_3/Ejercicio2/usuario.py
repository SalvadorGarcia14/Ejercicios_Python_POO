import random
import string


class Usuario():
    
    ids_generados_unicos = set()
    
    def __init__(self, nombre: str, email: str, password: str):
        self.__id = self.generar_id_unico()
        self.__nombre = nombre
        self.__email = email
        self.__password = password
 
    @property
    def id(self):
        return self.__id

    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> str:
        self.__nombre = nuevo_nombre

    @property
    def email(self) -> str:
        return self.__email
    @email.setter
    def email(self, nuevo_email: str) -> str:
        self.__email = nuevo_email


    @property
    def password(self) -> str:
        return self.__password
    @password.setter
    def password(self, nuevo_password: str) -> str:
        self.__password = nuevo_password
          
    
    @classmethod
    def generar_id_unico(cls) -> str:
        while True:
            nuevo_id = "".join(random.choices(string.digits, k=6))
            if nuevo_id not in cls.ids_generados_unicos:
                cls.ids_generados_unicos.add(nuevo_id)
                return nuevo_id
    
    def valiidar_credenciales(self, email: str, password: str) -> bool:
        print("Validando...")
        if self.email == email and self.password == password:
            print("Credenciales Validas")
            return True
        print("Credenciales Invalidas")
        return False

    def __str__(self):
        return (
            f"ID: {self.id} - Nombre: {self.nombre} | Emaiil: {self.email} \n"
        )

    