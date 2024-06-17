# 1.- Escribe un programa que lea una cadena y devuelva un
# diccionario con la cantidad de apariciones de cada palabra en la
# cadena. Por ejemplo, si recibe “Qué lindo día que hace hoy” debe
# devolver: {“que”: 2, “lindo”: 1, “día”: 1, “hace”: 1, “hoy”: 1}

txt = input("ingrese una frase\t")
lista= {}
x = txt.lower().split()


cont = 0

for i in range (len(x)):
    #si la palabra se repite agrega 1 
    if x[i] in lista:
        lista[x[i]] = lista[x[i]] +1
    #de otra manera es 1 fijo
    else:
        lista[x[i]] = 1

print ("las palabras ingresadas se encuentran:",lista)