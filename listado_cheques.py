def msgInput():
    print ("""
Acontinuacion se le solicitara informacion para filtrar un archivo csv y de esa forma visualizar toda la informacion de los cheques emitidos o depositados por el cliente en cuestion.""")
    # Dispondra de la informacion en el siguiente orden.
    # Nombre archivo, DNI del cliente, tipo de cheque, estado del cheque, fecha origen, fecha pago, salida buscada.
    caso = []
    caso.append (input ("Ingrese el nombre del archivo a filtrar: "))
    ingresoDni(caso)
    print ("""
El cheque fue:
>>> Ingrese el numero de su respuesta
    1. Emitido
    2. Depositado
    """)
    tipoCheque(caso)
    print ("""
Cual es el estado del cheque:
>>> Ingrese el numero de su respuesta
    1. Pendiente
    2. Aprobado
    3. Rechazado
    """)
    estadoCheque(caso)
    print (caso)
    msgInput()

def ingresoDni(array):
    dni = input ("Ingrese el DNI del cliente: ")
    if dni.isdigit():
        array.append (int (dni))
    else:
        print ("Solo se aceptan enteros sin puntos, comas, ni espacios")
        ingresoDni(array)

def tipoCheque(array):
    tipo = input()
    if tipo.isdigit():
        if int(tipo) == 1:
            array.append("Emitido")
        elif int(tipo) == 2:
            array.append ("Depositado")
        else:
            print("Esa opcion no es correcta.")
            tipoCheque(array)
    else:
        print("Esa opcion no es correcta.")
        tipoCheque(array)

def estadoCheque(array):
    tipo = input()
    if tipo.isdigit():
        if int(tipo) == 1:
            array.append("Pendiente")
        elif int(tipo) == 2:
            array.append ("Aprobado")
        elif int(tipo) == 3:
            array.append ("Rechazado")
        else:
            print("Esa opcion no es correcta.")
            tipoCheque(array)
    else:
        print("Esa opcion no es correcta.")
        tipoCheque(array)

msgInput()