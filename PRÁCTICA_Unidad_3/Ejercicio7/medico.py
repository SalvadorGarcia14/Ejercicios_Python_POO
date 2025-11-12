from datetime import date

class Medico():
    
    _matriculas_registradas = set()  # para validar que sean únicas

    def __init__(self, nombre_apellido: str, matricula: str, fecha_matricula: date):
        if matricula in Medico._matriculas_registradas:
            raise ValueError(f"Ya existe un médico con la matrícula {matricula}")
        
        self.__nombre_apellido = nombre_apellido
        self.__matricula = matricula
        self.__fecha_matricula = fecha_matricula



    @property
    def nombre_apellido(self) -> str:
        return self.__nombre_apellido
    @nombre_apellido.setter
    def nombre_apellido(self, nuevo_nombre_apellido) -> str:
        self.__nombre_apellido = nuevo_nombre_apellido


    @property
    def matricula(self) -> str:
        return self.__matricula


    @property
    def fecha_matricula(self) -> date:
        return self.__fecha_matricula
    @fecha_matricula.setter
    def fecha_matricula(self, nuevo_fecha_matricula) -> date:
        self.__fecha_matricula = nuevo_fecha_matricula
        
    
    def __str__(self):
        return (
            f"Medico: {self.nombre_apellido} \n"
            f"Matricula: {self.matricula} | Fecha: {self.fecha_matricula} \n"
        )