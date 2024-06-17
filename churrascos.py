"""En un delivery se venden 4 tipos de sándwich:
- Churrasco $1.400
- Completo $1.000
-Vegetariano $1.900
- Barros Luco $2.500
"""

churrasco = 1400
completo = 1000
vegetariano = 1900
barrosluco = 2500
total=0

#PRESENTAMOS SISTEMA

print(f"""
 BIENVENIDO AL DELIVERY DE SANDWICH
--------------------------------------------
1) CHURRASCO ${churrasco} 
2) COMPLETO $ {completo}
3) VEGETARIANO $ {vegetariano}
4) BARROS LUCO $ {barrosluco}
5) CANCELAR COMPRA """)

opcion = int (input("SELECCIONE :"))

#VALIDAR OPCION 
if opcion in (1,2,3,4,5):
    cantidad = int(input("ingrese el sandwich que desea agregar :"))
    
    #VALIDAR CANTIDAD 
 if cantidad>0
   if opcion==1:
    print("ha seleccionado churrasco",cantidad*churrasco)
   if opcion==2:
    print("ha seleccionado completo",cantidad*completo)
   if opcion==3:
    print("ha seleccionado vegetariano",cantidad*vegetariano)
   if opcion==4:
    print("ha seleccionado barrosluco", catidad * barrosluco)
   if opcion==5:
    print("ha seleccionado "salir"")
   
             


     