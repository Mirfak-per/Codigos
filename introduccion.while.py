"""
ciclo while 
- el ciclo while realiza la condicion al principio del ciclo, en el caso de que la condicion sea verdadera entramos al ciclo, en caso contrario finaliza el ciclo, 
- como la condicion se realiza al principio, podria nunca ejecutarse. 
"""

x = 5

while x<10:
    x += 1
    print(x)
    
    r = input ("ingrese una letra: ")
    while r!="x":
        print(r)
        r= input ("ingrese una letra: ")
