import csv

# Esta funcion guarda el archivo como csv en la variable archivoCheques para luego ser trabajada dese la misma
def readFile(datos, array):
    file = open(array[0])
    print(file)
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
            object[categorias[i]]= row[i]
            i += 1
        diccionario.append (object)







# Toma la decision sobre que tipo de salida del resultado realizar
def output(results, array):
    choice = array[1]
    print(choice)
    if choice == "pantalla":
        salidaPantalla(results)
    elif choice == "archivo":
        salidaArchivo(results)
    else:
        print ("Pendiente")

#Estructura que me sirve para escribir un archivo csv. Podria plantearse la salida en la carpeta descargas.
def salidaArchivo(resultados):
    file = open("Resultados/salida.csv", "w") #dni
    file.write("palabra1,palabra2,palabra3") #Resultados
    file.close()
    file = open ("Resultados/salida.csv", "r")
    csvsalida = csv.reader(file)
    print (csvsalida)
    for row in csvsalida: print(row)
    print (resultados)
    file.close()

def salidaPantalla(resultados):
    print ("Pendiente terminal")
    print (resultados)
