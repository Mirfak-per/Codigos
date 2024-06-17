productos = {}
import os
import time

while True:
    try:
        os.system("cls")
        print("""
                    menu 
            1 - ingresar un producto
            2 - vender un producto
            3 - salir del sistema
        """)
        opc = int(input("ingrese una opcion (1-2)\n"))

        if opc == 1:
            producto = input("ingrese en nombre del producto \n").capitalize()

            if producto not in productos.keys():
                precio = int(input("ingrese el precio del producto"))
                productos[producto] = precio
                print(f"el producto '{producto}', con el precio de '{precio}', ha sido agregado con exito")

            else:
                print("el producto ya se encuentra en el sistema, quiere actualizar el precio?")
                n = int(input("si = 1 , no = 2"))
                if n == 1:
                    precio = int(input("ingrese el precio del producto"))
                    productos[producto] = precio
                    print(f"el producto '{producto}', con el precio de '{precio}', ha sido actualizado con exito")
                if n == 2:
                    print("regresando al menu....")
                else:
                    print ("valor ingresado incorrecto.... regresando al menu")

        if opc == 2:
            producto = input("ingrese el nombre del producto que quiere vender").capitalize()
            if producto in productos.keys():
                n = int(input("ingrese la cantidad de productos que vende"))
                total =productos[producto] * n
                print(f"la cantidad de {producto} que vende es de {n}, un total de {total}")
            else:
                print("el producto que ingreso no se enceuntra en el sistema.... regresando al menu")
                
        if opc == 3:
            print("saliendo del sistema")
            break
        time.sleep(3)
    except ValueError:
        print("error al ingresar un numero, ingreso un flotante o caracter...regresando al menu")
        time.sleep(3)
    except:
        print("error desconocido, regresando al menu...")
        time.sleep(3)
