palabra = input("ingrese una frase\t")

letra= input("ingrese una letra\t")


n= palabra.lower().count(letra.lower())

print(f"la cantidad de {letra} es {n}, en la frase ingresada '{palabra}'")


