from datos import estadias, precio
from datetime import datetime, date, time

from estadia import Estadia


def registrar_ingreso():
    print("Registrar Ingreso \n")
    patente = input("Ingresar Patente: ").upper()
    hora = input("Hora entrada (HH:MM): ")

    hora_entrada = time.fromisoformat(hora)

    # Verificar si la patente ya existe en estadias EN CURSO
    patente_existene = any(e.nro_patente == patente and e.estado == "EN_CURSO" for e in estadias)

    if patente_existene:
        print("Error: la patente ya está registrada en el sistema.")
    else:
        fecha = date.today()

        # ✅ llamada corregida
        nueva_estadia = Estadia(fecha, patente, "EN_CURSO", hora_entrada, pagado=False)

        estadias.append(nueva_estadia)
        print("Ingreso registrado correctamente.\n")


def registrar_salida():
    print(" Registrar Salida \n")
    patente = input("Ingrese patente: ").upper()
    
    estadia = None
    for estadia_existe in estadias:
        if estadia_existe.nro_patente == patente and estadia_existe.estado == "EN_CURSO":
            estadia = estadia_existe
            break
    
    if not estadia:
        print(" No se encontró una estadía EN CURSO para esa patente.")
        return
    
    hora = input("Hora salida (HH:MM): ")
    hora_salida = time.fromisoformat(hora)
    
    importe = estadia.registrar_salida(hora_salida, precio)
    print(f" Salida registrada — Total a pagar: ${importe}")


def listar_estadias():
    print(" Lista de estadías \n")
    for estadia in estadias:
        print("----------------------")
        print(estadia)
    
def main():
    while True:
        print("=== ESTACIONAMIENTO === \n")
        print("1 — Registrar ingreso")
        print("2 — Registrar salida")
        print("3 — Listar estadías")
        print("4 — Salir")

        opcion = input("Opción: ")
        
        if opcion == "1":
            registrar_ingreso()
        elif opcion == "2":
            registrar_salida()
        elif opcion == "3":
            listar_estadias()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opcion invalida...")

if __name__ == "__main__":
    main()
