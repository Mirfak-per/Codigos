# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus
#clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
#Ingredientes vegetarianos: Pimiento y tofu.

#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana
#o no, y en función de su respuesta le muestre un menú con los ingredientes
#disponibles para que elija.

# Solo se puede eligir un ingrediente además de la
#mozzarella y el tomate que están en todas la pizzas.

# Al final se debe mostrar
#por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes
#que lleva.

pizza = input("si su pizza es vegetariana ingrese (Y), si no ingrese (N) \n")

if pizza.upper() == "Y":
    pizzaveg1 = input("quiere pimiento en su pizza?, para si ingrese (Y), si no ingrese (N)\n")
    pizzaveg2 = input("quiere tofu en su pizza? (Y), si no ingrese (N)\n")
elif pizza.upper() == "N":
    pizzanoveg1 = input ("quiere Peperoni en su pizza? (Y), si no ingrese (N)\n")
    pizzanoveg2 = input ("quiere Jamón en su pizza? (Y), si no ingrese (N)\n")
    pizzanoveg3 = input ("quiere Salmón en su pizza? (Y), si no ingrese (N)\n")
else:
    print("no ingreso una opcion de pizza valida")

if pizza.upper() == "Y":
    print("el tipo de pizza ingresado es vegetariana")
    if pizzaveg1.upper() == "Y":
        print("su pizza tiene pimiento")
    elif pizzaveg1.upper() == "N":
        print("su pizza no tiene pimiento")

    if pizzaveg2.upper() == "Y":
      print ("su pizza tiene tofu")
    elif pizzaveg2.upper() == "N":
       print("su pizza no tiene tofu")

if pizza.upper() == "N":
    print("el tipo de pizza ingresado no es vegetariana")
    if pizzanoveg1.upper() == "Y":
        print("su pizza tiene peperoni")
    elif pizzanoveg1.upper() == "N":
        print("su pizza no tiene peperoni")

    if pizzanoveg2.upper() == "Y":
      print ("su pizza tiene jamon")
    elif pizzanoveg2.upper() == "N":
       print("su pizza no tiene jamon")

    if pizzanoveg3.upper() == "Y":
      print ("su pizza tiene Salmón")
    elif pizzanoveg3.upper() == "N":
       print("su pizza no tiene Salmón") 

print("-" *250)
print("si una pocion no le aparece, ej: su pizza no tiene salmon, ingreso mal la opcion")