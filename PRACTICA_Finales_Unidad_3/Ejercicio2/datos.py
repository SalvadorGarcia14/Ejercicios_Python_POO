from tag import Tag
from usuario import Usuario
from video import Video
from lista_reproduccion import ListaReproduccion

from datetime import date
from typing import List


tags = [
    Tag("WoW"),
    Tag("Vlog"),
    Tag("Games"),
]

usuarios = [
    Usuario("Sylvanas Windruner", "sylvanas@gmail.com", "sylvanas123"),
    Usuario("Anna Zak", "anna@gmail.com", "anna123"),
]


videos = [
    Video("Vlog en Abu Dhabi, Final F1", date(2025, 12, 9), usuarios[1]),
    Video("Make Up en Abu Dhabi", date(2025, 12, 10), usuarios[1]),
    Video("Recorriedo Entrañas (Viejo Lordaeron)", date(2025, 5, 3), usuarios[0]),
]

videos[0].add_tag(tags[1])
videos[1].add_tag(tags[1])
videos[2].add_tag(tags[0])
videos[2].add_tag(tags[2])




listas_reproduccion = [
    ListaReproduccion("Juego WoW"),
    ListaReproduccion("Viaje a Abu Dhabi F1"),
    ListaReproduccion("Sin Videos"),
]

listas_reproduccion[0].add_video(videos[2])
listas_reproduccion[1].add_video(videos[0])
listas_reproduccion[1].add_video(videos[1])


for usuario in usuarios:
    print(usuario)

for video in videos:
    print(video)

for tag in tags:
    print(tag)

for lista_reproduccion in listas_reproduccion:
    print(lista_reproduccion)