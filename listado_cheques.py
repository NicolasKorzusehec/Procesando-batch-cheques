# Defino librerias a utilizar.
import csv
from filtrar import * # Todas funciones aplicadas para crear el array con las desiciones iniciales del usuario. Involucra la primer parte del programa.
from ejecutar import * # Todas las funciones usadas por el programa para ejecutarse. Involucra la segunda parte del programa. 
#Desde la obtencion del archivo csv y su conversion a un objeto utilizable, hasta su posterior salida. Depende de las decisiones tomadas por el usuario.

# Defino variables.
filtros = [] # Decisiones
archivoCheques = [] # En bruto
objetoDatos=[] # Objeto utilizable derivado del archivoCheques
resultados = [] # Objeto ya filtrado y dispuesto para su salida


def filtradoDicc(diccionario, filtros, resultados):
    print("hi")


if __name__ == '__main__':
    print ("""
    El programa ofrece una prueba con el archivo "test.csv" incluido""")
    
    # Crea un array con todos los filtros deseados por el usuario.
    filtrosCsv(filtros)
    print(filtros)

    # Recibe el nombre del archivo desde el primer elemento del array 'filtros' y lo asigna a la variable 'archivoCheques'  para poder trabajar sobre el.
    readFile(archivoCheques, filtros)

    # Itera en cada fila util del archivo a filtrar creando un objeto que se incluye en la lista 'objetoDatos' para trabajarla facilmente posteriormente.
    crearDicc(archivoCheques, objetoDatos)
    for obj in objetoDatos:
        print (obj)

    # Filtra el objeto creado a partir del csv con las deciciones del usuario de la funcion 'filtrarCsv()', luego incluye esos resultados en el objeto resultados.
    filtradoDicc(objetoDatos, filtros, resultados)

    # Recibe la decision del usuario sobre como presentar los resultados e invoca la funcion correspondiente a la misma.
    output(resultados, filtros)
