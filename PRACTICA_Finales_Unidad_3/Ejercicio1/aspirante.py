

class Aspirante():
    def __init__(self, nombre: str, apellido: str, email: str, num_telefono: str):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__num_telefono = num_telefono
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> str:
        self.__nombre = nuevo_nombre


    @property
    def apellido(self) -> str:
        return self.__apellido
    @apellido.setter
    def apellido(self, nuevo_apellido: str) -> str:
        self.__apellido = nuevo_apellido


    @property
    def email(self) -> str:
        return self.__email
    @email.setter
    def email(self, nuevo_email: str):
        self.__email = nuevo_email


    @property
    def num_telefono(self) -> str:
        return self.__num_telefono
    @num_telefono.setter
    def num_telefono(self, nuevo_num_telefono: str) -> str:
        self.__num_telefono = nuevo_num_telefono
    
    
    def __str__(self):
        return (
            f"Nombre y Apellido: {self.nombre} {self.apellido} \n"
            f"Email: {self.email} | Num Telefono: {self.num_telefono} \n"
        )