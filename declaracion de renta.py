#Los tramos impositivos para la declaración de la renta en un determinado
#país son los siguientes:
#Renta Tipo impositivo
#Menos de $1.000.000 5%
#Entre $1.000.000 y $2.000.000 15%
#Entre $2.000.000 y $3.500.000 20%
#Entre $3.500.000 y $6.000.000 30%
#Más de $6.000.000 45%
#Escribir un programa que pregunte al usuario su renta anual y muestre por
#pantalla el tipo impositivo que le corresponde.

renta = int(input("declare su renta anual\n"))

if renta< 1000000:
    print("a la declaración renta se le aplico un tipo impositivo del 5%")
    print("la cantidad de dinero que tiene que pagar es de", renta - (renta * 0.95))

elif renta>= 1000000 and renta <= 2000000:
    print("a la declaración renta se le aplico un tipo impositivo del 15%")
    print("la cantidad de dinero que tiene que pagar es de", renta - (renta * 0.85))

elif renta> 2000000 and renta <= 3500000:
    print("a la declaración renta se le aplico un tipo impositivo del 20%")
    print("la cantidad de dinero que tiene que pagar es de", renta - (renta * 0.80))

elif renta> 3500000 and renta <= 6000000:
    print("a la declaración renta se le aplico un tipo impositivo del 30%")
    print("la cantidad de dinero que tiene que pagar es de", renta - (renta * 0.70))

elif renta> 6000000:
    print("a la declaración renta se le aplico un tipo impositivo del 45%")
    print("la cantidad de dinero que tiene que pagar es de", renta - (renta * 0.55))