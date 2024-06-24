def registrar_trabajador():
    #Nombre y Apellido, Cargo, Sueldo bruto. 
    #Una vez ingresado los datos, se deben calcular,
    Diccionario={}
    lista = []
    Nombre = input("Ingrese el nombre y apellido del trabajador ")
    Cargo = input("Ingrese el cargo del trabajador ")
    while True:
        try:
            Sueldo = int(input("Ingrese el sueldo bruto del trabajador "))
            break
        except:
            print("Error, Intente otra vez")
    Diccionario={
                "Nombre": Nombre,
                "Cargo": Cargo,
                "Sueldo": Sueldo,
                }
    lista.append(Diccionario)
    return lista[:]


def tabla_de_trabajadores(lista):
    #los valores de acuerdo con la siguiente tabla
    # Trabajador Cargo   Sueldo Bruto   Desc. Salud   Desc. AFP Líquido a pagar
    # Homero      CEO       1000000         70000       120000         810000
    # Simpson
    print(f"""
                 Trabajador       Cargo         Sueldo Bruto        Desc. Salud         Desc. AFP         Líquido a pagar""")
    for i in range (len(lista)):
        print({lista[i]["Nombre"]},    {lista[i]["Cargo"]},    {lista[i]["Sueldo"]},    {lista[i]["Sueldo"]*0.12},      {lista[i]["Sueldo"]*0.07},     {lista[i]["Sueldo"]-((lista[i]["Sueldo"]*0.07)+(lista[i]["Sueldo"]*0.12))}) 


def imprimir_sueldos(lista):
    import csv
    with open("empresa.csv","w",newline="") as sueldo_csv:
        escribir_fila=csv.writer(sueldo_csv)
        escribir_fila.writerows("Trabajador","Cargo","Sueldo Bruto","Desc. Salud","Desc. AFP","Líquido a pagar")
        escribir_fila.writerow(lista)

def menu():
    print("""
    1. Registrar trabajador
    2. Listar los todos los trabajadores
    3. Imprimir planilla de sueldos
    4. Salir del Programa
    """)
    opc = int(input())
    return opc