from misPaquetes.messageBoxes import *

import img2pdf
from os import walk
import os
from progress.bar import Bar, ChargingBar

"""
Este script convierte las fotos de seguimiento de interventoria a pdf. Este solo aplica para cumplir como
lo solicito la SDM con formato a partir de SEPTIEMBRE del 2022.
Se solicita seleccionar la carpeta donde va a guardar los pdf's que se generaran y tambien se solicita seleccionar la 
carpeta donde estan las fotos de seguimiento, en este caso para el antiguo esquema antes de septiembre del 2022
"""

def nombreArchivos(ruta = '.'):
    """
    genera una lista con las direcciones de las carpetas qeu ya no tienen subcarpetas, esto con el fin 
    de llegar hasta donde estan los archivos del tipo que se necesite. en mi caso de tipo imagen
    esta es una solucion especifica de mi funcion y no general.
    """
    rutas = []
    fileName = []
    numeroEliminar = len(ruta)

    for (dirs, subcapetas, _) in walk(ruta):
        if(len(subcapetas) == 0):
            rutas.append(dirs)
            texto = (dirs[numeroEliminar+1::1].replace("Mantenimiento ",""))

            if texto.count("Otros")!=0:
                texto = texto.replace("Otros\\","")
                texto = texto.replace("\\"," ")
                texto = texto.replace("_","")

            else:
                texto = texto.upper()
                texto = texto.replace("EXT ","EXT")
                texto = texto.replace("ID ","ID")
                texto = texto.replace("\\"," ")

            fileName.append(texto)
    return fileName, rutas

def imagenToPDF():
    noGenerados = []
    ruta2 = cuadroDialogo("ELIJA DESTINO DONDE DESEA CREAR LOS ARCHIVOS")
    if not ruta2: 
        print("no se eligió ninguna opcion")
        return
    print(""" seleccione la carpeta donde se encuentra la estructura general de carpetas del registro fotografico mensual: 
    Mantenimiento correctivo
    Mantenimiento preventivo
    Otros
    Siniestros""")
    seleccion = cuadroDialogo("ELIJA CARPETA DONDE ESTAN LAS FOTOS",ruta2)
    if not seleccion: 
        print("no se eligió ninguna opcion")
        return
    lista, rutas = nombreArchivos(seleccion)
    bar2 = Bar('Creando PDFs:', max=len(lista))
    for i in range(len(lista)):
        imagenes_jpg = [(rutas[i]+os.sep+archivo) for archivo in os.listdir(rutas[i]) if (archivo.endswith(".jpg") or archivo.endswith(".jpeg") or archivo.endswith(".png"))]
        if(len(imagenes_jpg)==0):continue

        with open(ruta2+os.sep+lista[i]+".pdf", "wb") as documento:
            documento.write(img2pdf.convert(imagenes_jpg))
        bar2.next()
    bar2.finish()

    if (len(noGenerados)!=0):
        print("\nLos siguientes archivos no se generaron: \n")
        [print(nombre) for nombre in noGenerados]
    
    ventanaInfo("ARCHIVOS CREADOS SATISFACTORIAMENTE")