from datetime import date
from usuario import Usuario
from libro import Libro
from tipo_documento import TipoDocumento



tipos_documento = [
    TipoDocumento("DNI"),
    TipoDocumento("Pasaporte"),
    TipoDocumento("Libreta Cívica")
]

usuarios = [
    Usuario("Anna", "Zak", date(2001, 3, 12), tipos_documento[0], "12345678",
        "AnnaZak", True, "annazak@gmail.com", "anna123", date(2025, 11, 1), None, True),
    
    Usuario("Salvador", "Garcia", date(2000, 12, 21), tipos_documento[2], "87654321",
        "Salvi", True, "salvi@gmail.com", "salvi123", date(2025, 11, 5), None, False),

]

libros = [
    Libro("Novela de Sylvanas", "World of Warcraft", date(2022, 10, 5)),
    Libro("Star Wars: Darth Vader", "Disney Novelas", date(2025, 10, 20)),
    Libro("Nier Automata: 2B Historia", "2B", date(2025, 11, 15)),
]

for libro in libros:
    print(libro)