from datetime import date
from datos import usuarios, libros, listas_lecturas

from usuario import Usuario
from libro import Libro
from lista_lectura import ListaLectura

def mostrar_libros_disponibles():
    print(" LIBROS DISPONIBLES \n")
    for i, libro in enumerate(libros, start=1):
        print(f"[{i}] {libro} ")

def login():
    print(" LOGIN  \n")
    email = input("Email: ")
    password = input("Contraseña: ")

    for usuario in usuarios:
        if usuario.validar_credenciales(email, password):
            return usuario

    print(" Usuario o contraseña incorrectos")
    return None


def nueva_lista_lectura(usuario):
    nombre_lista = input("Ingrese el nombre de la Nueva Lista: ")
    nueva_lista = ListaLectura(nombre_lista, date.today())
    usuario.add_lista(nueva_lista)
    print("Nueva Lista Creada")

def borrar_lista(usuario):
    if not usuario.listas_lecturas:
        print("No hay listas cargadas")
        return
    
    print(" LISTAS DE LECTURA \n")
    for i, lista in enumerate(usuario.listas_lecturas, start=1):
        print(f"[{i}] {lista}")

    indice = int(input("Seleccione la lista a eliminar: ")) - 1

    if indice < 0 or indice >= len(usuario.listas_lecturas):
        print("Índice inválido")
        return

    lista_seleccionada = usuario.listas_lecturas[indice]
    usuario.remove_lista(lista_seleccionada)

    print("Lista eliminada")
    
    
def agregar_libro(usuario):
    nombre_lista = input("Nombre de la lista: ")
    
    lista = None

    for lista_encontrada in usuario.listas_lecturas:
        if lista_encontrada.nombre == nombre_lista:
            lista = lista_encontrada
            break
    
    if not lista:
        print(" Lista no encontrada")
        return
    
    mostrar_libros_disponibles()
    indice = int(input("Selecione la lista a eliminar: ")) - 1
    libro_seleccionado = libros[indice]
    
    lista.add_libro(libro_seleccionado)
    print(f" '{libro_seleccionado.nombre}' agregado a la lista '{lista.nombre}'")
    
def eliminar_libro(usuario):
    nombre_lista = input("Nombre de la lista: ")
    
    lista = None
    for lista_encontrada in usuario.listas_lecturas:
        if lista_encontrada.nombre == nombre_lista:
            lista = lista_encontrada
            break
    
    if not lista:
        print(" Lista no encontrada")
        return

    if not lista.libros:
        print(" La lista está vacía")
        return

    print(" LIBROS EN LA LISTA ")
    for i, libro in enumerate(lista.libros, start=1):  # ✅ corregido
        print(f" [{i}] {libro}")
    
    isbn = input("Ingrese el ISBN del libro a eliminar: ")

    libro = None

    for libro_existente in lista.libros:  # ✅ búsqueda en la lista correcta
        if libro_existente.isbn == isbn:
            libro = libro_existente
            break
    
    if not libro:
        print("Libro no encontrado en esta lista")
        return

    lista.remove_libro(libro)
    print("Libro eliminado")

def menu(usuario):
    while True:
        print(f"\n===== MENÚ - Usuario: {usuario.user_name} =====")
        print("1 - Nueva Lista de Lectura")
        print("2 - Borrar Lista de Lectura")
        print("3 - Agregar libro a mi lista")
        print("4 - Eliminar libro de mi lista")
        print("5 - Cerrar Sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nueva_lista_lectura(usuario)
        elif opcion == "2":
            borrar_lista(usuario)
        elif opcion == "3":
            agregar_libro(usuario)
        elif opcion == "4":
            eliminar_libro(usuario)
        elif opcion == "5":
            print(" Sesión cerrada\n")
            break
        else:
            print(" Opción inválida")



def main():
    while True:
        usuario = login()
        if usuario:
            menu(usuario)


if __name__ == "__main__":
    main()