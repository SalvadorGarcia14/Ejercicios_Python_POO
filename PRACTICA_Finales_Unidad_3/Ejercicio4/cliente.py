

class Cliente():
    def __init__(self, nombre: str, apellido: str, nro_documento: str, nro_comunidad: int = None):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__nro_documento = nro_documento
        self.__nro_comunidad = nro_comunidad
    
    
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre) -> str:
        self.__nombre= nuevo_nombre
    
    @property
    def apellido(self) -> str:
        return self.__apellido
    @apellido.setter
    def apellido(self, nuevo_apellido) -> str:
        self.__apellido = nuevo_apellido
        
    @property
    def nro_documento(self) -> str:
        return self.__nro_documento
    @nro_documento.setter
    def nro_documento(self, nuevo_nro_documento) -> str:
        self.__nro_documento = nuevo_nro_documento

    @property
    def nro_comunidad(self) -> int:
        return self.__nro_comunidad
    @nro_comunidad.setter
    def nro_comunidad(self, nuevo_nro_comunidad) -> int:
        self.__nro_comunidad = nuevo_nro_comunidad
    
    
    def __str__(self):
        return (
            f"Nombre y Apellido: {self.nombre} {self.apellido} - DNI: {self.nro_documento} | Comunidad [{self.nro_comunidad if self.nro_comunidad is not None else "No tiene Comunidad"}]\n"
        )