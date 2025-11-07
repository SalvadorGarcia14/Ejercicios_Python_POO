
class TipoDocumento():
    def __init__(self, tipo_documento: str):
        self.__tipo_documento = tipo_documento
    
    @property
    def tipo_documento(self) -> str:
        return self.__tipo_documento
    
    def __str__(self):
        return (
            f"Tipo de Documento: {self.tipo_documento}"
        )
