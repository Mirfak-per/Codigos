# Construir programa que permita identificar las empresas que han tenido ventas inferiores
# a $100.000.000, entre $100.000.001 y $200.000.000 y más de $200.000.000, a lo cual
# usted deberá crear tres archivo llamado
import csv

archivo_csv = open("listado empresa.csv","r",newline="")
datos = csv.reader(archivo_csv,delimiter=",")
lista=list(datos)
archivo_csv.close()

# for i in range(len(lista)):
#     print(lista[i][0],lista[i][1],lista[i][2],sep=",")




archivo_csv = open("Pequeño_Contribuyente.csv","w",newline="")
escritor_csv = csv.writer(archivo_csv,delimiter=",")
escritor_csv.writerow(["Rut","Nombre","Ventas"])
for i in range(1,len(lista)):
    if len(lista[i])>1:
        if int(lista[i][2])<= 100000000:
            escritor_csv.writerow(lista[i])
archivo_csv.close()

archivo_csv = open("Mediano_Contribuyente.csv","w",newline="")
escritor_csv = csv.writer(archivo_csv,delimiter=",")
escritor_csv.writerow(["Rut","Nombre","Ventas"])
for i in range(1,len(lista)):
    if len(lista[i])>1:
        if int(lista[i][2])>=100000001 and int(lista[i][2])>=20000000 :
            escritor_csv.writerow(lista[i])
archivo_csv.close()

archivo_csv = open("Gran_Contribuyente.csv","w",newline="")
escritor_csv = csv.writer(archivo_csv,delimiter=",")
escritor_csv.writerow(["Rut","Nombre","Ventas"])
for i in range(1,len(lista)):
    if len(lista[i])>1:
        if int(lista[i][2])>200000000:
            escritor_csv.writerow(lista[i])
archivo_csv.close()