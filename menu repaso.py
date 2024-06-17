#lista = list(("Diablo","Diosito","Angel"))
# .append agrega a la lista en la ultima posicion de la siguiente manera:
# lista.append(0,"dato") lista = ["Diablo","Diosito","Angel","dato"]

# .insert agrega donde quieras en la lista de la siguiente manera :
# lista.insert(0,"dato") lista = ["dato","Diablo","Diosito","Angel"]

#.reverse invierte la lista
#.sort ordena la lista
#.index entrega la posicion de algo en la lista
import time
import os
import msvcrt
lista_codigo = []
lista_nombre = []
lista_raza = []
while True:
    os.system ("cls")
    print("menu")
    print("1. agregar animal")
    print("2. ver lista de mascotas")
    print("3. modificar dato de mascota")
    print("4. eliminar mascota de la lista")
    print("5.salir")
    while True:
        try:
            opc = int(input("ingrese la opcion (1-5)"))
            if opc in [1,2,3,4,5]:
                break
            else:
                print("error")
        except:
            print("error, no ingreso un numero")
    if opc ==1:
        codigo = input("ingrese codigo")
        nombre = input("ingrese el nombre")
        raza = input("ingrese raza")

        lista_codigo.append(codigo)
        lista_nombre.append(nombre)
        lista_raza.append(raza)
        print("mascota agregada con exito")
    elif opc ==2:
        print("lista")
        for i in range (len(lista_raza)):
            print(f"Codigo: {lista_codigo[i]} - Nombre: {lista_nombre[i]} - Raza: {lista_raza[i]}")

    elif opc ==3:
        codigo = input("ingrese el codigo de la mascota para modificar")
        try:
            n= lista_codigo.index(codigo)
            nombre=input("ingrese nuevo nombre")
            raza = input("ingrese nueva raza")
            lista_nombre[i]= nombre
            lista_raza[i]  = raza
        except:
            print("codigo incorrecto")

    elif opc==4:
        codigo = input("ingrese un codigo a eliminar")
        if codigo in lista_codigo:
            n=lista_codigo.index(codigo)
            lista_codigo.pop(n)
            lista_raza.pop(n)
            lista_nombre.pop(n)
            print("mascota eliminada")
        else:
            print("error")
        """try:
                print("error, ingreso un codigo de mascota incorrecto")
                n=lista_codigo.index(codigo)
                lista_codigo.pop(n)
                lista_raza.pop(n)
                lista_nombre.pop(n)
                print("mascota eliminada")
           except:
                print("error, el codigo ingresado no exsiste")"""

    else:
        print("adios")
        break
    time.sleep(3)
    # time.sleep(3), pausa el coigo por un tiempo, tambien por decimales, necesita import time