"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo,
Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
nota que ha sacado en cada asignatura, y después las muestre por pantalla con el
mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las
asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas
por el usuario."""
import random

Asignaturas = []

Notas = []

cont = input("ingrese la cantidad de asiganturas que quiere ingresar\n")

for i in range (int(cont)):
    materia = input(f"ingrese la asignatura, (por ejemplo Matemática) hasta terminar el conteo {i}\n")
    Asignaturas.append(materia)

    Notas.append(random.randint(10,70))

for i in range (len(Asignaturas)):
    print(f"\tEn {Asignaturas[i]} \n\thas sacado {Notas[i]}\n")
