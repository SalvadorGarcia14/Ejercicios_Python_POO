from datos import clientes_logins, productos, compras_realizadas
from compra import Compra

from datetime import datetime

def menu():
    print(""" 
    1 -> Nueva Compra
    2 -> Resumen de Compras
    3 -> Salir
    """)

def mostrar_productos():
    for i, produto in enumerate(productos, start=1):
        print(f"{i} | {produto}")
    

def nueva_compra():
    fecha_hora = datetime.today()
    compra_cliente = Compra(fecha_hora, clientes_logins[0], False, 0, clientes_logins[0].nro_documento)

    while True:
        print(""" 
        1 -> Agregar Producto    
        2 -> Finalizar Compra
        """)
        
        op = input("Ingrese la opcion seleccionada: ")
        
        if op == "1":
            mostrar_productos()
            indice_producto = int(input("Ingreese el Producto: ")) - 1
            if 0 <= indice_producto <= len(productos):
                producto_seleccionado = productos[indice_producto]
                compra_cliente.add_producto(producto_seleccionado)
                print("Producto Agregado \n")
        elif op == "2":
            compra_cliente.finalizar_compra()
            compras_realizadas.append(compra_cliente)
            print("Gracias por su compra, los datos de su factura son: ")
            print(compra_cliente)
            break
        else:
            print("Opcion Invalida...")



def resumen_compras():
    for i, compra in enumerate(sorted(compras_realizadas, key=lambda x: x.fecha_hora), start=1):
        print(f"{i} - {compra}")


def main():
    while True:
        menu()
        opcion = input("Ingrese la opcion seleccionada: ")
        
        if opcion == "1":
            nueva_compra()
        elif opcion == "2":
            resumen_compras()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion Invalida...")


if __name__ == "__main__":
    main()