
import os
import math
opc = 0
opcv= 0


while True:
    print("1. Calcular area")
    print("2. Calcular perimetro")
    print("3. Salir")
    while True:
        try:
            opc = int(input("Ingrese la opcion deseada (1-3)"))
            if opc in [1,2,3]:
                break
        except:
            print("ingrese un valor que se encuentre en el (1-3)")

    if opc == 1:
        while True:
            if opc == 1:
                print("Calulando el area")
                print("1. Cuadrado")
                print("2. Rectangulo")
                print("3. Circulo")
                print("4. Volver al menu pricipal")
                while True:
                    try:
                        opcv = int(input("Ingrese la opcion deseada (1-4)"))
                        if opcv  in [1,2,3,4]:
                            break
                    except:
                        print("Intente otra vez, ingrese un valor numerico que se encuentre en (1-4)")

                if opcv ==1:
                    print ("calculando el area de el cuadrado")
                    while True:
                        try:
                            ladoc =int(input("ingrese el lado del Cuadrado\n"))
                            break
                        except:
                            print("error, ingreso un valor no numerico")
                    os.system("cls")
                    print(f"El area del Cuadrado es:{ladoc * ladoc}")

                elif opcv ==2:
                    print ("calculando el area de el Rectangulo")
                    while True:
                        try:
                            print("ingrese el largo")
                            lado =int(input("ingrese el lado del Rectangulo"))
                            print("ingrese el ancho")
                            ancho= int(input())
                            break
                        except:
                            print("error, ingreso un valor no numerico")
                    os.system("cls")
                    print(f"El area del Rectangulo es:{lado * ancho}")

                elif opcv ==3:
                    print ("calculando el area de el Circulo")
                    while True:
                        try:
                            print("Ingrese el Radio del Circulo")
                            Radio =int(input("ingrese el lado del Cuadrado"))
                            break
                        except:
                            print("error, ingreso un valor no numerico")
                    os.system("cls")
                    print(f"el area del circulo es: {math.pi * (Radio**2) }")
                elif opcv ==4:
                    print("Regresando al menu principal")
                    break

    elif  opc == 2:
        while True:
            if opc == 2:
                print("Calulando el perimetro")
                print("1. Cuadrado")
                print("2. Rectangulo")
                print("3. Circulo")
                print("4. Volver al menu pricipal")
                while True:
                    try:
                        opcv = int(input("Ingrese la opcion deseada (1-4)"))
                        if opcv  in [1,2,3,4]:
                            break
                    except:
                        print("Intente otra vez, ingrese un valor numerico que se encuentre en (1-4)")

                if opcv ==1:
                    print ("calculando el perimetro de el cuadrado")
                    while True:
                        try:
                            ladoc =int(input("ingrese el lado del Cuadrado\n"))
                            break
                        except:
                            print("error, ingreso un valor no numerico")
                    os.system("cls")
                    print(f"El perimetro del Cuadrado es:{ladoc * 4}")

                elif opcv ==2:
                    print ("calculando el perimetro de el Rectangulo")
                    while True:
                        try:
                            print("ingrese el largo")
                            lado =int(input("ingrese el lado del Rectangulo"))
                            print("ingrese el ancho")
                            ancho= int(input())
                            break
                        except:
                            print("error, ingreso un valor no numerico")
                    os.system("cls")
                    print(f"El perimetro del Rectangulo es:{(lado + ancho) *2}")


                elif opcv ==3:
                    print ("calculando el perimetro de el Circulo")
                    while True:
                        try:
                            Radio =int(input("ingrese el Radio del Circulo"))
                            break
                        except:
                            print("error, ingreso un valor no numerico")
                    os.system("cls")
                print(f"el perimetro del circulo es: {2* (math.pi * Radio) }")

            elif opcv == 4:
                print("Regresando al menu principal")
                break

    if opc == 3:
        print("saliendo del programa")
        break