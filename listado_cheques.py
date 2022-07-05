# Defino librerias a utilizar.
# Todas las funciones aplicadas para crear el obj con las desiciones iniciales del usuario. Involucra la primer parte del programa.
from choices import * 
# Todas las funciones usadas por el programa para ejecutarse. Involucra la segunda parte del programa. 
# Desde la obtencion del archivo csv y su conversion a un objeto utilizable, hasta su posterior salida. Depende de las decisiones tomadas por el usuario.
from ejecutar import * 


# Defino variables.
archivoOrigen = {} # Contendra la ubicacion del archivo compre el que se trabajara.
decisiones = {} # Decisiones
filtro = {} # Filtros especificos derivados de las decisiones
archivoCheques = [] # En bruto
objDatos=[] # Lista de objetos utilizable derivado del archivoCheques
resultados = [] # Lista de objetos ya filtrado y dispuesto para su salida


if __name__ == '__main__':
    print ("""
>>> El programa ofrece una prueba con el archivo "test.csv" incluido""")
    
    nombreArchivo(archivoOrigen)
    
    # Recibe el nombre del archivo desde el primer elemento del array 'filtros' y lo asigna a la variable 'archivoCheques'  para poder trabajar sobre el.
    readFile(archivoCheques, archivoOrigen)

    # Itera en cada fila util del archivo a filtrar creando un objeto que se incluye en la lista 'objetoDatos' para trabajarla facilmente posteriormente.
    crearDicc(archivoCheques, objDatos)

    # Crea un obj con todas las decisiones deseados por el usuario.
    decidir(decisiones)

    #Define un objeto especifico que contiene unicamente los filtros.
    filtrar(decisiones, filtro)

    # Filtra el objeto creado a partir del csv con las deciciones del usuario de la funcion 'filtrarCsv()', luego incluye esos resultados en el objeto resultados.
    filtradoDicc(objDatos, filtro, resultados)

    # Recibe la decision del usuario sobre como presentar los resultados e invoca la funcion correspondiente a la misma.
    output(resultados, decisiones)
