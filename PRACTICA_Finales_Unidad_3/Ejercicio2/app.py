from datos import listas_reproduccion, videos, usuarios, tags
from typing import List

from tag import Tag
from usuario import Usuario
from video import Video
from lista_reproduccion import ListaReproduccion


def mostrar_menu():
    print(""" 
        1 -> Home
        2 -> Nueva Lista
        3 -> Ver Listas
        4 -> Salir
    """)

def recorrer_listas():
    for i, lista in enumerate(listas_reproduccion, start=1):
        print(f"{i} - {lista}")

def recorrer_video():
    for i, video in enumerate(videos, start=1):
        print(f"{i} - {video}")

def recorrer_usuario():
    for i, usuario in enumerate(usuarios, start=1):
        print(f"{i} - {usuario}")

def recorrer_tag():
    for i, tag in enumerate(tags, start=1):
        print(f"{i} - {tag}")


def mostrar_home():
    print(" --- HOME --- \n")
    recorrer_video()

def creear_listas():
    print("Creando una lista de reproducción \n")
    nombre = input("Ingrese el nombre de la lista: ")
    print("Seleccione al menos un video para crear la lista...")
    recorrer_video()
    indice_video = int(input("Seleccione el video: ")) - 1
    
    if 0 <= indice_video < len(videos):
        video = videos[indice_video]
        print(f"Titulo seleccionada: {video.nombre}")
    else:
        print("Ingrese una opción en el rango de las opciones")

    lista = ListaReproduccion(nombre)
    lista.add_video(video)
    listas_reproduccion.append(lista)
    print("Se creó la lista exitosamente \n")

def ver_listas():
    print("--- LISTAS DE REPRODUCCIÓN --- \n")
    for lista_reproduc in listas_reproduccion:
        if lista_reproduc.cantidad_videos > 0:
            print(lista_reproduc)

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese la opcion seleccionada: ")
    
        if opcion == "1":
            mostrar_home()
        elif opcion == "2":
            creear_listas()
        elif opcion == "3":
            ver_listas()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opcion Invalida...")
    


if __name__ == "__main__":
    main()