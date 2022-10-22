from messageBoxes import *
import shutil
from progress.bar import Bar, ChargingBar
from os import walk
import os


""" 
Este script permite pasar las fotos del esquema de carpetas mes -> actividad -> ext ## id ## fecha -> fotos 
al esquema mes -> actividad -> fotos(ext ## id ## fecha), para qeu el ingeniero ricardo patiño le quede
facil la revision de las fotos
"""

def formatoFotos():

    RUTA_ORIGEN = 'C:/Users/User/Desktop/jonathan/DIGITALIZACION FOTOS/10. Septiembre 2022'
    if not RUTA_ORIGEN: 
        print("no se eligió ninguna opcion")
        return

    RUTA_DESTINO = 'C:/Users/User/Desktop/jonathan/DIGITALIZACION FOTOS/10. Septiembre 2022_4'
    if not RUTA_DESTINO: 
        print("no se eligió ninguna opcion")
        return
    

    def creacionCarpetasActividades():
        """ 
        luego de listar los nombres de las carpetas (rutas) esta funcion las creara donde el usuario elija 
        """
        for (dirs, subcapetas, archivos) in walk(RUTA_ORIGEN):
            ACTIVIDADES = subcapetas
            break
        [os.makedirs(RUTA_DESTINO+"/"+r) for r in ACTIVIDADES]


    def nombreArchivos(ruta = '.'):
        """
        Genera una lista con las direcciones de las carpetas que ya no tienen subcarpetas, esto con el fin 
        de llegar hasta donde estan los archivos del tipo que se necesite. en este caso de tipo imagen .jpg
        """
        rutasNombres = []
        nombresDestino = []
        numeroEliminar = len(ruta)
        for (dirs, subcapetas, archivos) in walk(ruta):
            if(len(subcapetas) == 0):
                nombreBase = os.sep + dirs[numeroEliminar+1::1]
                [rutasNombres.append(dirs+os.sep+nom) for nom in archivos if nom.endswith('.jpg')]
                [nombresDestino.append(f'{nombreBase}({i+1})') for i in range(len(archivos)) if archivos[i].endswith('.jpg')]

        return rutasNombres, nombresDestino


    def moverFotos(rutaOrigen, rutaDestino='.'):
        rutasNombres, nombresDestino = nombreArchivos(rutaOrigen)
        ruta2 = rutaDestino
        # ruta2 = cuadroDialogo("seleccione carpeta destino donde guardara las fotos")

        imagenes_destino = [(ruta2+archivo+".jpg") for archivo in nombresDestino]

        # [shutil.copy2(rutasNombres[i], imagenes_destino[i]) for i in range(len(imagenes_destino))]
        bar2 = Bar('Procesando Fotos:', max=len(imagenes_destino))
        for i in range(len(imagenes_destino)):
            shutil.copy2(rutasNombres[i], imagenes_destino[i])
            bar2.next()
        bar2.finish()

    try:
        moverFotos(RUTA_ORIGEN, RUTA_DESTINO)
    except:
        creacionCarpetasActividades()
        moverFotos(RUTA_ORIGEN, RUTA_DESTINO)
    
    ventanaInfo("FOTOS PROCESADAS SATISFACTORIAMENTE")


formatoFotos()