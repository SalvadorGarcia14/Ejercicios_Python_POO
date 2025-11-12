from datos import carreras, titulos, inscripciones

from aspirante import Aspirante
from inscripcion import Inscripcion

from datetime import date
from typing import List


def mostrar_menu():
    print("""
    1 -> Nueva Inscripcion
    2 -> Ver Carereras
    3 -> Ver Inscripciones
    4 -> Salir
    """)

def mostrar_carreras():
    for i, carrera in enumerate(carreras, start=1):
        print (f"{i} -> {carrera}")

def mostrar_títulos():
    for i, titulo in enumerate(titulos, start=1):
        print (f"{i} -> {titulo}")

def mostrar_aspirantes():
    for i, aspirante in enumerate(inscripciones, start=1):
        print (f"{i} -> {aspirante}")


def nueva_inscripcion():
    print("Seleccione la Carrera: \n")
    mostrar_carreras()
    indice_carreras = int(input("Seleccione la Opción: ")) - 1

    if 0 <= indice_carreras < len(carreras):
        carrera = carreras[indice_carreras]
        print(f"Carrera seleccionada: {carrera.nombre}")
    else:
        print("Ingrese una opción en el rango de las opciones")
    
    print("Ingrese los datos del Aspirante: \n")
    nombre = input("Ingrese el Nombre del Aspirante: ")
    apellido = input("Ingrese el Apellido del Aspirante: ")
    email = input("Ingrese el Email del Aspirante: ")
    num_telefono = input("Ingrese el Numero de Telefono del Aspirante: ")
    fecha_inscripcion = date.today()
    inscripcion_activa = True

    nuevo_aspirante = Aspirante(nombre, apellido, email, num_telefono)
    
    print("Indica el titulo de grado del Aspirante: \n")
    mostrar_títulos()
    indice_titulos = int(input("Seleccione la Opción: ")) - 1

    if 0 <= indice_titulos < len(titulos):
        titulo = titulos[indice_titulos]
        print(f"Titulo seleccionada: {titulo.nombre}")
    else:
        print("Ingrese una opción en el rango de las opciones")
    
    
    nueva_inscripcion = Inscripcion(fecha_inscripcion, inscripcion_activa, nuevo_aspirante, carrera)
    inscripciones.append(nueva_inscripcion)
    
    print("Se registró la inscripción exitosamente \n")
    print(nueva_inscripcion)


def ver_carreras():
    print("Carreras disponibles: \n")
    for carrera in sorted(carreras, key=lambda x: x.comiendozo):
        print(carrera)

def ver_inscripciones():
    print("Inscripciones activas: \n")
    for inscripcion in inscripciones:
        if inscripcion.inscripcion_activa:
            print(inscripcion)


def main():
    while True:
        print("---SISTEMAS DE INSCRIPCIONES---")
        mostrar_menu()
        op = input("Ingrese la opcion seleccionada: ")
    
        if op == "1":
            nueva_inscripcion()
        elif op == "2":
            ver_carreras()
        elif op == "3":
            ver_inscripciones()
        elif op == "4":
            print("Saliendo... \n")
            break
        else:
            print("Opcion invalida")


if __name__ == "__main__":
    main()