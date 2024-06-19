# Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje
# indicando si la dirección es válida o no, valiéndose de una función para decidirlo.
# Una dirección se considerará válida si contiene el símbolo "@".

def verifcorr():
    while True:
        nombre = input("Ingrese su correo con @")
        if "@" in nombre:
            print("Correo ingresado correctamente!")
            break
        else:
            print("Correo ingresado sin @, intente otra vez \n")

verifcorr()