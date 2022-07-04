def nombreArchivo(array):
    estado = False
    print("""Ingrese el nombre del archivo a filtrar: 
    >>>Solo debe escribir el nombre mas no la terminacion .csv""")
    array.append (input ())

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
    print("Pendiente programar salida")
    array.append("Pendiente")
