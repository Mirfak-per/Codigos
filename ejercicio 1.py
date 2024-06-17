# Escriba un algoritmo que permita almacenar una determinada cantidad de palabras en una lista. Las
# palabras serán ingresadas por el usuario. Luego, debe mostrar por pantalla cuál es la palabra más larga que
# se ingresó (es decir, la que tiene mayor cantidad de caracteres)
palabras = []
cont= 0
while True:
    palabra = input("ingrese una palabra, si quiere salir ingrese un numero\n")

    if palabra.isnumeric()== False:
        palabras.append(palabra)
    else:
        print("saliendo...")
        break

for i in range(1,len(palabras)):
    if len(palabras[i]) > len(palabras[cont]):
        maxpal = palabras[i]
    cont+= +1
    
print(f"la palabra mas grande es {maxpal}")
