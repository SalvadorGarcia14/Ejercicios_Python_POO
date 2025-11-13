from datos import generos, autores, libros, listas_lecturas

from lista_lectura import ListaLectura
from datetime import date



def menu():
    print(""" 
        --- MENU ---
        1 -> Pagina Principal
        2 -> Nueva Lista de Lectura
        3 -> Ver Listas de Lectura
        4 -> Salir
    """) 


def mostrar_generos():
    for i , genero in enumerate(generos, start=1):
        print(f"{i} - {genero}")

def mostrar_autores():
    for i, autor in enumerate(autores, start=1):
        print(f"{i} - {autor}")
        
def mostrar_liibros():
    for i, libro in enumerate(libros, start=1):
        print(f"{i} - {libro}")

def mostrar_listas_lecturas():
    for i, lista in enumerate(listas_lecturas, start=1):
        print(f"{i} - {lista}")


def pagina_principal():
    print("--- PAGINA PRINCIPAL ---")
    
    for libro in sorted(libros, key=lambda x: x.nombre):
        print(libro)


def nueva_lista_lectura():
    print("--- CREANDO LISTA LECTURA ---")
    
    nombre = input("Ingrese el nombre de la lista: ")
    
    libros_seleccionados = []

    mostrar_liibros()
    indice_libro = int(input("Seleccione el libro: ")) - 1
    if 0 <= indice_libro < len(libros):
        libro_seleccionado = libros[indice_libro]
        libros_seleccionados.append(libro_seleccionado)
        print(f"Seleccion: {libro_seleccionado.nombre} ")
        print("Seleccion Exitosa")
    else:
        print("Ingrese una opción válida")
        return
    
    while True:
        print("--- Quiere Seleccionar mas de un Libro ---")
        op = input(""" 
            1 -> Agregar otro libro
            2 -> Para salir
        """)

        if op == "1":
            mostrar_liibros()
            indice_libro = int(input("Seleccione el libro: ")) - 1
            if 0 <= indice_libro < len(libros):
                libro_seleccionado = libros[indice_libro]
                libros_seleccionados.append(libro_seleccionado)  # ← FALTABA ESTO
                print(f"Agregado: {libro_seleccionado.nombre}")
            else:
                print("Opción inválida")
        elif op == "2":
            print("Seleccion de Libros Completa")
            break
        else:
            print("Opcion invalida")
    
    nueva_lista = ListaLectura(nombre)

    for libro in libros_seleccionados:
        nueva_lista.add_libro(libro)

    listas_lecturas.append(nueva_lista)

    print("Se creó la lista exitosamente.\n")

def ver_listas_lecturas():
    for lista in sorted(listas_lecturas, key=lambda x: x.codigo):
        if lista.cantidad_libros > 0:
            print(lista)


def main():
    while True:
        menu()
        opcion = input("Ingrese la opcion seleccionada: ")
        
        if opcion == "1":
            pagina_principal()
        elif opcion == "2":
            nueva_lista_lectura()
        elif opcion == "3":
            ver_listas_lecturas()
        elif opcion == "2":
            print("Saliendo...")
            break
        else: 
            print("Opcion Invalida")
    


if __name__ == "__main__":
    main()