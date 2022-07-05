import csv

# Esta funcion desacoplada me permite crear los filtros de forma indepediente en el script `filtrar.py` bajo la premisa de incluir el arreglo que contiene los filtros como parametro de las mismas, logrando asi mejorar sus especificidades facilmente. Inclusive el usuario podria decidir que filtros aplicar.
# !!! Se debe respetar la posicion  de la funcion 'nombreArchivo()' y 'salida()' para no romper el codigo en su ejecucion posteriormente!!!
def filtrosCsv(obj):
    print ("""
Acontinuacion se le solicitara informacion para filtrar un archivo csv y de esa forma visualizar toda la informacion de los cheques emitidos o depositados por el cliente en cuestion.
""")
    # Dispondra de la informacion en el siguiente orden.
    # Nombre archivo, salida buscada, DNI del cliente, tipo de cheque, estado del cheque, fecha origen, fecha pago.
    nombreArchivo(obj)
    salida(obj)
    ingresoDni(obj)
    tipoCheque(obj)
    estadoCheque(obj)
    fechaOrigen(obj)
    fechaPago(obj)

def nombreArchivo(obj):
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
            obj["archivo"] ="src/"+nombreArchivo
            estado = True
        except FileNotFoundError:
            print ("""
            No se ha encontrado el archivo. Vuelve a intentar.""")
            continue

def salida(obj):
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
                obj["salida"] = "pantalla"
                estado = True
            elif int(salida) == 2:
                obj["salida"] = "archivo"
                estado = True
            else:
                print("Esa opcion no es correcta.")
        else:
            print("Esa opcion no es correcta.")

def ingresoDni(obj):
    estado = False
    print ("Ingrese el DNI del cliente: ")
    while estado != True:
        dni = input ()
        if dni.isdigit():
            obj["DNI"] = int (dni)
            estado = True
        else:
            print ("Solo se aceptan enteros sin puntos, comas, ni espacios")

def tipoCheque(obj):
    estado = False
    print ("""
El cheque fue:
>>> Ingrese el numero de su respuesta
    1. Emitido
    2. Depositado
    3. No requiero especificar
    """)
    while estado != True:
        tipo = input()
        if tipo.isdigit():
            if int(tipo) == 1:
                obj["Tipo"] = "Emitido"
                estado = True
            elif int(tipo) == 2:
                obj["Tipo"] = "Depositado"
                estado = True
            elif int(tipo) == 3:
                return
            else:
                print("Esa opcion no es correcta.")
        else:
            print("Esa opcion no es correcta.")

def estadoCheque(obj):
    estado = False
    print ("""
Cual es el estado del cheque:
>>> Ingrese el numero de su respuesta
    1. Pendiente
    2. Aprobado
    3. Rechazado
    4. No requiero especificar
    """)
    while estado != True:
        tipo = input()
        if tipo.isdigit():
            if int(tipo) == 1:
                obj["Estado"] = "Pendiente"
                estado = True
            elif int(tipo) == 2:
                obj["Estado"] = "Aprobado"
                estado = True
            elif int(tipo) == 3:
                obj["Estado"] = "Rechazado"
                estado = True
            elif int(tipo) == 4:
                return
            else:
                print("Esa opcion no es correcta.")
        else:
            print("Esa opcion no es correcta.")

def fechaOrigen(obj):
    print("Pendiente programar fechaOrigen")
    obj["FechaOrigen"] ="Pendiente"

def fechaPago(obj):
    print("Pendiente programar fechaPago")
    obj["Fecha"] ="Pendiente"

