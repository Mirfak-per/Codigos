#Desarrolle un algoritmo que solicite ingresar las notas de un alumno en particular.
#Al principio del algoritmo,el usuario debe ingresar la cantidad de notas que se requiere ingresar. 
#También debe solicitar el nombre de laasignatura y nombre del alumno.
#Al finalizar, se debe mostrar al alumno el promedio de las notas ingresadasdel siguiente modo
#El alumno [Pepito Perez] tiene un promedio de [6,5] en la asignatura de [Matemáticas]

nombre = input("ingrese el nombre completo del alumno\n")
materia = input("ingrese la materia del alumno\n")
cont = 0
cont2 = 0
suma = 0

while cont != 1:
    nota = float(input("ingrese la nota \n si quiere terminar ingrese 0\n"))
    if nota == 0:
        cont = 0
    else:
        cont2 = cont2 + 1
        suma = suma + nota

promedio = suma / cont2

print(f"El alumno {nombre} tiene un promedio de {round(promedio,2)} en la asignatura de {materia}")