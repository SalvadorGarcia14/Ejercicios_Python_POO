from genero import Genero
from autor import Autor
from libro import Libro
from lista_lectura import ListaLectura

from datetime import date
from typing import List

generos = [
    Genero("Ficcion"),
    Genero("Novela"),
    Genero("Fantasia"),
    Genero("Manga"),
]

autores = [
    Autor("Anna", "Zak", date(2001, 3, 12)),
    Autor("Sylvanas", "Windrunner", date(1990, 5, 23)),
]

libros = [
    Libro("Sylvanas Windruner - La Novela", date(2022, 5, 21), generos[1], autores[1]),
    Libro("Guia de Guias Maestras", date(2025, 1, 1), generos[0]),
    Libro("F1 -  El nacimiento", date(2022, 10, 23), generos[2], autores[0]),
    Libro("Libro para agregar", date(2024,1,1), generos[3])
]

libros[0].add_genero(generos[1])
libros[0].add_genero(generos[2])

libros[1].add_genero(generos[0])

libros[2].add_genero(generos[0])
libros[2].add_genero(generos[2])

libros[3].add_genero(generos[3])


listas_lecturas = [
    ListaLectura("WoW"),
    ListaLectura("Variedad")
]

listas_lecturas[0].add_libro([libros[0]])
listas_lecturas[1].add_libro([libros[1]])
listas_lecturas[1].add_libro([libros[2]])

for genero in generos:
    print(genero)


for autor in autores:
    print(autor)


for libro in libros:
    print(libro)

for lista in listas_lecturas:
    print(lista)