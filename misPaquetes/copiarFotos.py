from misPaquetes.messageBoxes import *
import shutil

from os import walk
import os

""" 
este script permite copiar imagenes de una carpeta a otra segun el registro fotografico llevado por interventoria de 
semaforizacion; se realiza con la necesidad de corregir la manera en que se llevara los registros fotograficos a partir
de septiembre del 2022. solo es util para mover las fotos al nuevo esquema de carpetas, por lo que su ultimo
fue en octubre del 2022
"""

def nombreArchivos(ruta = '.'):
    """
    Genera una lista con las direcciones de las carpetas que ya no tienen subcarpetas, esto con el fin 
    de llegar hasta donde estan los archivos del tipo que se necesite. en mi caso de tipo imagen 
    """
    rutas = []
    Direcciones = []
    numeroEliminar = len(ruta)

    for (dirs, subcapetas, archivos) in walk(ruta):
        if(len(subcapetas) == 0):
            if (dirs.count("Otros")==0) :
                rutas.append(dirs)
            else: continue
                
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
    return Direcciones, rutas, archivos

# caso general de los nombres de carpetas y subcarpetas y archivos
def nombreArchivos2(ruta = '.'):
    rutas = []
    Direcciones = []
    numeroEliminar = len(ruta)

    for (dirs, subcapetas, archivos) in walk(ruta):
        if(len(subcapetas) == 0):
            if (dirs.count("Otros")==0) :
                rutas.append(dirs)
            else: continue

            texto = (dirs[numeroEliminar+1::1].replace("Mantenimiento ",""))
            Direcciones.append(texto)
    return Direcciones, rutas, archivos

def moverFotos(ruta1='.'):
    listas, rutas, _ = nombreArchivos('C:/Users/User/Desktop/jonathan/DIGITALIZACION FOTOS/10. Septiembre 2022')
    listas2, rutas2, _ = nombreArchivos2('C:/Users/User/Desktop/jonathan/DIGITALIZACION FOTOS/10. Septiembre 2022_2')

    for i in range(len(listas)):
        imagenes_jpg = [(rutas[i]+"/"+archivo) for archivo in os.listdir(rutas[i]) if (archivo.endswith(".jpg") or archivo.endswith(".jpeg") or archivo.endswith(".png"))]
        if(len(imagenes_jpg)==0):continue
        [shutil.copy2(img, rutas2[i]) for img in imagenes_jpg]