from misPaquetes.messageBoxes import *
from tkinter import *
from tkinter import filedialog as FileDialog
from tkinter import messagebox as MessageBox

import img2pdf
from os import scandir, getcwd, system, listdir, walk, mkdir, makedirs
from os.path import isfile, join
import os
import misPaquetes

"""
Este script es para pasar del antiguo esquema de carpetas al nuevo esquema de carpetas para
el registro fotografico de los seguimientos de interventoria del componente electricos
a partir de septiembre del 2022. ultimo uso octubre del 2022
 """


def listarCarpetasNuevas(ruta1='.'):
    """ 
    Esta funcion crea la lista de las carpetas como van a ser creadas en donde se elija para tal fin.
    Solo se usa para cuando tengamos la estructura de carpetas mes->tipo actividad->ext #### -> ID #### -> imagenes
    La estructura de salida para la creacion de carpetas es: mes->tipo actividad->ext #### ID #### -> fecha (opcional v)
    """
    listaPDF = imagenes_jpg = [archivo for archivo in os.listdir(ruta1) if archivo.endswith(".pdf")]
    for i in range(len(listaPDF)):
        if(listaPDF[i].count("CORRECTIVO_")!=0):
            listaPDF[i]=listaPDF[i].replace("CORRECTIVO_","/Mantenimiento correctivo/")
            
        if(listaPDF[i].count("PREVENTIVO_")!=0):
            listaPDF[i]=listaPDF[i].replace("PREVENTIVO_","/Mantenimiento preventivo/")

        if(listaPDF[i].count("SINIESTRO_")!=0):
            listaPDF[i]=listaPDF[i].replace("SINIESTRO_","/Siniestros/")

        listaPDF[i]=listaPDF[i].replace(".pdf","")
    return listaPDF

def crearCarpetasNuevas(ruta1='.'):
    """ 
    luego de listar los nombres de las carpetas (rutas) esta funcion las creara donde el usuario elija 
    """
    listaPDF = listarCarpetasNuevas(ruta1)
    ruta2 = cuadroDialogo("seleccione carpeta destino donde creara las subcarpetas")
    if not ruta2: 
        print("no se eligió ninguna opcion")
        return
    [os.makedirs(ruta2+r) for r in listaPDF]