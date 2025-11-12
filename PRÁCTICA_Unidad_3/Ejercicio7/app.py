from datetime import datetime, time
from datos import pacientes, turnos, especialidad1, especialidad2, especialidades
from turno import Turno


def buscar_paciente(dni):
    for paciente in pacientes:
        if paciente.nro_documento == dni:
            return paciente

    return None


def menu_mostrar_especialidades():
    print(" ESPECIALIDADES \n")
    for especialidad in especialidades:
        print(especialidad)



def reservar_turno():
    dni = input("Ingrese DNI del paciente: ")
    paciente = buscar_paciente(dni)

    if not paciente:
        print("❌ Paciente no encontrado.")
        return

    menu_mostrar_especialidades()
    codigo = int(input("Ingrese el codigo de la Especialidad: "))
    especialidad = None
    for especilidad_existente in especialidades:
        if especilidad_existente.codigo == codigo:
            especialidad = especilidad_existente
            break
    
    if not especialidad:
        print("Código inválido.")
        return

    print(" Médicos disponibles ")
    for medico in especialidad.medicos:
        print(medico)
        
    matricula = input("Ingrese matrícula del médico: ")
    medico = None
    for medico_existente in especialidad.medicos:
        if medico_existente.matricula == matricula:
            medico = medico_existente
            break

    if not medico:
        print("Matrícula inválida.")
        return

    fecha = datetime.strptime(input("Ingrese fecha (dd/mm/yyyy): "), "%d/%m/%Y").date()
    hora = datetime.strptime(input("Ingrese hora (HH:MM): "), "%H:%M").time()

    for turno in turnos:
        if turno.fecha == fecha and turno.hora == hora and turno.medico == medico:
            print("❌ Ya existe un turno reservado para esa fecha/hora.")
            return

    estado = "Reservado"
    autorizado = True
    
    turno = Turno(fecha, hora, estado, autorizado, medico, paciente)
    turnos.append(turno)

    print("Turno reservado correctamente. \n")


def cancelar_turno():
    dni = input("Ingrese DNI del paciente: ")
    paciente = buscar_paciente(dni)

    if not paciente:
        print("❌ Paciente no encontrado.")
        return
    
    futuros = []
    for turno in turnos:
        if turno.paciente == paciente and turno.estado == "Reservado":
            futuros.append(turno)
        
    if not futuros:
        print("No tiene turnos futuros.")
        return
    
    print("Turnos futuros")
    for i, turno_elegir in enumerate(futuros, start=1):
        print(f"[{i}] -> {turno_elegir}") 
    indice = int(input("Seleccione el turno: ")) - 1
    futuros[indice].cancelar_turno()

    print(" Turno cancelado.\n")



def ingresar_paciente():
    dni = input("Ingrese DNI del paciente: ")
    paciente = buscar_paciente(dni)

    if not paciente:
        print("❌ Paciente no encontrado.")
        return

    hoy = datetime.now().date()
    del_dia = []
    for t in turnos:
        if t.paciente == paciente and t.fecha == hoy:
            del_dia.append(t)

    if not del_dia:
        print("No tiene turnos para hoy.")
        return

    print("Turnos del día")
    for i, turno_elegir in enumerate(del_dia, start=1):
        print(f"[{i}] -> {turno_elegir}")
    indice = int(input("Seleccione el turno: ")) - 1
    token = int(input("Ingrese token de obra social: "))
    if del_dia[indice].ingresar_paciente(token):
        print("Paciente ingresado y autorizado.\n")
        

def ver_turnos():
    print(" LISTADO DE TURNOS ")
    turnos_ordenados = sorted(turnos, key=lambda x: (x.fecha, x.hora))
    
    for i, turno_elegido in enumerate(turnos_ordenados, start=1):
        print(f"Turno [{i}] \n")
        print(turno_elegido)
        
 

def menu():
    while True:
        print("\n====== SISTEMA DE TURNOS ======")
        print("1 - Reservar turno")
        print("2 - Cancelar turno")
        print("3 - Ingresar paciente")
        print("4 - Ver turnos")
        print("0 - Salir")

        op = input("Seleccione una opción: ")

        if op == "1":
            reservar_turno()
        elif op == "2":
            cancelar_turno()
        elif op == "3":
            ingresar_paciente()
        elif op == "4":
            ver_turnos()
        elif op == "0":
            break


if __name__ == "__main__":
    menu()