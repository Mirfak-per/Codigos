import os
os.system("cls")
x = 0
while True:
    try:
        x= int(input("ingrese con cuantas personas viene"))
        break
    except:
        print("error, ingrese un valor numerico")

joven=0
adulto=0
adultomayor=0
total = 0
edad= 0

for i in range(x):
    while True:
        try:
            edad = int(input("ingrese una edad"))
            break
        except:
            print("error, ingrese un valor numerico")

    if edad > 7 and edad < 12:
        print(f"se agregaron 4000 a su total, el integrante numero {i+1} de {x}")
        joven= joven + 1
    elif edad >= 12  and edad <65:
        print(f"se agregaron 7000 a su total, el integrante numero {i+1} de {x}")
        adulto= adulto + 1
    elif edad >= 65:
        print(f"se agregaron 3000 a su total, el integrante numero {i+1} de {x}")      
        adultomayor= adultomayor + 1
    else:
        print("pasa gratis")      

total = total +(joven*4000) + (adulto*7000) + (adultomayor*3000)
print(f"""\tENCOMIENDAS
------------------------------------------------------
{joven} niño:\t${joven*4000}
{adulto} adulto:\t${adulto*7000}
{adultomayor} adulto mayor:\t${adultomayor*3000}
------------------------------------------------------
\tTotal de lo que tiene que pagar:\t\t${total}
""")