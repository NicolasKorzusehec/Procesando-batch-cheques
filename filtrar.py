import csv

def nombreArchivo(array):
    estado = False
    print("""Ingrese el nombre del archivo a filtrar:
    Ejemplo: test.csv (disponible)
    ***Este campo es obligatorio.""")
    while estado != True:
        try:
            print(""">>>Se requiere colocar el archivo a verificar dentro de la carpeta src perteneciente al programa.""")
            nombreArchivo = input()
            file = open("src/"+nombreArchivo, "r")
            csvfile = csv.reader(file)
            print (csvfile)
            array.append ("src/"+nombreArchivo)
            estado = True
        except FileNotFoundError:
            print ("""
            No se ha encontrado el archivo. Vuelve a intentar.""")
            continue

def ingresoDni(array):
    estado = False
    print ("Ingrese el DNI del cliente: ")
    while estado != True:
        dni = input ()
        if dni.isdigit():
            array.append (int (dni))
            estado = True
        else:
            print ("Solo se aceptan enteros sin puntos, comas, ni espacios")

def tipoCheque(array):
    estado = False
    print ("""
El cheque fue:
>>> Ingrese el numero de su respuesta
    1. Emitido
    2. Depositado
    """)
    while estado != True:
        tipo = input()
        if tipo.isdigit():
            if int(tipo) == 1:
                array.append("Emitido")
                estado = True
            elif int(tipo) == 2:
                array.append ("Depositado")
                estado = True
            else:
                print("Esa opcion no es correcta.")
        else:
            print("Esa opcion no es correcta.")

def estadoCheque(array):
    estado = False
    print ("""
Cual es el estado del cheque:
>>> Ingrese el numero de su respuesta
    1. Pendiente
    2. Aprobado
    3. Rechazado
    """)
    while estado != True:
        tipo = input()
        if tipo.isdigit():
            if int(tipo) == 1:
                array.append("Pendiente")
                estado = True
            elif int(tipo) == 2:
                array.append ("Aprobado")
                estado = True
            elif int(tipo) == 3:
                array.append ("Rechazado")
                estado = True
            else:
                print("Esa opcion no es correcta.")
        else:
            print("Esa opcion no es correcta.")

def fechaOrigen(array):
    print("Pendiente programar fechaOrigen")
    array.append("Pendiente")

def fechaPago(array):
    print("Pendiente programar fechaPago")
    array.append("Pendiente")

def salida(array):
    estado = False
    print ("""
Como quisiera visualizar el resultado?
>>> Ingrese el numero de su respuesta
    1. Por pantalla
    2. En otro archivo csv
    """)
    while estado != True:
        salida = input()
        if salida.isdigit():
            if int(salida) == 1:
                array.append("pantalla")
                estado = True
            elif int(salida) == 2:
                array.append ("archivo")
                estado = True
            else:
                print("Esa opcion no es correcta.")
        else:
            print("Esa opcion no es correcta.")
