Edad = int(input("ingresa tu edad "))
nombre = input ("ingresa tu nombre ")

if (Edad >= 18):
    print (nombre + ", eres mayor de edad")
elif (Edad >=14):
    print (nombre +", eres adolecente (menor o igual a 14)")
else:
    print (nombre +", eres menor de edad")