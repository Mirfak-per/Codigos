# Escribir una función que calcule el total de una factura tras aplicarle el IVA.
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura.
# Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 19%.

def facturaiva(dinero,Iva = 19):
    apliva = dinero * (Iva / 100)
    return (dinero+apliva)

plata = int(input("ingrese dinero "))

print("valor de nuevo monto",facturaiva(plata))

iva = int(input("ingrese un valor de iva ej: '45' "))

print("valor de nuevo monto",facturaiva(plata,iva))