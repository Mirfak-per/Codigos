#  Realizar un programa que permita guardar los nombres y la edades de los alumnos de 
#  un curso.
#  Realiza un programa que introduzca el nombre y la edad de cada alumno.
#  El proceso de lectura de datos terminará cuando se introduzca como nombre un 
#  asterisco (*) Al finalizar se mostrará los siguientes datos:
# • Todos los alumnos mayores de edad.
# • Los alumnos mayores (los que tienen más edad)
import time
import os
os.system("cls")
alumnos = list()
edades = list()
alumnosmayores= list()
while True:

    alumno = input("ingrese el nombre de el alumno, si quiere salir del programa ingrese *")

    if alumno != "*":
        alumnos.append(alumno)

        while True:
            try:
                edad=int(input("ingrese una edad para el alumno"))
                break
            except:
                print("ingrese un numero entero para la edad")

        edades.append(edad)
        print(f"nombre '{alumno}' y edad '{edad}', ingresados con exito")
    else:
        print("terminando.... mostrando datos")
        time.sleep(2)
        os.system("cls")
        break

print("Todos los alumnos mayores de edad....")
time.sleep(2)
for i in range (len(edades)):
    if edades[i] >= 18:
        print(f"alumno {alumno[i]}, es mayor de edad")

