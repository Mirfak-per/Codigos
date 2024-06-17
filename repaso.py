archivo = open("ejemplo.txt")
lineas =  archivo.readlines()

for linea in lineas:
    print(linea,end="")

archivo.close()