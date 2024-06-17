##alumnos = ["Pedro","Luis","Carlos"]
alumnos =[]
while True:
    alumno =input("ingrese el nombre de un alumno, si ingresa un numero guarda los archivos")
    if alumno.isnumeric()==True:
        break
    else:
        alumnos.insert(0,alumno)
    
archivo = open("alumnos.txt", "w")

for i in range(len(alumnos)):
    archivo.write(f"{alumnos[i]}\n")

archivo.close()
