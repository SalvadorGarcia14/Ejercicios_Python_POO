from datos import usuarios

from datetime import date
from usuario import Usuario

def menu():
    print("1 -> Iniciar Sesion")
    print("2 -> Registrar Usuario")
    print("3 -> Salir")


def sub_menu(usuario):
    while True:
        print(f"\nUsuario logueado: {usuario.nombre} {usuario.apellido}")
        print("1 -> Dar de baja este usuario")
        print("2 -> Ver estado")
        print("3 -> Salir")
    
        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            usuario.baja_usuario(usuarios)
            print(usuario)
        elif opcion == "2":
            print(usuario)
        elif opcion == "3":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opcion invalida...")


def registrar_usuario():
    print("Creando Nuevo Usuario...")
    
    nombre = input("Ingrese su Nombre: ")
    apellido = input("Ingrese su Apellido: ")
    fecha_nacimiento_str = input("Ingrese su fecha nacimiento: ")
    fecha_nacimiento = date.strftime(fecha_nacimiento_str, "%d/%m/%Y")
    
    nro_documento = input("Ingrese su DNI: ")
    
    for dni in usuarios:
        if dni.nro_documento == nro_documento:
            print("El dni ya esta registrado...")
            return
    
    user_name = input("Ingrese su User Name: ")
    
    for username in usuarios:
        if username.user_name == user_name:
            print("El User Name ya esta registrado... Ingrese otro")
            return
    
    email = input("Ingrese su Email: ")
    password = input("Ingrese su Contraseña: ")

    
    nuevo_usuario = Usuario(
        nombre= nombre,
        apellido= apellido,
        fecha_nacimiento= fecha_nacimiento,
        nro_documento= nro_documento,
        
        user_name= user_name,
        password= password,
        estado= True,
        email= email,
        fecha_alta= date.today(),
        fecha_baja= None
    )
    
    usuarios.append(nuevo_usuario)
    print(f"Usuario - {nombre} {apellido} | {user_name} | DNI: {nro_documento} - registrado con éxito.\n")


def buscar_usuario(user_name, password):
    for usuario in usuarios:
        if usuario.validar_credenciales(user_name, password):
            return usuario
    return None


def main():
    while True:
        menu()
    
        opcion = input("Ingrese una opcion: ")
        
        if opcion == "1":
            print("Ingrese las credenciales...\n")
            user_name = input("User Name: ")
            password = input("Contraseña: ")

            usuario = buscar_usuario(user_name, password)

            if usuario and usuario.estado == True:
                sub_menu(usuario)
            else:
                print("Usuario no encontrado o está dado de baja.")
                
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opcion incorrecta...")

if __name__ == "__main__":
    main()
    