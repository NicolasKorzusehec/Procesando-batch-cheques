# Esta funcion desacoplada me permite crear los filtros de forma indepediente en el script `filtrar.py` bajo la premisa de incluir el arreglo que contiene los filtros como parametro de las mismas, logrando asi mejorar sus especificidades facilmente. Inclusive el usuario podria decidir que filtros aplicar.
# !!! Se debe respetar la posicion  de la funcion 'nombreArchivo()' y 'salida()' para no romper el codigo en su ejecucion posteriormente!!!
def decidir(obj, datos):
    print ("""
Acontinuacion se le solicitara informacion para filtrar un archivo csv y de esa forma visualizar toda la informacion de los cheques emitidos o depositados por el cliente en cuestion.
""")
    # Dispondra de la informacion en el siguiente orden.
    # Salida buscada, DNI del cliente, tipo de cheque, estado del cheque, fecha origen, fecha pago.
    salida(obj)
    ingresoDni(obj, datos)
    tipoCheque(obj)
    estadoCheque(obj)
    #fechaOrigen(obj)
    #fechaPago(obj)

def buscarArchivo(obj):
    estado = False
    print("""Ingrese el nombre del archivo a filtrar:
    Ejemplo: longtest.csv (RECOMENDADA)
    """)
    while estado != True:
        try:
            print(""">>> Se requiere colocar el archivo a verificar dentro de la carpeta src perteneciente al programa.""")
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

# Presenta en pantalla las opciones de dni disponibles, facilitando el uso de la aplicacion considerando que se deja de lado el error humano al tipiar el numero.
def ingresoDni(obj, datos):
    dniHabilitados = {}
    dniDisponibles(dniHabilitados, datos)
    print("""
>>> Se inspecciono el archivo para determinar todos los DNIs disponibles.
Seleccione el DNI del cliente:""")
    for choice in dniHabilitados:
        print(choice, ": ", dniHabilitados[choice])
    estado = False
    while estado != True:
        try:
            indice = input ()
            if indice.isdigit():
                obj["DNI"] = dniHabilitados[indice]
                estado = True
            else:
                print ("Solo se aceptan enteros sin puntos, comas, ni espacios.")
        except:
            print("Esa opcion no esta disponible.")
            estado = False

# alista todos los dnis unicos presentes en el archivo csv de origen
def dniDisponibles(habilitados, datos):
    dniContados = []
    n = 1
    for row in datos:
        if dniContados.count(row["DNI"]) == 0:
            habilitados[f"{n}"] = row["DNI"]
            dniContados.append (row["DNI"])
            n += 1

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
                obj["Tipo"] = "EMITIDO"
                estado = True
            elif int(tipo) == 2:
                obj["Tipo"] = "DEPOSITADO"
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
                obj["Estado"] = "PENDIENTE"
                estado = True
            elif int(tipo) == 2:
                obj["Estado"] = "APROBADO"
                estado = True
            elif int(tipo) == 3:
                obj["Estado"] = "RECHAZADO"
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
    obj["FechaPago"] ="Pendiente"

