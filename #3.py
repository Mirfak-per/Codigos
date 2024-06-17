# Escribir un programa que cree un diccionario de traducción
# español-inglés. El usuario introducirá las palabras en español e
# inglés. El programa debe crear un diccionario con las palabras y
# sus traducciones.
# Después pedirá una frase en español y utilizará el diccionario para
# traducirla palabra a palabra. Si una palabra no está en el
# diccionario debe dejarla sin traducir.

dicct={}
dicct2 = {}
while True:
    try:
        i = 0
        print("""
            menu    
        1- ingresar traduccion español ingles al diccionario
        2- traducir frase a ingles
        3- traducir frase a español
        4- salir
        """)
        opc = int(input("ingrese una opcion (1-4)\n"))

        if opc == 1:
            español = input("ingrese una palabra en español\n")
            ingles = input("ingrese la tradducion de la palabra que ingreso anteriormente\n")
            if español not in dicct.keys():
                dicct[español] = ingles
                print(f"la palabra {español} y su traduccion {ingles}, se agregaron con exito")
            else:
                print("la tradducion ya se encuentra en el sistema, quiere actualizar el significado?")
                n = int(input("si = 1 , no = 2\n"))
                if n == 1:
                    dicct[español] = ingles
                    dicct2[ingles] = español
                    print(f"la palabra {español} y su traduccion {ingles}, se agregaron con exito")
                if n == 2:
                    print("regresando al menu....")
                else:
                    print ("valor ingresado incorrecto.... regresando al menu")

        if opc == 2:
            frase = input("ingrese una frase para traducir a ingles\n")
            x = frase.split()
            y = []
            for i in range (len(x)):
                if x[i] in dicct.keys():
                    y.append(dicct[x[i]])
                else:
                    y.append(x[i]) 
                i += +1
            print(y)
        if opc == 3:
            frase = input("ingrese una frase para traducir a español\n")
            x = frase.split()
            y = []
            for i in range (len(x)):
                if x[i] in dicct2.keys():
                    y.append(dicct2[x[i]])
                else:
                    y.append(x[i]) 
                i += +1
            print(y)
        if opc == 4:
            print("saliendo...")
            break
    except:
        pass