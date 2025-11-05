from datos import usuarios_registrados
from usuario import Usuario

from datetime import date

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
            usuario.baja_usuario(usuarios_registrados)
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
    
    user_name = input("Ingrese un User Name unico: ")
    
    for usuario in usuarios_registrados:
        if usuario.user_name == user_name:
            print("El User Name ya existe, intente otro")
            return
    
    email = input("Ingrese el Email: ")
    password = input("Ingrese la Contraseña: ")
    nombre = input("Ingrese el Nombre: ")
    apellido = input("Ingrese el Apellido: ")
    
    nuevo_usuario = Usuario(
        user_name = user_name,
        estado= True,
        email= email,
        password= password,
        nombre= nombre,
        apellido= apellido,
        fecha_alta=date.today(),
        fecha_baja= None 
    )    

    usuarios_registrados.append(nuevo_usuario)
    print(f"Usuario -{user_name}- registrado con éxito.\n")
    
    
    
def buscar_usuario(user_name, password):
    for usuario in usuarios_registrados:
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
    