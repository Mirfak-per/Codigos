cantdias = [31,29,31,30,31,30,31,31,29,31,30,29]
mes= list(("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"))

buscar = input()
if buscar in mes:
    n=mes.index(buscar.lower)
    print (f"la cantidad de dias del mes {mes[n]} es {cantdias[n]}")
else:
    print("error")
    
