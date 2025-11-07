
class TipoDocumento: #Representa un tipo de documento (DNI, Pasaporte, etc)
    def __init__(self, tipo_documento: str):
        self.__tipo_documento = tipo_documento
    
    @property
    def tipo_documento(self) -> str:
        return self.__tipo_documento

    def __str__(self) -> str:    # Método de instancia
        return f"Tipo: {self.tipo_documento}"