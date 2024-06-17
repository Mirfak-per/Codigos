lista  = []
valor= 0
while True:
    opc = input("quiere ingresar un valor? Y/N\n")
    
    if opc.upper() == "Y":
        while True:
            try:
                valor=int(input("ingrese un valor\t"))
                break
            except:
                print("error, intente nuevamente")

    elif opc.upper() == "N":
        break

    lista.append(valor)

print(lista)

nummax = lista[0]

nummin = lista[0]
for i in range(len(lista)):
    if lista[i] > nummax:
        nummax= lista[i]

    if lista[i] < nummin:
        nummin= lista[i]

print ("el numero mas grande ingresado en la lista es",nummax)
print ("el numero mas pequeño ingresado en la lista es",nummin)