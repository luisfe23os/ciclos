print("Fiesta crazy")
print("**********")
print("0.salir")
print("1.registrar invitado")
print("2.ver lista de invitados")
print("3.ver quien pago ")
print("4.ver quien no pago")
print("5.cambiar informacion")
print("6.retirar invitados")
print("**********")

opcion=8
invitados =[]

while opcion!=0:
    invitado={}
    opcion=int(input("ingrese un numero "))
    if opcion==1:
     invitado["nombre"]=input("digite su nombre ")
     invitado["id"]=input("diigte su id ")
     invitado["cedula"]=input("ingrese su cedula ") 
     invitado["eps"]=input("dgite su eps ")
     invitado["edad"]=input("edad ")
     invitado["estado"]=bool(input("pago?? "))
     invitado["valorcouta"]=float(input("ingrese el valor "))  #casteo

     invitados.append(invitado)

    elif opcion==2:
        # pass passar al siguiete 
        # recorrido de la lista 
        # print(invitados)
        for persona in invitados:
            print(f"persona:{persona['nombre']}")
            print(f"persona:{persona['id']}")
    elif opcion==3:
        for persona in invitados:
            if persona["estado"]==true:
                print(persona)
    elif opcion==4:
        pass
    elif opcion==5:
        pass
    elif opcion==6:
        pass
    else:
        print("opcion invalidad")