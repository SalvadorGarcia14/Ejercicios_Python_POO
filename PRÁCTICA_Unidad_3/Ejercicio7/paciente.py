


class Paciente():
    
    _nro_documento_registrados = set()
    
    def __init__(self, nombre_apellido: str, tipo_documento: str, nro_documento: str, obra_social: str):
        
        if not Paciente.validar_documento_unico(nro_documento):
            raise ValueError(f"El numero de Documento '{nro_documento}' ya esta registrado...")

        self.__nombre_apellido = nombre_apellido
        self.__tipo_documento = tipo_documento
        self.__nro_documento = nro_documento
        Paciente._nro_documento_registrados.add(nro_documento)
        self.__obra_social = obra_social
    
    
    
    @property
    def nombre_apellido(self) -> str:
        return self.__nombre_apellido
    @nombre_apellido.setter
    def nombre_apellido(self, nuevo_nombre_apellido) -> str:
        self.__nombre_apellido = nuevo_nombre_apellido


    @property
    def tipo_documento(self) -> str:
        return self.__tipo_documento
    @tipo_documento.setter
    def tipo_documento(self, nuevo_tipo_documento) -> str:
        self.__tipo_documento = nuevo_tipo_documento
    

    @property
    def nro_documento(self) -> str:
        return self.__nro_documento


    @property
    def obra_social(self) -> str:
        return self.__obra_social
    @obra_social.setter
    def obra_social(self, nuevo_obra_social) -> str:
        self.__obra_social = nuevo_obra_social
        
    
    @classmethod
    def validar_documento_unico(cls, nro_documento):
        if nro_documento not in cls._nro_documento_registrados:
            return True
        return False
    
    
    def __str__(self):
        return (
            f"{self.nombre_apellido} | {self.tipo_documento} : {self.nro_documento} \n"
            f"Obra Social: [{self.obra_social}] \n"
        )
        
    
