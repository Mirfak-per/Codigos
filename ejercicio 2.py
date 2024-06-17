# Escriba un algoritmo que permita transformar grados Celsius en Fahrenheit y viceversa. Para ello, debe
# crear un pequeño menú como el que se muestra a continuación:
# ======================
# Conversión de Temperaturas:
# ======================
# Seleccione la conversión que desea realizar:
# 1) Celsius a Fahrenheit
# 2) Fahrenheit a Celsius
# 3) Salir
# Una vez que el usuario haya seleccionado la opción deseada, deberá ingresar el número que desea
# transformar y mostrar su equivalente en la temperatura deseada. Finalmente, el sistema debe preguntar si
# desea calcular otro valor (dentro de la misma opción seleccionada anteriormente) o si desea volver al
# menú principal. No olvidar que siempre se debe validar que el usuario ingrese una opción correcta.
import os
import time
while True:
    opc2=1
    os.system("cls")
    print("""
            ======================
            Conversión de Temperaturas:
            ======================
    Seleccione la conversión que desea realizar:
            1) Celsius a Fahrenheit
            2) Fahrenheit a Celsius
            3) Salir
        """)
    while True:
        try:
            opc= int(input("ingrese una opcion(1-3)\n"))
            break
        except:
            print("error al ingresar un valor, intente otra vez")

    if opc == 1:
        while True:
            os.system("cls")
            
            print("opcion 1, cesius a fahernheit")
            while True:
                try:
                    valor = int(input("ingrese un valor para transformar de celsius a farenheit\n"))
                    break
                except:
                    print("error al ingresar el valor, intente otra vez")
            print(f"el valor ingresado {valor} °celsius, se ha trasformado a farenheit, el nuevo valor es de {(valor * 9/5) +32}")

            while True:
                try:
                    opc2= int(input("desea regresar al menu? si es asi, ingrese 0, si no ingrese 1\n"))
                    break
                except:
                    print("error, intente otra vez")

            if opc2 == 0:
                print("saliendo al menu...")
                break
        
    elif opc == 2:
        while True:
            os.system("cls")
            print("opcion 1, fahernheit a cesius ")
            while True:
                try:
                    valor = int(input("ingrese un valor para transformar de farenheit a celsius \n"))
                    break
                except:
                    print("error al ingresar el valor, intente otra vez")

            print(f"el valor ingresado {valor}°farenheit, se ha trasformado a celsius, el nuevo valor es de {(valor - 32) * 5/9}")

            while True:
                try:
                    opc2= int(input("desea regresar al menu? si es asi, ingrese 0, si no ingrese 1\n"))
                    break
                except:
                    print("error, intente otra vez")

            if opc2 == 0:
                print("saliendo al menu...")
                break
    elif opc== 3:
        os.system("cls")
        print("saliendo del programa....")
        break
    else:
        print("error, ingrese un valor que se encuentre en el menu")
    time.sleep(2)