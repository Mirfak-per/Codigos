frase = input("ingrese una frase\t")

palindromo = ""


#este for transforma el "i" en un caracter de la frase "hola", luego la agrega asi h+"" -> o + "h"-> l + "oh"
for i in (frase):
    print(i)
    palindromo = i + palindromo

#print(palindromo)
    
if palindromo.replace(" ","") == frase.replace(" ",""):
    print(f"la frase ingresada {frase} se lee igual al revez y al derecho")
else:
    print(f"la frase ingresada {frase} no se lee igual al revez y al derecho")