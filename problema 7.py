# Escribir una función que reciba como parámetro un rut.
# La función debe validar si el rut es correcto o no

# Escribir un programa que permita realizar los siguientes cálculos de área y
# perímetro para las siguientes figuras: Circulo, Cuadrado, Rectángulo.
# El programa debe tener un menú principal en el cual se debe seleccionar el tipo
# de calculo que desea realizar y luego seleccionar el tipo de figura. 
# Se deben utilizar funciones.

def menutipo():
    limpiar()
    print("""
            Menu
        1. Circulo
        2. Cuadrado
        3. Rectangulo
        4. Salir
        """)
    opc = int(input("ingrese una opcion: "))
    return opc

def menucalc():
    limpiar()
    print("""
            Menu
        1. Area
        2. Perimetro
        3. Salir 
    """)
    opc = int(input("Ingresa una opcion"))
    return opc

def area():
    import math
    while True:
        limpiar()
        print("Calculando el area....")
        opc = menutipo()
        if opc == 1:
            radio = float(input("Ingrese el Radio del circulo: "))
            print(f"El area del ciculo es de {math.pi * (radio**2)}")
        elif opc == 2:
            lado = input("Ingrese el lado de el cuadrado: ")
            print(f"El area del cuadrado es {lado * lado}")
        elif opc == 3:
            Largo = input("Ingrese el Largo de el Rectangulo: ")
            Ancho = input("Ingrese el Ancho de el Rectangulo: ")
            print(f"El area de el Rectangulo es de: {Largo * Ancho}")
        elif opc == 4:
            print("Resgresando al menu...")
            esperar()
            break
        esperar()

def perimetro():
    import math
    while True:
        limpiar()
        print("Calculando el Perimetro....")
        opc = menutipo()
        if opc == 1:
            radio = float(input("Ingrese el Radio del circulo: "))
            print(f"El area del ciculo es de {(math.pi*2) * (radio)}")
        elif opc == 2:
            lado = input("Ingrese el lado de el cuadrado: ")
            print(f"El area del cuadrado es {lado * 4}")
        elif opc == 3:
            Largo = input("Ingrese el Largo de el Rectangulo: ")
            Ancho = input("Ingrese el Ancho de el Rectangulo: ")
            print(f"El Perimetro de el Rectangulo es de: {(Largo + Ancho)*2}")
        elif opc == 4:
            print("Resgresando al menu...")
            esperar()
            break
        esperar()

def limpiar():
    import os
    os.system("cls")

def esperar():
    import time
    time.sleep(2)

def calculofigura():
    limpiar()
    while True:
        opc = menucalc()
        if opc == 1:
            area()
        elif opc == 2:
            perimetro()
        elif opc == 3:
            print("Saliendo...")
            esperar()
            break

calculofigura()