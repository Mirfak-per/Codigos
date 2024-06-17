# Desarrollar un algoritmo que permita administrar el listado de alumnos de un curso (La administración se
# debe hacer en listas). El sistema de debe permitir gestionar el listado teniendo en cuenta las siguientes
# funcionalidades:
# ● Agregar alumno: Agregar un alumno a la lista. El sistema debe validar que el nombre del alumno no
# se encuentre registrado previamente en la lista (Para efectos prácticos, registrar sólo el nombre, sin
# apellidos)
# ● Listar alumnos: Debe mostrar la lista de alumnos ordenada de forma vertical.
# ● Eliminar alumno: El sistema de poder eliminar alumnos ya sea por nombre o posición en la lista.
# El sistema debe mostrar un menú como el siguiente:
# ============================
# ADMINISTRACIÓN DE ALUMNOS
# ============================
# Seleccione alguna opción:
# 1) Agregar nuevo alumno
# 2) Listar alumnos registrados
# 3) Eliminar alumno
# 4) Salir
# No olvidar que siempre se debe validar que el usuario ingrese una opción correcta.
import os
import time
alumnos = []

while True:
    os.system("cls")
    print("""
        ============================
        ADMINISTRACIÓN DE ALUMNOS
        ============================
        Seleccione alguna opción:
        1) Agregar nuevo alumno
        2) Listar alumnos registrados
        3) Eliminar alumno
        4) Salir
        """)
    while True:
        try:
            opc = int(input("ingrese un valor (1-4)"))
            break
        except:
            print("error, ingrese un valor valido")

    if opc ==1:
        print("opcion 1, agregar alumno")
        nombre  =input("ingrese el nombre del alumno")
        if nombre.capitalize() in alumnos:
            print("error, el nombre ya se encuentra en el listado")
        else:
            alumnos.append(nombre.capitalize())
            print(f"el nombre {nombre.capitalize()}, ha sid agregado con exito. ")
        time.sleep(2)

    elif opc == 2:
        print("opcion 2, listado de alumnos")
        for i in range (len(alumnos)):
            print(alumnos[i],"el numero del alumno es",i)
        print("espera 5 segundos y se te regresara al menu....")
        time.sleep(5)

    elif opc == 3:
        print("opcion 3, eliminar alumno")
        print("1, buscar por nombre \n 2, buscar por numero en la lista")
        while True:
            try:
                opc2= int(input("ingrese una opcion(1-2)"))
                break
            except:
                print("error al ingresar una opcion, intente otra vez")
        if opc2 ==1:
            print("buscando por nombre")
            buscar = input("ingrese el nombre del alumno\n")
            if buscar.capitalize() in alumnos:
                alumnos.remove(buscar.capitalize())
                print(f"alumno{buscar.capitalize()} eliminado con exito")
            else:
                print(f"el alumno{buscar.capitalize()} no se encuentra en la lista")
        elif opc2 ==2:
            print("buscando por numero en la lista")
            while True:
                try:
                    buscar= int(input("ingrese el numero del alumno en la lista"))
                    break
                except:
                    print("error, intente otra vez")
            if buscar <= len(alumnos):
                alumnos.pop(buscar)
                print("alumno eliminado con exito")
                
            else:
                print("el alumno no se encuentra en la lista")
        time.sleep(2)

    else:
        print("error, intente otra vez")