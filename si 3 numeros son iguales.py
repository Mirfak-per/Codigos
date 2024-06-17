num1 = int(input("ingrese el primer numero\n"))
num2 = int(input("ingrese el segundo numero\n"))
num3 = int(input("ingrese el tercer numero\n"))

#lee si los 3 son iguales
if num1 == num2 == num3:
    print("todos los numeros son iguales")
#si los dos son iguales
elif num1 == num2 or num2 == num3 or num1 == num3:
    print ("ingreso 2 numeros iguales")
#ninguno es igual
else:
    print("no ingreso numeros iguales")