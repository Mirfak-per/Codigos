#Escribe un programa que solicite al usuario el ingreso de una temperatura enescala Fahrenheit
# (debe permitir decimales) y le muestre el equivalente engrados Celsius
opcion = int(input("eliga una opcion\n1.fharenthit\n2.celsius\n"))

#menu de opciones dependiendo de "opcion"
if opcion == 1:
    #ingresa una temp
    fah = float(input("ingrese una temperatura en fharenhit\n"))
    #hace los calculos para cambiar la temperatura
    nuevatem = (fah - 32) * 5/9
     #da la nueva temperatura transforamda
    print ("la temperatura tansformada a celsius es. ",nuevatem)

elif opcion ==2:
    #ingresa una temp
    cel = float(input("ingrese una temperatura en celcius\n"))
     #hace los calculos para cambiar la temperatura
    nuevatem2= (cel * 9/5) + 32
     #da la nueva temperatura transforamda
    print("la temperatura tansformada faharenheit es. ",nuevatem2)

#si la opcion ingresada no es valida (ej: opcion es 5)    
else:
    print ("error, no ingreso una opcion valida, intente otra vez")