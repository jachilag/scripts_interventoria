from email.policy import strict
from messageBoxes import *
from PyPDF2 import PdfFileMerger
from progress.bar import Bar, ChargingBar
from os import walk
import os

""" CASO DE USO ESPECIFICO: este script es para unir los pdfs que tengan el mismo nombre pero que estan separadas en
diferentes carpetas, en este caso son 4 carpetas. En una quinta carpeta se generan los pdfs que resulta de la union
de los pdfs de las primeras cuatro carpetas; solo se unen entre si los archivos que tengan el mismo nombre.
Importante que los archivos pdfs en cada una de las 4 primeras carpetas esten completas con su correspondiente 
informacion.

las carpetas deben estar tituladas asi:
1. INFORME Y EV.COSTOS
2. PROTOCOLOS
3. BITACORA
4. FORMATOS INTERVENTORIA
5. COMPILADOS
"""


def rutaArchivos(ruta = '.'):
    """ 
    genera una lista con las direcciones de las carpetas qeu ya no tienen subcarpetas, esto con el fin de llegar hasta donde estan
    los archivos del tipo que se necesite. en mi caso de tipo pdf
    """
    rutas = []
    fileName = []
    numeroEliminar = len(ruta)

    for (dirs, subcapetas, _) in walk(ruta):
        if(len(subcapetas) == 0):
            rutas.append(dirs)
            texto = (dirs[numeroEliminar+1::1])
            fileName.append(texto)

    return fileName, rutas

def unirPDFsiniestros():
    print(""" \nDebe seleccionar la carpeta general que contenga la estructura de carpetas:
    1. INFORME Y EV.COSTOS
    2. PROTOCOLOS
    3. BITACORA
    4. FORMATOS INTERVENTORIA
    5. COMPILADOS
     """)
    seleccion = 'C:/Users/User/Desktop/jonathan/DIGITALIZACION FOTOS/QUINCENA 2'
    if not seleccion: 
        print("no se eligió ninguna opcion")
        return

    nombres, rutas = rutaArchivos(seleccion)
    archivosPDF = [(archivo) for archivo in os.listdir(rutas[0]) if archivo.endswith(".pdf")]
    
    bar2 = Bar("Uniendo Archivos: ", max=len(archivosPDF))
    for file in archivosPDF:
        pdfs = []
        fusionador = PdfFileMerger(strict=False)

        for i in range(4):
            archivosPDF_2 = [(archivo) for archivo in os.listdir(rutas[i]) if archivo.endswith(".pdf")]
            if file in archivosPDF_2:
                fusionador.append(open(rutas[i]+os.sep+file, 'rb'))
        
        with open(rutas[4]+os.sep+file, 'wb') as salida:
            fusionador.write(salida)
        bar2.next()
    bar2.finish()

    ventanaInfo("ARCHIVOS CREADOS SATISFACTORIAMENTE")

unirPDFsiniestros()