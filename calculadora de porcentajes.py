#Escribe un programa que solicite al usuario un número y le reste el 15%,almacenando todo en una única variable. A continuación, mostrar el resultadofinal en pantalla

num1 = float(input("ingrese un numero\n"))

#el 0.85 es lo mismo que poner ((num1 * 15)/100 -num1) *(-1), es mas rapido 
#tambien se puede hacer lo otro, solo quita el "#"


#tambien se puede guardar el resultado ej:
#porcentaje = (num1 * 15)/100
#print ("quitandole el 15%, al numero ingresado da: ", num1-porcentaje)

print ("quitandole el 15%, al numero ingresado da: ", num1 * 0.85)