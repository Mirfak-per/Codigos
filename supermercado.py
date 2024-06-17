"""
Desarrollar un algoritmo que permita administrar el listado de productos de un almacén
de barrio.
El sistema de productos debe permitir gestionar completamente los
productos teniendo las siguientes consideraciones:

● Agregar: Agregar un producto a la lista. El sistema debe validar que el nombre del
producto no se encuentre registrado
en la lista.

● Listar: Debe mostrar la lista de productos ordenada de forma vertical.

● Buscar: Debe permitir buscar un producto según la posición dentro de la lista

● Modificar: El sistema debe poder modificar productos que se encuentren guardados
previamente.

● Eliminar: El sistema de poder eliminar productos ya sea por nombre o posición en la
lista."""

opc= 1
productos = []
n2= 0

while opc != 6:
    print("""
    ADMINISTRACIÓN DE PRODUCTOS
    *******************************
    1) Agregar Producto
    2) Listar Productos
    3) Buscar Producto
    4) Modificar Producto
    5) Eliminar Producto
    6) Salir
    """)
    opc = int(input())

    if opc == 1:
        agregar = input("agrege el producto deseado")

        if agregar in productos:
            print ("el producto que intento agregar ya se encuantra en la lista")
        else:
            productos.append(agregar)

    elif opc==2:
        print("Lista de los productos")
        for i in (productos):
            print(i)

    elif opc==3:
        print("ingrese el nombre de el producto que desea buscar")
        buscar = input()
        if buscar in productos:
            for i in (productos):
                if i == buscar:
                    print(f"el producto ingresado es el numero {i}, se en cuentra en la lista")
        else:
            print("el producto que ingreso no se encuentra en la lista")

    elif opc == 4:
        print("para modificar un producto tiene que saber el numero o nombre, \n ejemplo: el primer producto es 0, el segundo es 1 y asi")
        n = input("ingrese el producto que desea modificar")
        if n.isdigit() == True:
            print(f"el producto que quiere cambiar es {productos[int(n)]}")
        else:
            print(f"el producto que desea cambiar es {n}")

        cambio = input("ingrese el cambio que desea para el producto, nombre si quiere cancelar esta accion\n ingrese el mismo nombre")
        if n.isdigit():
            productos[int(n)] = cambio
        else:
            if n in productos:
                for i in (productos):
                    if i == n:
                        n2 = i
        productos[n2] = cambio

    elif opc == 5:
        print("para eliminar un producto, ingrese el producto por su nombre o codigo")
        eliminar = input()
        if eliminar.isalpha():
            productos.remove(eliminar)
        else:
            productos.pop(eliminar)

    elif opc ==6:
        print("saliendo del programa")