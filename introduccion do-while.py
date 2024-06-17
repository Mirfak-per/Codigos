"""
el ciclo do-while no existe en python, pero se puede simular 
mediante el ciclo while y el uso del comando break. el comando break 
permite terminar un ciclo (cualquiera), en cualquier momento.
"""

while True: 
    r = input ("desea salir? s/n : ").lower()
    if r=="s":
        break
    print("hola estoy fuera de la condicion")