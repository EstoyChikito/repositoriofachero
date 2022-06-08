#variables
fecha_mantenimiento=[]
registros=[]
infovehiculo=[]
t_vehiculos=["Tipos de vehiculos permitidos: ","d=Diesel","b=Bencina","e=Electrico","h=Hibrido"]
menu=["----------------","Opcion 1-Registrar automovil","Opcion 2-Registro mantenimiento","Opcion 3-Consultar automovil","Opcion 4-Salir","----------------"]
swmenu=1
nummenu=int()
contador=0

try:
    while swmenu == 1:
        for opcmenu in menu:
            print (opcmenu)
        nummenu=int(input("Ingrese una opción: "))
        if nummenu == 1:
            print("Ha seleccionado la opcion 1-Registrar automovil")
            try:
                validar_patente=False
                while validar_patente==False:
                    patente=input("Ingrese la patente de su vehiculo: ")
                    if patente[0:3].isdigit() and patente[4:6].isalpha():
                        validar_patente=True
                        print("patente validada correctamente")
                    elif patente[0:3].isalpha() and patente[4:6].isdigit():
                        validar_patente=True
                        print("patente validada correctamente")
                    else:
                        print("Patente mal ingresada")
                validar_patente=False        
            except:
                print("error en pedir patente")
            try:
                año_fabricacion=int(input("Ingrese año de fabricacion de el vehiculo: "))
                while año_fabricacion > 2021 or año_fabricacion < 1900:
                    print("Año de fabricacion fuera de el rango, debe ingresar un año entre 1900 y 2021... \nIntente de nuevo")
                    año_fabricacion=int(input("Ingrese año de fabricacion: "))
            except:
                print("error en pedir año fabricacion")
            try:
                for tipovehiculos in t_vehiculos:
                    print(tipovehiculos)
                tipo_vehiculo=input("Ingrese letra segun tipo de vehiculo: ")
                letra_vehiculo=tipo_vehiculo.upper()
                while letra_vehiculo != "B" and letra_vehiculo != "H" and letra_vehiculo != "E" and letra_vehiculo != "D":
                    print("Letra Ingresada incorrectamente, intente de nuevo")
                    for tipovehiculos in t_vehiculos:
                        print(tipovehiculos)
                    tipo_vehiculo=input("Ingrese letra segun tipo de vehiculo: ")
                    letra_vehiculo=tipo_vehiculo.upper()
            except:
                print("Error en Tipo de vehiculo")

            try:
                marca=input("Ingrese marca: ")
                while marca == "":
                    print("La marca no puede estar vacia, por favor intente de nuevo")
                    marca=input("Ingrese marca: ")        
            except:
                print("Error en pedir marca")

            try:
                modelo=input("Ingrese modelo: ")
                while modelo == "":
                    print("El modelo no puede estar vacio, por favor intente de nuevo")
                    modelo=input("Ingrese marca: ")  
            except:
                print("Error en pedir modelo")

            concat=["Patente:",patente," Año de fabricación:",año_fabricacion," Tipo de vehiculo:",tipo_vehiculo," Marca:",marca," Modelo:",modelo]
            infovehiculo.append(concat)


        elif nummenu == 2:
            try:
                print("Ha seleccionado la opcion 2-Registro mantenimiento")
                nuevo=input("Ingrese patente a buscar:  ")
            
         
                for lis in infovehiculo:
                    valorindice = lis
                    for v in valorindice:
                        if nuevo==v:
                            patenteencontrada=True
                            break
                    contador=contador+1 
               

               
                while patenteencontrada == False:
                    print("Patente no encontrada, intente de nuevo")
                    nuevo=input("Ingrese patente a buscar:  ")
                    for lis in infovehiculo:
                        valorindice = lis
                        for v in valorindice:
                            if nuevo==v:
                                patenteencontrada=True
                                break
                        contador=contador+1    
                
                
                if patenteencontrada == True:
                    print("Patente encontrada\nSe le pedira ingresar el dia para registrarlo en el mantenimiento...")
                    fecha_mantenimiento=(input("Ingrese fecha: "))
                    obserbaciones=input("Ingrese las observaciones de su vehiculo(Esto lo verá el mecanico al momento de el mantenimiento): ")
                    registro=["Fecha mantenimiento:",fecha_mantenimiento,"Observaciones:",obserbaciones]
                    print("Registro de mantenimiento creado correctamente")
                    infovehiculo.append[registro]
            except:
                print("Error menu2")


        elif nummenu == 3:
            print("Ha seleccionado la opcion 3-Consultar automovil")
            nuevo=input("Ingrese patente a buscar:  ")
            for lis in infovehiculo:
                valorindice = lis
                for v in valorindice:
                    if nuevo==v:
                        print("Valor encontrado es ->  :",infovehiculo[contador,contador])
                        break
                contador=contador+1 
                

        elif nummenu == 4:
            print("Ha seleccionado la opcion 4-Salir")
            swmenu=0
        else:
            print("Numero incorrecto")
except:
    print("Error en el menu")
print("Cerrando sesión...")




