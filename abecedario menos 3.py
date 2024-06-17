"""Escribir un programa que almacene el abecedario en una lista, elimine de la lista las
letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante"""

nuevoabc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(nuevoabc,"\n")
letra = []

for i in range (len(nuevoabc)):

    if i == 0: 
        i = 1

    if i % 3 == 0:
        letra.append(nuevoabc[i])

for i in letra:
    nuevoabc.remove(i)

print(nuevoabc)