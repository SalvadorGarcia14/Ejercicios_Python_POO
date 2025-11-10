from usuario import Usuario
from libro import Libro
from lista_lectura import ListaLectura

from typing import List
from datetime import date

libros = [
    Libro("Novela de Sylvanas Windrunner", "World of Warcraft - Novelas", date(2022, 5,10)),
    Libro("Nier Automata, VOL 1", "PlatinumGames", date(2023, 10, 25)),
    Libro("Nier Automata, VOL 2", "PlatinumGames", date(2024, 11, 5)),
    Libro("Aloy - La Nora Marginada", "", date(2024, 6, 10)),
]


listas_lecturas = [
    ListaLectura("Novelas WoW", date(2025, 5, 20)),
    ListaLectura("Nier Automata", date(2025, 10, 1)),
    ListaLectura("Saga Horizon", date(2025, 1, 1)),
]

usuarios = [
    Usuario("Anna", "Zak", date(2001, 3, 12), "12345678", "AnnaZak", "anna123", "anna@gmail.com", date(2020, 5, 10)),
    Usuario("Sylvanas", "Windrunner", date(2000, 12, 21), "12345", "SylvanasWindrunner", "sylvanas123", "sylvanas@gmail.com", date(2025,2,2)),
]

for libro in libros:
    print(libro)
    
for lista in listas_lecturas:
    print(lista)

for usuario in usuarios:
    print(usuario)