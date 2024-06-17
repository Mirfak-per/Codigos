# De una empresa de transporte se quiere guardar el nombre de los conductores que 
# tiene, y los kilómetros que conducen cada día de la semana.
# Para guardar esta información se van a utilizar dos arreglos:
# • Nombre: Lista para guardar los nombres de los conductores.
# • kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
# Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realza 
# cada conductor.
# Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha 
# realizado.

nombres = list()
total_kms = list()
cant = int(input("ingrese la cantidad de empleados que tiene"))
kmstotal = 0

for i in range (cant):
    nombre = input(f"ingrese el nombre del emlpeado {i+1}")
    nombres.append(nombre)
    for i in range (6):
        kms= int(input(f"ingrese la cantidad de kms que viajo el conductor {nombre}, en el dia {i+1}\n si no vaijo ese dia ingrese 0\n"))
        kmstotal += kms
    total_kms.append(kmstotal)

for i in range (len(nombres)):
    print(f"el conductor {nombres[i]}, viajo un total de {total_kms[i]} kms esta semana")