#Una empresa les paga a sus empleados con base en las horas trabajadas en la semana 
#(de lunes a viernes).Para esto, se registran las horas que trabajó cada día y
#el valor de la hora de cada empleado. Realice unalgoritmo para determinar el sueldo semanal
#de cada uno de los trabajadores. Además, calcule cuánto pagó laempresa por los todos los empleados.
#Al iniciar la ejecución, el algoritmo debe pedir que se ingrese la cantidadde empleados.

empleados = int(input("ingrese la cantidad de empleados\n"))
horas = int(input("ingrese cuanto se le paga a los empleados por hora\n"))
ix = 0
total = 0
for ix in range(empleados):
    print(""" 
                   menu
          opcion 1, total por semana
          opcion 2, total por dia
            """)
    opc=int(input(""))
    if opc == 1:
        semana = int(input(f"ingrese las horas por semana del empleado {ix+1}\n"))
        print(f"la cantidad a pagar por semana al empeado {ix+1} es de:", horas * semana)
        total = total + (horas * semana)
        print(f"la cantidad a pagar a todos los empleados es de: {total}")

    elif opc ==2:
        print("hasta el sabado, 6 dias, si el empleado no trabajo ese dia ingrese 0")
        dia1 = int(input(f"ingrese la cantidad de horas trabajadas del empleado {ix+1} el dia lunes\n"))
        dia2 = int(input(f"ingrese la cantidad de horas trabajadas del empleado {ix+1} el dia martes\n"))
        dia3 = int(input(f"ingrese la cantidad de horas trabajadas del empleado {ix+1} el dia miercoles\n"))
        dia4 = int(input(f"ingrese la cantidad de horas trabajadas del empleado {ix+1} el dia jueves\n"))
        dia5 = int(input(f"ingrese la cantidad de horas trabajadas del empleado {ix+1} el dia viernes\n"))
        dia6 = int(input(f"ingrese la cantidad de horas trabajadas del empleado {ix+1} el dia sabado\n"))
        semana2 = dia1 + dia2 + dia3 + dia4 + dia5 + dia6
        
        print(f"la cantidad a pagar al empleado {ix+1} es de: {semana2 * horas}")
        total = total + (semana2 * horas)
        print(f"la cantidad a pagar a todos los empleados es de: {total}")