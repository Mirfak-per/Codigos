import csv

with open("nuevo archivo.csv",newline="") as archivo:
    datos = csv.reader(archivo,delimiter=";")
    lista = list(datos)

for i in range(len(lista)):
    print(lista[i][0],lista[i][1],lista[i][2],sep=",")

#guardar mayores de 19

archivo_csv = open("mayores_de_19.csv", "w", newline="")
escritor_csv = csv.writer(archivo_csv,delimiter=";")
escritor_csv.writerow(["Nombre","Edad","Comuna"])

for i in range(1,len(lista)):
    if len(lista[i])>1:
        if int(lista[i][1])>= 19:
            escritor_csv.writerow(lista[i])