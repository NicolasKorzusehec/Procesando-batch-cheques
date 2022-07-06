# Se debe revisar el resultado final x eu por alguna razon alguno de los array no queda con el largo esperado

import csv

ubicacionOrigen = "src/extension.csv" # Es el exportado desde excel con separador de ";"
archivoBruto = []
archivoSolucionado = []

def buscarArchivo(origen):
    estado = False
    print("""Ingrese el nombre del archivo a filtrar:
    Ejemplo: test.csv""")
    while estado != True:
        try:
            print(""">>> Se requiere colocar el archivo a verificar dentro de la carpeta src perteneciente al programa.""")
            #nombreArchivo = input()
            #file = open("src/"+nombreArchivo, "r")
            file = open(origen, "r")
            file.close()
            print ("Existe el archivo.")
            estado = True
        except FileNotFoundError:
            print ("""
            No se ha encontrado el archivo. Vuelve a intentar.""")
            continue

def readFile(datos, src):
    file = open(src)
    csvfile = csv.reader(file)
    for row in csvfile:
        if row != []:
            datos.append(row)
    file.close()

def arreglarCsv(origen, resultado):
    for row in origen:
        newRow = row[0].split(";")
        resultado.append(newRow)

def salidaArchivo(resultados):
    nombresalida = input("""Nombre archivo salida: 
    >>> Solo requiere el nombre, mas no la terminacion .csv
    """)
    with open(f"Resultados/{nombresalida}.csv", 'w', newline='') as file: # Es el archivo que se creo como resultado
        writer = csv.writer(file, quoting=csv.QUOTE_ALL,delimiter=',')
        writer.writerows(resultados)


if __name__ == "__main__":
    buscarArchivo(ubicacionOrigen) # Se debe definir al inicio del script.
    readFile(archivoBruto, ubicacionOrigen)
    print(archivoBruto)
    print ("Este es el archivo origen")

    arreglarCsv(archivoBruto, archivoSolucionado)
    print (archivoSolucionado)
    print ("Este el archivo solucionado")
    salidaArchivo(archivoSolucionado)