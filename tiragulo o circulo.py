#Escriba un programa que pregunte primero si se quiere calcular el área de un
#triángulo o la de un círculo. Si se contesta que se quiere calcular el área de
#un triángulo (escribiendo T o t), el programa tiene que pedir entonces la base
#y la altura y escribir el área. 

#Si se contesta que se quiere calcular el área de
#un círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y
#escribir el área.

#Se recuerda que el área de un triángulo es base por altura dividido por 2 y
#que el área de un círculo es Pi (aproximadamente 3,141592) por el radio al
#cuadrado.

#Nota: Utilice como valor de pi el valor 3.141592.

opc = input("ingrese que area quiere calcular, tiragulo (T), o circulo (C)")

if opc.upper() == "T":
    lado1t = float(input("ingrese la base del triangulo"))
    lado2t = float(input("ingrese el lado del triangulo"))
    print ("el area del triangulo ingresado es de:",(lado1t * lado2t)/2)
elif opc.upper() == "C":
    radioc = float(input("ingrese el radio del circulo"))
    pi = 3.141592
    print ("el area del circulo ingresado es de:",pi * (radioc**2))