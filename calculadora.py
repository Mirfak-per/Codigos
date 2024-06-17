def suma(a,b):
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    resultado = a + b
    print(f"el valor de la suma es de {resultado}")

def resta(a,b):
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    resultado = a - b
   

def division(a,b):
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    division = a / b
    return(division)

def multiplicacion(a,b):
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    multiplicacion = a * b
    return(multiplicacion)

def limpiar():
    import os
    os.system("cls")

def esperar2():
    import time
    time.sleep(2)

def Menu():
    print("""
        Menu
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. Salir
        """)

while True:
    limpiar()
    Menu()
    opc = int(input("Ingresa una opcion: "))
    if opc == 1:
        print("Opcion 1, Suma")
        suma()

    elif opc == 2:
        print("Opcion 2, Resta")
        resta()

    elif opc == 3:
        print("Opcion 3, Multiplicacion")
        multiplicacion()

    elif opc == 4:
        print("Opcion 4, Division")
        division()

    elif opc == 5:
        print("saliendo...")
        esperar2()
        limpiar()
        break
    esperar2()    
