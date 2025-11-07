from datetime import date
from usuario import Usuario
from libro import Libro
from tipodocumento import TipoDocumento


tipos_documento = [
    TipoDocumento("DNI"),
    TipoDocumento("Pasaporte"),
    TipoDocumento("Libreta Cívica")
]

usurios = [
    Usuario("Anna", "Zak", date(2001, 3, 12), "12345678", tipos_documento[0], 
        "AnnaZak", True, "anna123","annazak@gmail.com", date(2025, 11, 1), True, None),
    
    Usuario("Salvador", "Garcia", date(2000, 12, 21), "87654321", tipos_documento[0],
        "Salvi", True, "salvi123", "salvi@gmail.com", date(2025, 11, 5), False, None) 
]

#    Usuario("Anna", "Zak", date(2001, 3, 12), "12345678", "AnnaZak", "anna123", True, "annazak@gmail.com", date(2025, 11, 1), None),

libros = []

libros.append(Libro("El señor de los anillos", "Tolkien", date(1954, 1, 1)))
libros.append(Libro("Harry Potter", "Rowling", date(1997, 6, 26)))
libros.append(Libro("Clean Code", "Robert C. Martin", date(2008, 8, 1)))


usurios[0].add_libro(libros[0])