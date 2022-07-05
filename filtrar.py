import csv

# Esta funcion desacoplada me permite crear los filtros de forma indepediente en el script `filtrar.py` bajo la premisa de incluir el arreglo que contiene los filtros como parametro de las mismas, logrando asi mejorar sus especificidades facilmente. Inclusive el usuario podria decidir que filtros aplicar.
# !!! Se debe respetar la posicion  de la funcion 'nombreArchivo()' y 'salida()' para no romper el codigo en su ejecucion posteriormente!!!
def filtrosCsv(arreglo):
    print ("""
Acontinuacion se le solicitara informacion para filtrar un archivo csv y de esa forma visualizar toda la informacion de los cheques emitidos o depositados por el cliente en cuestion.
""")
    # Dispondra de la informacion en el siguiente orden.
    # Nombre archivo, salida buscada, DNI del cliente, tipo de cheque, estado del cheque, fecha origen, fecha pago.
    nombreArchivo(arreglo)
    salida(arreglo)
    ingresoDni(arreglo)
    tipoCheque(arreglo)
    estadoCheque(arreglo)
    fechaOrigen(arreglo)
    fechaPago(arreglo)

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
            file.close()
            array.append ("src/"+nombreArchivo)
            estado = True
        except FileNotFoundError:
            print ("""
            No se ha encontrado el archivo. Vuelve a intentar.""")
            continue

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

