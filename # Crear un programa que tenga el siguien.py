import os
listanum= []
os.system ("cls")
while True:
    x= []
    cont= 0
    print("MENU")
    print("1. Añadir numero a lista, al final")
    print("2. Añadir numero a la lista, elegir pocicion")
    print("3. Longitud de la lista")
    print("4. Eliminar el ultimo numero")
    print("5. Eliminar un numero elegido por el usuario")
    print("6. Contar numeros")
    print("7. Pocisiones de un numero")
    print("8. Mostrar numeros")
    print("9. Salir")
    while True:
        try:
            opc=int(input("Ingrese una opcion de 1-9"))
            break
        except:
            print("Error, ingrese un numero que se enceuntra en el menu")

    if opc == 1:
        os.system("cls")
        print("opcion 1, ingresar un numero a la ultima posicion")
        while True:
            try:
                numero=int(input("ingrese un numero para agregar al final"))
                listanum.append(numero)
                break
            except:
                print("ingrso un numero incorrecto, intente otra vez")

    elif opc ==2:
        os.system("cls")
        print("opcion 2, ingresar un numero en una posicion elegida por el usuario")
        while True:
            try:
                posicion= int(input("ingrese una posicion para agregar el numero"))
                if posicion != 0:
                    listanum.insert(posicion,numero)
                    break
                else:
                    print("el numero 0 no se puede ingresar....\n intente otra vez")
            except:
                print("ingreso un numero no entero, intente otra vez")

    elif opc ==3:
        os.system("cls")
        print(f"opcion 3, longitud de la lista....\n la cantidad de elementos en la lista es de {len(listanum)}")
        
    elif opc == 4:
        os.system("cls")
        n=len(listanum) -1
        print(f"opcion 4, eliminando el ultimo numero de la lista....\n el ultimo numero de la lista es {listanum[n]}....eliminado")
        listanum.pop(n)

    elif opc == 5:
        os.system("cls")
        print("opcion 5, elimiar un numero desde su posicion....")
        while True:
            try:
                posicion = int(input("ingrese la posicion del numero"))
                if posicion in listanum and posicion != 0:
                    listanum.pop(posicion)
                    break
                else:
                    print("posisicion no existe o es 0, saliendo al menu....")
                    break
            except:
                print("ocurrio un error, intente otra vez")

    elif opc == 6:
        os.system("cls")
        print("opcion 6, cuantas veces aparece el numero ingresado...")
        while True:
            try:
                numero=int(input("ingrese el numero que desea contar"))
                break
            except:
                print("numero erroneo")
        for i in range(len(listanum)):
            if numero in listanum:
                cont += +1
        print(f"el numero ingresado,{numero}, aparece {cont} veces en la lista.")

    elif opc == 7:
        os.system("cls")
        print("opcion 7, en que posiciones aparece el numero ingresado...")
        while True:
            try:
                numero=int(input("ingrese el numero que desea contar"))
                break
            except:
                print("numero erroneo")
        for i in range(1,len(listanum)):
            if listanum[i] in listanum and listanum[i] == numero:
                x.append(i)
        print(f"el numero, {numero} aparece en las posiciones {x}")

    elif opc == 8:
        os.system("cls")
        print("opcion 8, mostando lista de numeros....")
        for i in range(len(listanum)):
            print(listanum[i])

    elif opc == 9:
        os.system("cls")
        print("opcion 9, saliendo...")
        break

    else:
        print("error, ingrese valor correcto para el menu")