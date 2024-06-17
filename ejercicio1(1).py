"""genere un convertidor de :
-dolares a pesos chilenos
-soles a pesos chilenos
-pesos argentinos a pesos chilenos
"""

#variables
dolar = 957.59
soles = 258.24
parge = 1.10

#presentacion sistemas 
print(f"""
\033[32mSISTEMA CONVERTIDOR A PESOS CHILENOS🤑
---------------------------------------------\033[0M
1) DOLAR ${dolar} CLP
2) SOLES ${soles} CLP
3) PESOS ARGENTINOS ${parge}CLP""")
opcion = int (input("SELECCIONE :"))

#VALIDAR OPCION 
if opcion in (1,2,3):
    cantidad = int(input("ingrese cantidad a transformar :"))
    #validar cantidad
    if cantidad>0:
        if opcion== 1:
            print(f"{cantidad} de dolar equivalen a {(cantidad*dolar)} CLP\033[0m")
        elif opcion== 2:
            print(f"{cantidad} de soles equivalen a {(cantidad*soles)} CLP \033[0m")
        elif opcion== 3:
            print(f"{cantidad} de pesos argentinos equivalen a {(cantidad*parge)} CLP \033[0m")  
    else:
        print("\033 [31mCANTIDAD NO VALIDA\033[0m")
else:
        print("\033 [31m OPCION NO VALIDA \033[0m")    

