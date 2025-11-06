from persona import Persona
from datetime import date


class Usuario(Persona):
    def __init__(self, nombre, apellido, fecha_nacimiento, nro_documento, 
                user_name: str, password: str, estado: bool, email: str, fecha_alta: date, fecha_baja: date):
        super().__init__(nombre, apellido, fecha_nacimiento, nro_documento)

        self.__user_name = user_name
        self.__password = password
        self.__estado = estado
        self.__email = email
        self.__fecha_alta = fecha_alta
        self.__fecha_baja = fecha_baja

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
    def fecha_alta(self) -> date:
        return self.__fecha_alta

    @property
    def fecha_baja(self) -> date:
        return self.__fecha_baja
    @fecha_baja.setter
    def fecha_baja(self, nuevo_fecha_baja) -> date:
        self.__fecha_baja = nuevo_fecha_baja

    def validar_credenciales(self, username: str, contra: str) -> bool:
        print("Validando...")
        if username == self.user_name and contra == self.password:
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
                print(f"Usuario -{usuario.user_name}- dado de baja correctamente.")
                return

        print("Usuario no encontrado...")
    
    def __str__(self):
        return (
            
            f"{super().__str__()}\n"
            
            f"{'*' * 20}\n"
            
            f"User Name: {self.user_name} | {self.nombre} {self.apellido}\n"
            f"Estado: {'Activo' if self.estado else 'Baja'}\n"
            f"Email: {self.email}\n"
            f"Fecha Alta: {self.fecha_alta}\n"
            f"Fecha Baja: {self.fecha_baja if self.fecha_baja is not None else ''} \n"
            f"{'*' * 20} \n"
        )

