import csv

from choices import nombreArchivo

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
            object[categorias[i]]= row[i]
            i += 1
        diccionario.append (object)

# Filtra el objeto creado a partir del csv con las decisiones del usuario de la funcion 'filtrarCsv()', luego incluye esos resultados en el objeto resultados.
def filtrar(choices, filtros):
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
    if results == {}:
        print ("No hay transacciones con esas caracteristicas.")
        return main()





# Toma la decision sobre que tipo de salida del resultado realizar.
def output(results, obj):
    choice = obj["salida"]
    if choice == "pantalla":
        salidaPantalla(results)
    elif choice == "archivo":
        salidaArchivo(results)
    else:
        print ("Pendiente")

#Estructura que me sirve para escribir un archivo csv. Podria plantearse la salida en la carpeta descargas.
def salidaArchivo(resultados):
    contenido = ""
    header = []
    for key in resultados[0]:
        header.append(key)
    contenido += header
    for row in resultados:
        bodyRow = []
        for key in row:
            bodyRow.append(row[key])
        contenido += bodyRow
    nombresalida = input("Nombre archivo salida: ")
    file = open(f"Resultados/{nombresalida}.csv", "w") #dni
    file.write(contenido) #Resultados
    file.close()

def salidaPantalla(resultados):
    print ("""
Los resultados obtenidos fueron los siguientes: """)
    print ("-----------------------------------------")
    for row in resultados:
        for key in row:
            print(key, ":", row[key])
        print ("-----------------------------------------")