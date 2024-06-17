alumnos =[]

while True:
    alumno =input("ingrese el nombre de un alumno y separe la nota por una coma (alumno1,60),\nsi ingresa un numero solo en el nombre guarda el archivo (21412123....)\n")
    
    if alumno.isnumeric()==True:
        break
    else:
        alumnos.insert(0,alumno)

archivo = open("notas.csv", "a")
archivo.write("Nombre,Nota\n")
for i in range(len(alumnos)):
    #archivo.write(f"{alumnos[i]}\n")
    archivo.writelines(f"{alumnos[i]}\n")
archivo.close()
#W -WRITE R- READ A- APPEND

