import os
import time
#dict() y {} Crea un diccionario vacio o con valor si se agrega asi: dict(Key,Valor) entre paréntesis

# d2 = dict([
#       ('Nombre', 'Sara'),
#       ('Edad', 27),
#       ('Documento', 1003882),
#           ])

# d3 = dict(Nombre='Sara',
#           Edad=27,
#           Documento=1003882)

# print(d2)
# print(d3)
#ambas formas tendrian que imprimir lo siguiente....
#{'Nombre': 'Sara', 'Edad': 27, 'Documento': 1003882}

alumnos = dict()
while True:
    try:
        print("""
                Menu 
            1 AGREGAR
            2,BUSCAR
            3,ELIMINAR
            4,SALIR
    """)
        opc = int(input("ingrese una opcion\n"))

        if opc == 1:
            #guarda el rut y nombre ingresado
            rut =input("ingrese el rut del alumno\n")
            nombre = input("ingrese el nombre del alumno\n")

            #si el rut ya se encuetra en el diccionario da un error
            if rut in alumnos:
                print("el rut ya se encuetra dentro de la lista")
            #de otra manera continua agregando lo ingresado a el diccionario con el rut como key y el nombre como valor
            else:
                alumnos[rut]= nombre
                print(f"el alumno {nombre}, de rut {rut}, ha sido ingresado correctamente")

        elif opc == 2:
            buscar = input("ingrese el nombre del alumno\n")
            #busca si el nombre se encuentra en el diccionario, luego da el rut del alumno en una confirmacion
            for key in alumnos:
                if alumnos[key] == buscar:
                    print(f"el alumno {alumnos[key]}, su rut es {key}")

        elif opc == 3:
            opc2 = int(input("Quiere eliminar por nombre (1) o por rut (2)?\n"))
            if opc2 == 1:
                buscar = input("ingrese el nombre del alumno\n")
                #si el nombre se encuentra en el diccionaro, lo elimina y da una confirmacion
                for key in alumnos:
                    if alumnos[key] == buscar:
                        print(f"el alumno {alumnos[key]}, su rut es {key}, se ha eliminado")
                        del(alumnos[key])
                        break

            elif opc2==2:
                rut = input("ingrese el rut\n")
                #si el rut se encunetra en el diccionario, lo elimina y da una confrimacion
                if rut in alumnos:
                    print(f"el alumno {alumnos[rut]}, su rut es {rut}, se ha eliminado")
                    del(alumnos[rut])
                    
            else:
                print("error al ingresar una opcion")

        elif opc == 4:
            print("saliendo...")
            time.sleep(2)
            os.system("cls")
            break

        else:
            print("error al ingresar una opcion")
    except:
        print("error, regresando al menu")
    time.sleep(2)
    os.system("cls")
#imprime en orden los ruts y alumnos que se ingresen correctamente
for key in alumnos:
    print(f"{key}  {alumnos[key]}")