# Desarrolle una aplicación en Python utilizando Visual Studio que permita resolver el siguiente caso:
# Una empresa necesita desarrollar una aplicación que permita registrar los sueldos brutos de los trabajadores y calcular el líquido
# a pagar. Para ello necesita que la aplicación cumpla con las siguientes funcionalidades
# 1. Registrar trabajador
# 2. Listar los todos los trabajadores
# 3. Imprimir planilla de sueldos
# 4. Salir del Programa
from funciones import *
lista = []

while True:
    opc = menu()

    if opc ==1:
        lista = registrar_trabajador()
    elif opc ==2:
        tabla_de_trabajadores(lista)
    elif opc ==3:
        imprimir_sueldos(lista)
    elif opc ==4:
        print("saliendo...")
        break
    else:
        print("error, regresando al menu")