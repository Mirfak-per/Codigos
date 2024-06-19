# Definir una función inversa() que calcule la inversión de una cadena. 
# Por ejemplo, la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"


def inversa(texto):
    palindromo = ""
    for i in texto:
     palindromo = i + palindromo
    return palindromo

palabra = input("Ingrese una palabra: ")

palabreinvera = (inversa(palabra))

print(palabra,"inversa es", palabreinvera)