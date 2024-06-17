import csv
archivo_csv = open("nuevo archivo.csv","w",newline="")
escritor_csv = csv.writer(archivo_csv,delimiter=";")
escritor_csv.writerow(["Nombre","Edad","Comuna"])

while True:
    nombre = input("Ingrese su nombre: ")
    if nombre.capitalize()== "Salir":
        break
    else:
        edad  =input("Ingrese su edad: ")
        comuna = input("Ingrese su comuna: ")
        lista = []
        lista.append(nombre.capitalize())
        lista.append(edad.capitalize())
        lista.append(comuna.capitalize())
        escritor_csv.writerow(lista)

archivo_csv.close()        