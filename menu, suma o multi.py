print ("menu ")
print ("opcion 1, suma")
print ("opcion 2, multiplicacion")
opcion= int(input("ingrese la opcion \n"))


if (opcion == 1):
    print ("ingreso la primera opcion, suma")

    n1= int(input("escriba el primer numero \n"))

    n2= int(input("escriba el segundo numero \n"))

    print (" la suma de los numeros es", n1+n2)

elif (opcion == 2):
    print ("eligio la opcion 2, multiplicacion")

    n1= int(input("escriba el primer numero \n"))

    n2= int(input("escriba el segundo numero \n"))
 
    print (" la multiplicacion de los numeros es", n1*n2)
    
else:
    opcion= int(input ("la opcion ingresada es incorrecta, intente otra vez \n"))