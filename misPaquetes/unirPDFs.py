from misPaquetes.messageBoxes import*
from PyPDF2 import PdfFileMerger

import os
from os import walk

""" CASO DE USO GENERAL: este script es para unir los pdfs que se encuentren en una carpeta seleccionada y luego
guardar un archivo de salida en una carpeta seleccionada con un nombre de archivo especificado"""


def rutaArchivos(ruta = '.'):
    """ 
    genera una lista con las direcciones de las carpetas que ya no tienen subcarpetas, 
    esto con el fin de llegar hasta donde estan
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

def unirPDFs():
    ruta = cuadroDialogo("ELIJA CARPETA DONDE ESTAN LOS ARCHIVOS PDF")
    if not ruta: 
        print("no se eligió ninguna opcion")
        return
    archivosPDF = [(ruta+"/"+archivo) for archivo in os.listdir(ruta) if archivo.endswith(".pdf")]
    rutaSalida = cuadroDialogoGuardarArchivo("GUARDAR ARCHIVO FINAL COMO",ruta)
    fusionador = PdfFileMerger()
    
    for file in archivosPDF:
        pdfs = []
        fusionador.append(open(file, 'rb'))

    with open(rutaSalida, 'wb') as salida:
        fusionador.write(salida)

    ventanaInfo("ARCHIVO CREADO SATISFACTORIAMENTE")