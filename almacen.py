#Desarrolle un algoritmo para almacén de barrio que permita registrar una venta y los precios de losproductos asociados a ella.
#El algoritmo deberá pedir la cantidad y el precio unitario del producto, luegopreguntará si desea ingresar otro producto a la venta.
#Cuando ya haya ingresado todos los productos, mostrará el total a pagar y solicitará el monto con quecancela el cliente, luego muestra el monto del vuelto
opc = 0
suma = 0
cont3= 1

while opc != 2:
    print("""
             menu
      ingrese su opcgion
      1. opcion 1, aregar compra
      2. opcion 2, salir""")
    
    opc = int(input())
    if opc == 1:
        product=input("ingrese el producto")
        precio = int(input("ingrese el precio del producto\n"))
        cantprod = int(input(f"cuantos {product} lleva?\n"))
        suma = suma + (precio * cantprod)
        print(f"la el precio de {product} que lleva ({cantprod}) es de {suma}\n")

giro = int(input(f"ingrese con cuanto dinero paga, tiene que llegar a {suma}\n"))
extra = 0

while cont3 != 0:
    if giro > suma:
        print("se le dara un vuelto de", giro - suma)
        cont3 = 0

    elif giro < suma:
         
         extra = int(input(f"le falta dinero {(suma-giro)} ingrese lo que falta"))
         if extra >= (suma-giro):
             
             print("su boleta es de", extra -(suma - giro))
         else:
             print("aun le falta dinero, intente otra vez")  

    else:
        print("un segundo, se esta imprimendo su boleta")
        cont3 = 0