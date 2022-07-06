import csv
from datetime import datetime
from choices import *

# Esta funcion guarda el archivo como csv en la variable archivoCheques para luego ser trabajada desde la misma
def readFile(datos, obj):
    file = open(obj["archivo"])
    #print(file)
    csvfile = csv.reader(file)
    for row in csvfile:
        if row != []:
            datos.append(row)
    file.close()

# Itera en cada fila util del archivo a filtrar creando un objeto que se incluye en la lista objetoDatos para trabajarla facilmente posteriormente.
def crearDicc(data, diccionario):
    categorias = data[0] # primer fila del csv
    casos = data[1:] # Las demas filas
    # Creo un objeto vacio que contendra la row, luego itero en cada categoria y su corresondiente valor para crear facilmente un objeto independientemente de la cantidad de pares/valor que dispongamos mientas el csv haya sido correctamente creado.
    for row in casos:
        object = {}
        i = 0
        while i < len (categorias):
            if categorias[i] == "Valor":
                value = float(row[i])
                object[categorias[i]]= value
                i += 1
            else:
                object[categorias[i]]= row[i]
                i += 1
        diccionario.append (object)

# Filtra el objeto creado a partir del csv con las decisiones del usuario de la funcion 'filtrarCsv()', luego incluye esos resultados en el objeto resultados.
def crearFiltros(choices, filtros):
    for key in choices:
        if key != "archivo" and key != "salida":
            filtros[key] = choices[key]
    print("Los filtros a usar son: ", filtros)

# Itera por los pares clave/valor el objeto filtro y lo compara con el mismo par de cada caso. En caso de darse una disparidad se cabia el estado a false y no se incluye esa fila en los resultados
def filtradoDicc(data, filtros, results):
    for row in data:
        estado = True
        for key in filtros:
            if row[key] != filtros[key]:
                estado = False
        if estado:
            results.append(row)

# Toma la decision sobre que tipo de salida del resultado realizar.
def output(results, obj):
    choice = obj["salida"]
    if choice == "pantalla":
        salidaPantalla(results)
    elif choice == "archivo":
        salidaArchivo(results)
    else:
        print ("Pendiente")

#Estructura que transforma los resultados en un estring, luego los incluye en un archio csv.
def salidaArchivo(resultados):
    contenido = ""
    headerReference = resultados[0]
    for key in headerReference:
        contenido += key + ","
    contenido = contenido[:len(contenido)-1]
    contenido += "\n"
    for row in resultados:
        for key in row:
            strValue = str(row[key])
            contenido += strValue + ","
        contenido = contenido[:len(contenido)-1]
        contenido += "\n"
    srcOut = nombrandoArchivo(resultados)
    file = open(srcOut, "w") 
    file.write(contenido) #Resultados
    file.close()


def nombrandoArchivo(results):
    dniUso = results[0]["DNI"]
    timest = timestampActual()
    print (msgPosArchivo (dniUso, timest))
    print (timest)

    nameArchivo = dniUso + "-" + timest + ".csv"
    print("El nombre del archivo es ", nameArchivo)
    path = "Resultados/" + nameArchivo
    return path

def timestampActual():
    dt = datetime.now() # Obtengo la fecha y hora actual.
    ts = str (datetime.timestamp(dt)) #en funcion de esos datos obtengo el timestamp.
    return ts

def msgPosArchivo(dni, tiempo):
    ts =  datetime.timestamp(tiempo)
    return f"Se imprimio un .csv en la carpeta `Resultados`. La misma refiere  al dni: {dni} y el timestamp: {tiempo} el cual corresponde a la fecha{ts}."


# Imprime en consola los resultados obtenidos.
def salidaPantalla(resultados):
    if resultados != []:
        print ("""
    Los resultados obtenidos fueron los siguientes: """)
        print ("-----------------------------------------")
        for row in resultados:
            for key in row:
                print(key, ":", row[key])
            print ("-----------------------------------------")
    else:
        print ("No hay transacciones con esas caracteristicas.")