#Escribir una función que calcule el largo de una lista (sin usar la función LEN)

def nolen(lista):
    cont = 0
    for i in (lista):
        cont += +1
    return cont

lista = [23, 45, 56, 43, 65, 12, 34, 78, 90, 21, 67, 89, 54, 32, 76, 98, 10, 87, 43, 21, 65, 34, 56, 
         78, 90, 12, 43, 65, 87, 98, 21, 34, 56, 78, 90, 12, 43, 65, 87, 98, 21, 34, 56, 78, 90, 12, 43]

texto = "hola que tal"

print(nolen(lista))

print(len(lista))

print(nolen(texto))

print(len(texto))