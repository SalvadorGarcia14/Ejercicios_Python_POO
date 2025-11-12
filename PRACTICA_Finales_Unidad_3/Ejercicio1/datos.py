from carrera import Carrera
from titulo import Titulo
from inscripcion import Inscripcion
from aspirante import Aspirante

from datetime import date
from typing import List



#Titulos
titulos = [
    Titulo("Ingeniero en Sistema", "UTN"),
    Titulo("Contador Publico", "UNR"),
    Titulo("Lincenciado en Matematicas", "UNR"),
]


#Carrera pos-grado
carreras = [
    Carrera("Maestria en Sistemas Avanzados", date(2024,5, 12)),
    Carrera("Doctorado en Matematicas", date(2025, 3, 23)),
]

carreras[0].add_titulo_requerido(titulos[0])
carreras[1].add_titulo_requerido(titulos[2])

inspirante_false = Aspirante("Arthas", "Menetill", "arthas@gmail.com", "1234")

inscripciones = [
    Inscripcion(date(2025, 3, 5), False, inspirante_false, carreras[0])
]


for carrera in carreras:
    print(carrera)


for inscripcion in inscripciones:
    print(inscripcion)