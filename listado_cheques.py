# Defino librerias a utilizar.
import csv

from filtrar import *

# Esta funcion desacoplada me permite crear los filtros de forma indepediente en archivo `filtrar.py` bajo la premisa de incluir el arreglo que contiene los filtros como parametro de las mismas, logrando asi mejorar sus especificidades facilmente. Inclusive el usuario podria decidir que filtros aplicar.
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

def ejecucion(arreglo):
    file = open(arreglo[0])
    csvfile = csv.reader(file)
    for row in csvfile:
        print(row)
    print (csvfile)
    print ("Pendiente programar ejecucion")

#Estructura que me sirve para escribir un archivo csv.
def salidaPrograma():
    file = open("salida.csv", "w")
    file.write("palabra1,palabra2,palabra3")
    file.close()
    file = open ("salida.csv", "r")
    csvsalida = csv.reader(file)
    print (csvsalida)
    for row in csvsalida: print(row)

if __name__ == '__main__':
    filtros = []
    filtrosCsv(filtros)
    print(filtros)
    ejecucion(filtros)
    salidaPrograma()