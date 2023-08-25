bike=["biela","pedales","sillin"]
opcion=0
print("partbikes")
print(".............")
print("1.agregar producto")
print("2.ver productos de bodega")
print("3.obtener valor del inventario")
print("4.ver los productos mas vendidos")
print("5.salir")
while opcion!=5:
    opcion=int(input("digita un numero"))

    if opcion==1:
        nombre=input("digite el nombre del producto")
        bike.append(nombre)
        print("se agrego el ojecto")
    elif opcion==2:
        print(bike)

    elif opcion==3:
        print("opcion 3")
    elif opcion==4:
        print("opcion 4")
    else:
        print("error")
print("salio del programa")