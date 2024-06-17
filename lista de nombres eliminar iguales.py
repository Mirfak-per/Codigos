nombres1 = list()
nombres2 = list()

while True:
    print("añada un nombre a la lista 1, si quiere salir ingrese 0")
    nombre = input()
    
    if nombre.isnumeric() ==True:
        break 
    else:
        nombres1.append(nombre)


while True:
    print("añada un nombre a la lista 2, si quiere salir ingrese 0")
    nombre = input()

    if nombre.isnumeric() ==True:
        break
    else:
        nombres2.append(nombre)


print("elminando nombres iguales....")

for i in (nombres2):
    if i in nombres1:
        nombres1.remove(i)

print("nombres eliminados",nombres2)
print(nombres1)
