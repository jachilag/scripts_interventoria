import img2pdf
from os import walk
import os
from misPaquetes.messageBoxes import *

"""
Este script convierte las fotos de seguimiento de interventoria a pdf. Este solo aplica para los meses anteriores a 
septiembre del 2022. despues aplica el script imageToPDF_2.
Se solicita seleccionar la carpeta donde va a guardar los pdf's que se generaran y tambien se solicita seleccionar la 
carpeta donde estan las fotos de seguimiento, en este caso para el antiguo esquema antes de septiembre del 2022
"""

def nombreArchivos(ruta = '.'):
    """ 
    genera una lista con las direcciones de las carpetas qeu ya no tienen subcarpetas, 
    esto con el fin de llegar hasta donde estan los archivos del tipo que se necesite. 
    En este caso, de tipo imagen
    """
    rutas = []
    Direcciones = []
    numeroEliminar = len(ruta)

    for (dirs, subcapetas, archivos) in walk(ruta):
        if(len(subcapetas) == 0):
            rutas.append(dirs)
            texto = (dirs[numeroEliminar+1::1].replace("Mantenimiento ",""))

            if texto.count("Otros")!=0:
                texto = texto.replace("Otros\\","")
                texto = texto.replace("\\"," ")
                texto = texto.replace("_","")

            else:
                texto = texto.replace(" ","")
                texto = texto.replace("\\"," ")
                texto = texto.upper()
                if texto.count("_1") != 0:
                    texto = texto.replace("_1","")
                    texto = texto+"_1"
                if texto.count("_2") != 0:
                    texto = texto.replace("_2","")
                    texto = texto+"_2"

            Direcciones.append(texto)
    return Direcciones, rutas


def imagenToPDF():
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
    for i in range(len(lista)):
        imagenes_jpg = [(rutas[i]+"/"+archivo) for archivo in os.listdir(rutas[i]) if (archivo.endswith(".jpg") or archivo.endswith(".jpeg") or archivo.endswith(".png"))]
        if(len(imagenes_jpg)==0):continue

        with open(ruta2+"/"+lista[i]+".pdf", "wb") as documento:
            documento.write(img2pdf.convert(imagenes_jpg))
    
    MessageBox.showinfo("Informacion", "ARCHIVOS CREADOS SATISFACTORIAMENTE")