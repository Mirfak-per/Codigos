nomb = input("ingrese su nombre\t")
edad = input("ingrese su edad\t")
cont = 0

print(f"bienvenido {nomb}")

while cont != 1:
    if edad.isnumeric() == True:
        print("edad ingresada correctamente")
        break
    else:
        print("ingreso la edad de forma incorrecta")
        edad = input("igresela nuevamente\t")