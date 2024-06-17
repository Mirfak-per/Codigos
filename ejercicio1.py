#ejercicio 1:
#limpiar pantalla:
import os
os.system('cls')

print("COMPRA DE PASAJES")
cantidad_pasajes = 0
while cantidad_pasajes<=0:
    try:
        cantidad_pasajes = int(input("Ingrese cantidad de pasajes: "))
    except:
        print("ERROR! debe ingresar un valor numérico!")

acumulador = 0
for x in range(cantidad_pasajes):
    precio = 0
    while precio<=0:
        try:
            precio = int(input(f"Ingrese precio pasaje {x+1}: "))
        except:
            print("ERROR! debes ingresar un número entero")
    acumulador += precio
os.system('cls')
print("Su total a pagar es:\n\t",acumulador)