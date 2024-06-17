cantdias = [31,28,31,30,31,31]
mes= list(("enero","marzo","abril"))

buscar = input()
if buscar in mes:
    n=mes.index(buscar)
    print (f"la cantidad de dias del mes {mes[n]} es {cantdias[n]}")