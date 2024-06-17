import csv

archivo_csv= open("nuevo_archivo.csv","w",newline="")
escritor_csv = csv.writer(archivo_csv)
escritor_csv.writerow(["Nombre","Edad","Comuna"])

while True:
    nombre = input("Ingrese su nombre")
    edad = input("Ingrese su edad")
    comuna  = input("Ingrese su comuna")
    opc = input("Ingrese la opcion 1 continuar, 2 salir")
    if opc == "2":
        escritor_csv.writerow([nombre,edad,comuna])
        break
    else:
        escritor_csv.writerow([nombre.capitalize(),edad.capitalize(),comuna.capitalize()])

# escritor_csv.writerows([
#     ["Esteban",25,"Santiago"],
#     ["Maria",30,"Valparaiso"],
#     ["Carlos",22,"Osorno"]
# ])
archivo_csv.close()