#ejercicio 2:
import os #limpiar pantalla
import time #congelar pantalla ciertos segundos
import msvcrt #congelar pantalla hasta presionar una tecla

os.system('cls')

print("STARKEN")
cantidad_bultos = int(input("Ingrese cantidad de vultos a enviar: "))

cont_livianos = 0
cont_normales = 0
cont_pesados  = 0
for i in range(cantidad_bultos):
    kilo = float(input(f"Ingrese peso del bulto {i+1}: "))
    if kilo>0 and kilo<=5:
        cont_livianos += 1
    elif kilo>5 and kilo<=10:
        cont_normales += 1
    else:
        cont_pesados += 1
total = cont_livianos*1000 + cont_normales*4500 + cont_pesados*8000
os.system('cls')
#FORMA 1 BOLETA:
print("\tENCOMIENDAS")
print("-"*50)
print(f"{cont_livianos} bulto LIVIANO:\t${cont_livianos*1000}")
print(f"{cont_normales} bulto NORMAL:\t${cont_normales*1000}")
print(f"{cont_pesados} bulto PESADO:\t${cont_pesados*1000}")
print("-"*50)
print(f"\tTotal:\t\t${total}")

#FORMA 2 BOLETA:
print(f"""\tENCOMIENDAS
------------------------------------------------------
{cont_livianos} bulto LIVIANO:\t${cont_livianos*1000}
{cont_normales} bulto NORMAL:\t${cont_normales*1000}
{cont_pesados} bulto PESADO:\t${cont_pesados*1000}
------------------------------------------------------
\tTotal:\t\t${total}
""")