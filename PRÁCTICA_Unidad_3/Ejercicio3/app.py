from datetime import datetime
from usuario import Usuario

from datos import tipos_documento, libros, usurios


def login():
    print("\n=== LOGIN ===")

    username = input("Ingrese usuario: ")
    password = input("Ingrese contraseña: ")

    for usuario in usurios:
        if usuario.validar_credenciales(username, password):
            return usuario

    print("Usuario o contraseña incorrecta.")
    return None


def crear_usuario():
    print("\n=== ALTA USUARIO ===")

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
        nro_documento,
        tipo_documento,
        username,                 # user_name
        estado,
        password,
        email,
        fecha_alta,         # fecha_alta
        administrador,            # administrador
        fecha_baja                      # fecha_baja
    )
    
    usurios.append(nuevo_usuario)
    print("Usuario creado con éxito")


def buscar_usuario():
    username = input("Ingrese username a buscar: ")
    encontrado = None
    
    for usuario in usurios:
        if usuario.user_name == username:
            encontrado = usuario
            break

    if encontrado:
        print(f"Usuario encontrado: {encontrado}")
    else:
        print("No existe ese usuario.")
            
def buscar_libro():
    usuarios_leyeron = []

    isbn = input("Ingrese ISBN: ")

    for usuario_libro in usurios:
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
        print("5 - Agregar libro a mi colección")
        print("6 - Eliminar libro de mi colección")
        print("7 - Cerrar sesión")

        if usuario.administrador:
            print("1 - Nuevo usuario")
            print("2 - Buscar usuario")
            print("4 - Ver libros de usuario")
            print("3 - Buscar libro")

        opcion = input("Opción: ")

        if opcion == "7":
            break

        if opcion == "5": agregar_libro(usuario)
        elif opcion == "6": eliminar_libro(usuario)
        elif usuario.administrador:
            if   opcion == "1": crear_usuario()
            elif opcion == "2": buscar_usuario()
            elif opcion == "3": buscar_libro()
            elif opcion == "4":
                buscar_usuario()
        else:
            print("Opción inválida.")


def main():
    while True:
        usuario = login()
        if usuario:
            menu(usuario)


if __name__ == "__main__":
    main()