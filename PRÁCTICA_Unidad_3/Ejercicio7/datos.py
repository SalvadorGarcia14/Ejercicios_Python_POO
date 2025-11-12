from datetime import date

from paciente import Paciente
from medico import Medico
from especialidad import Especialidad
from turno import Turno


#Pacientes
pacientes = [
    Paciente("Anna Zak", "Pasaporte", "12345678", "OSDE"),
    Paciente("Sylvanas Windrunner", "DNI", "87654321", "IAPOS")
]

#Medicos
medico1 = Medico("Friedman Milton", "XVL123", date(2010, 5, 14))
medico2 = Medico("Smith Adam", "ABC987", date(2015, 2, 20))
medico3 = Medico("Hayek Friedrich", "QWE456", date(2017, 7, 10))


#Especialidades
especialidad1 = Especialidad("Cardiología", 101)
especialidad2 = Especialidad("Pediatría", 102)

especialidad1.add_medico(medico1)
especialidad1.add_medico(medico2)
especialidad2.add_medico(medico3)

especialidades = [especialidad1, especialidad2]

#Turnos
turnos = []
