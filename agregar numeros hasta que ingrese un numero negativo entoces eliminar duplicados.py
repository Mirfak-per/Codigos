# Crear un programa que añada números a una lista hasta que introducimos un número negativo. 
# A continuación, debe crear una nueva lista igual que la anterior pero 
# eliminando los números duplicados. 
# Muestra esta segunda lista para comprobar que 
# hemos eliminados los duplicados
import os
import time
os.system("cls")
x=list()
cont =0
numeros1= list()
numeros2= list()
#numeros1 = list ("2142568713264281761786248761278345612746446343673453574456345769846456353468")

while True:
    while True:
        try:
            numero = int(input("ingrese un numero,hasta que ingrese un numero negativo, no decimales"))
            break
        except:
            print("ingreso un numero decimal o una letra")

    if numero<0:
        break
    else:
        numeros1.append(numero)

numeros1.sort()
numeros2 = numeros1

print (numeros1,"\n eliminando numeros iguales....")
time.sleep (2)

for i in range(1,len(numeros1)):
    if (numeros1[i]) == (numeros1[cont]):
        x.append(numeros1[cont])
    cont+= +1

for i in x:
    numeros2.remove(i)
  
print(numeros2)