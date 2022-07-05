# Defino librerias a utilizar.
import csv
from filtrar import *

# Esta funcion desacoplada me permite crear los filtros de forma indepediente en el script `filtrar.py` bajo la premisa de incluir el arreglo que contiene los filtros como parametro de las mismas, logrando asi mejorar sus especificidades facilmente. Inclusive el usuario podria decidir que filtros aplicar.
def filtrosCsv(arreglo):
    print ("""
Acontinuacion se le solicitara informacion para filtrar un archivo csv y de esa forma visualizar toda la informacion de los cheques emitidos o depositados por el cliente en cuestion.
""")
    # Dispondra de la informacion en el siguiente orden.
    # Nombre archivo, DNI del cliente, tipo de cheque, estado del cheque, fecha origen, fecha pago, salida buscada.
    nombreArchivo(arreglo)
    ingresoDni(arreglo)
    tipoCheque(arreglo)
    estadoCheque(arreglo)
    fechaOrigen(arreglo)
    fechaPago(arreglo)
    salida(arreglo)

# Esta funcion guarda el archivo como csv en la variable archivoCheques para luego ser trabajada dese la misma
def readFile(datos, array):
    file = open(array[0])
    print(file)
    csvfile = csv.reader(file)
    print(csvfile)
    for row in csvfile:
        datos.append(row)

# Toma la decision sobre que tipo de salida del resultado realizar
def output(results, array):
    choice = array[6]
    print(choice)
    if choice == "pantalla":
        salidaPantalla(results)
    elif choice == "archivo":
        salidaArchivo(results)
    else:
        print ("Pendiente")

#Estructura que me sirve para escribir un archivo csv. Podria plantearse la salida en la carpeta descargas.
def salidaArchivo(resultados):
    file = open("Resultados/salida.csv", "w")
    file.write("palabra1,palabra2,palabra3") #Resultados
    file.close()
    file = open ("Resultados/salida.csv", "r")
    csvsalida = csv.reader(file)
    print (csvsalida)
    for row in csvsalida: print(row)
    print (resultados)

def salidaPantalla(resultados):
    print ("Pendiente terminal")
    print (resultados)

if __name__ == '__main__':
    print ("""
    El programa ofrece una prueba con el archivo "test.csv" incluido""")
    filtros = []
    archivoCheques = []
    archivoResultado = []
    
    filtrosCsv(filtros)
    print(filtros)

    readFile(archivoCheques, filtros)
    print (archivoCheques)
    
    output(archivoResultado, filtros)
    salidaArchivo(archivoResultado)
    salidaPantalla(archivoResultado)