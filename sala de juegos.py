#Escribir un programa para una empresa que tiene salas de juegos para todas
#las edades y quiere calcular de forma automática el precio que debe cobrar a
#sus clientes por entrar.
# El programa debe preguntar al usuario la edad del
#cliente y mostrar el precio de la entrada.
# Si el cliente es menor de 4 años
#puede entrar gratis, si tiene entre 4 y 18 años debe pagar $5.000 y si es mayor
#de 18 años, $10.000

edad = int(input("ingrese su edad \n"))

if edad<4:
    print("tiene menos de 4, puede entrar gratis")
elif edad>= 4 and edad<= 18:
    print(f"tiene {edad} para ingresar tiene que pagar 5000")
elif edad > 18:
    print("mayor que 18, para ingresar tiene que pagar 10000")