#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error
num1= float(input("ingrese el primer numero de la divison\n"))

num2= float(input("ingrese el segundo numero de la divison\n"))
#despues de ingresar dos numeros el programa verifica que no sea 0, si lo es muestra un mensaje de error, sino, continua con la division
if num2 == 0: 
    print("error en el programa, no se puede dividir en 0")
else:
    print("la division de ambos numeros es: ", num1/num2)
