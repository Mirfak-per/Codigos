num1 = float(input("ingrese un año\n"))

#qualquier año divisible por 400 y que el resultado sea un numero entero
# (que no sobre) es bisiesto, el cuatro esta para permitir años no entros ej 2024
#si el %4, no esta el programa detecta a ese año como no bisiesto

if  num1 % 4 ==0:
    "tal vez año bisiesto"
    if num1 % 100 != 0:
        print("año bisiesto")
    elif num1 % 400 == 0:
        print("año bisiesto")
    else:
        print("año no bisiesto")
else:
 print("año no bisiesto")