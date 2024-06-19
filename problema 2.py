# Escribir una función que reciba una por parámetro una lista de números y devuelva su promedio

def listaprom(listnum):
    cont = 0
    cont2 = 0
    while True:
        num = input("Agregando numeros a una lista hasta que ingrese 'Salir' ")
        if num.capitalize() != "Salir":

            if num.isnumeric():
                listnum.append(float(num))
                cont += +1
                print("numero ingresado correctamente!")
            else:
                print("no ingreso un numero")

        else:
            for i in (listnum):
                cont2 += +i
            print(f"elpromedio de {listnum} es \n {cont2 / cont}")
            exit("saliendo")


test = []

listaprom(test)

