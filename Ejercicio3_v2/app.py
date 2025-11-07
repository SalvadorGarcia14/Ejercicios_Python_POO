from datetime import datetime
from usuario import Usuario

from datos import tipos_documento, libros, usuarios


def login():
    print("\n=== LOGIN ===")

    username = input("Ingrese usuario: ")
    password = input("Ingrese contraseña: ")

    for usuario in usuarios:
        if usuario.validar_credenciales(username, password):
            return usuario

    print("Usuario o contraseña incorrecta.")
    return None


def nuevo_usuario():
    print(" ALTA USUARIO \n")
  
    username = input("Ingrese su username: ")
    
    email = input("Ingrese email: ")
    password = input("Ingrese contraseña: ")
    apellido = input("Apellido: ")
    nombre = input("Nombre: ")
    
    # fecha con validación
    fecha_str = input("Fecha de nacimiento (dd/mm/yyyy): ")
    fecha_nacimiento = datetime.strptime(fecha_str, "%d/%m/%Y").date()
    
    for i, tipo_doc in enumerate(tipos_documento):
        print(f"{i + 1} - {tipo_doc}")
    eleccion = int(input("Opcion: ")) - 1
    tipo_documento = tipos_documento[eleccion]
    
    nro_documento = input("Numero de documento: ")

    administrador = input("¿Es administrador? (s/n): ").lower()

    if administrador == "s":
        administrador = True
        return administrador
    else:
        administrador = False
    
    estado = True
    fecha_alta = datetime.today()
    fecha_baja = None

    nuevo_usuario = Usuario(
        nombre,
        apellido,
        fecha_nacimiento,
        tipo_documento,
        nro_documento,
        username,
        estado,
        email,
        password,
        fecha_alta,
        fecha_baja,
        administrador
    )
    
    usuarios.append(nuevo_usuario)
    print("Usuario creado con éxito")


def buscar_usuario():
    username = input("Ingrese username a buscar: ")
    encontrado = None

    for usuario_username in usuarios:
        if usuario_username.user_name == username:
            encontrado = username
            break
    
    if encontrado:
        print(f"Usuario encontrado: {encontrado}")
    else:
        print("No existe ese usuario.")


def buscar_libro():
    usuarios_leyeron = []

    isbn = input("Ingrese ISBN: ")

    for usuario_libro in usuarios:
        if usuario_libro.leyo_libro(isbn):
            usuarios_leyeron.append(usuario_libro)
    
    
    if not usuarios_leyeron:
        print("No se encontró el libro o nadie lo leyó. \n")
        return

    print("Usuarios que leyeron los libros: \n")
    for usuarios_leyo_libros in usuarios_leyeron:
        print(f"-> {usuarios_leyo_libros}")
    


def agregar_libro(usuario):
    print("Seleccione libro: ")

    for i, libro in enumerate(libros):
        print(f"{i + 1} -> {libro}")
    opcion = int(input("Opcion: ")) -1
    usuario.add_libro(libros[opcion])
    print("Libro agregado.")

def eliminar_libro(usuario):
    if not usuario.libros:
        print("No tiene libros cargados.")
        return

    print("Seleccione libro para eliminar: \n")
    for i, libro in enumerate(usuario.libros):
        print(f"{i + 1} - {libro}")

    opcion = int(input("Opción: ")) - 1
    usuario.remove_libro(usuario.libros[opcion])
    print("Libro eliminado.")


def menu(usuario):
    while True:
        print("\n=== MENÚ PRINCIPAL ===")

        if usuario.administrador:   # <-- Si es admin mostramos este menú
            print("1 - Nuevo usuario")
            print("2 - Buscar usuario")
            print("3 - Buscar libro")
            print("4 - Ver libros de usuario")
            print("5 - Agregar libro a mi colección")
            print("6 - Eliminar libro de mi colección")
            print("7 - Cerrar sesión")

            opcion = input("Opción: ")

            if opcion == "1":
                nuevo_usuario()
            elif opcion == "2":
                buscar_usuario()
            elif opcion == "3":
                buscar_libro()
            elif opcion == "4":
                print("\nLibros del usuario:")
                for libro in usuario.libros:
                    print(f"-> {libro}")
            elif opcion == "5":
                agregar_libro(usuario)
            elif opcion == "6":
                eliminar_libro(usuario)
            elif opcion == "7":
                print("Sesión cerrada.")
                break
            else:
                print("Opción incorrecta.")

        else:   # <-- menú para usuarios comunes
            print("1 - Ver mis libros")
            print("2 - Buscar libro")
            print("3 - Agregar libro a mi colección")
            print("4 - Eliminar libro de mi colección")
            print("5 - Cerrar sesión")

            opcion = input("Opción: ")

            if opcion == "1":
                print("Tus libros: \n")
                if not usuario.libros:
                    print("No tenés libros en tu colección.")
                else:
                    for libro in usuario.libros:
                        print(f"-> {libro}")
            elif opcion == "2":
                buscar_libro()
            elif opcion == "3":
                agregar_libro(usuario)
            elif opcion == "4":
                eliminar_libro(usuario)
            elif opcion == "5":
                print("Sesión cerrada.")
                break
            else:
                print("Opción incorrecta.")


def main():
    while True:
        usuario = login()
        if usuario:
            menu(usuario)

if __name__ == "__main__":
    main()

