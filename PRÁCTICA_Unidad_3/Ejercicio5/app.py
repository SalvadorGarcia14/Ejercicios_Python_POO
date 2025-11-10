from datos import paises, clientes
from cliente import Cliente

from datetime import date


def seleccionar(opciones): #Muestra opciones numeradas y devuelve el objeto elegido
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i} - {opcion}")
    indice = int(input("Ingrese una opcion: \n")) - 1
    return opciones[indice]



def registrar_cliente():
    print(" REGISTRAR CLIENTE  \n")

    nombre = input("Nombre y Apellido: ")
    print("Seleccione el Pais: ")
    pais = seleccionar(paises)
    
    print("Seleccione la Provincia: ")
    provincia = seleccionar(pais.provincias)
    
    print("Seelecciona la Localidad: ")
    localidad = seleccionar(provincia.localidades)
    
    direccion = input("Ingrese la Direccion: ")
    
    fecha_alta = date.today()
    
    nuevo_cliente = Cliente(nombre, direccion, localidad, fecha_alta)
    clientes.append(nuevo_cliente)
    print("Cliente registrado correctamente...")


def buscar_cliente():
    print(" BUSCAR CLIENTE \n")
    
    nro = int(input("Ingrese el numero del Cliente: "))
    
    cliente = None
    
    for cliente_existente in clientes:
        if cliente_existente.nro_cliente == nro:
            cliente = cliente_existente
            break

    if not cliente:
        print("No existe cliente con ese número... \n")
        return
    
    print("Cliente encontrado: \n")
    print(cliente)

    print("1 -> Eliminar cliente \n")
    print("2 -> Reactivar cliente \n")
    opcion = input("Seleccione opción: ")

    if opcion == "1":
        cliente.eliminar_cliente()
        print(" Cliente dado de baja. \n")
    elif opcion == "2":
        cliente.reactivar_cliente()
        print(" Cliente reactivado. \n")
    


def main():
    while True:
        print(" SISTEMA CLIENTES ")
        print("1 -> Registrar cliente")
        print("2 -> Buscar cliente")
        print("3 -> Salir")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            buscar_cliente()
        elif opcion == "3":
            print("Fin del programa... ")
            break
        else:
            print(" Opción incorrecta... ")


if __name__ == "__main__":
    main()