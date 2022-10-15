from os import system
from misPaquetes.messageBoxes import *
import misPaquetes.estructura_datos as ed

import misPaquetes.extraerPaginaPDF as extraerPg
import misPaquetes.unirPDFsiniestros as unirPDFsiniestros
import misPaquetes.unirPDFs as unirPDFs
import misPaquetes.imageToPDF_2 as img_PDF_2
import misPaquetes.imageToPDF_1 as img_PDF_1
import misPaquetes.nuevoFormatoFotos as nuevoFotos
import misPaquetes.creacion_carpetas as carpetas 
import misPaquetes.copiarFotos as copiarFotos


def opcion_1():
    extraerPg.separarPDFsiniestros()

def opcion_2():
    unirPDFsiniestros.unirPDFsiniestros()

def opcion_3():
    unirPDFs.unirPDFs()

def opcion_4():
    img_PDF_2.imagenToPDF()

def opcion_5():
    img_PDF_1.imagenToPDF()

def opcion_6():
    nuevoFotos.formatoFotos()

def opcion_7():
    carpetas.crearCarpetasNuevas(cuadroDialogo("seleccione carpeta donde estan los pdfs con los nombres"))

def opcion_8():
    copiarFotos.moverFotos()

def opcion_9():
    print("Aun en etapa de desarrollo :(")

def bloque(opcion,opciones,programa):   #para cada opcion seleccionada se ejecuta el bloque de instrucciones
    system("cls")
    try:
        if opcion != '0':
            extrae = lambda lista: lista[0]
            print(extrae([i for i in opciones if i.find(opcion+'.') != -1]),'\n')
            eval(f'opcion_{str(opcion)}()') #opcion_3()
            #if opcion!= 1: #agregar or ... a esta instruccion en caso que hayan mas submenus
            input("\n\npresione ENTER para continuar")
            programa()
        elif opcion == '0':
            system("cls")
    except:
        print("\nerror\n")
        input("\npresione ENTER para continuar")
        programa()


def programa():
    system('cls')
    print('BIENVENIDO A MIS SCRIPTS PARA INTERVENTORIA \n')
    print('Que accion desea realizar?:\n')
    opciones=[]
    opciones.append("1. Extraer paginas de protocolos.pdf o bitacora.pdf")
    opciones.append("2. Generar archivos COMPILADOS")
    opciones.append("3. Unir todos los PDFs de una carpeta (uso general)")
    opciones.append("4. Pasar fotos a PDF (DESPUES de septiembre 2022)")
    opciones.append("5. Pasar fotos a PDF (ANTES de septiembre 2022)")
    opciones.append("6. Renombrar Fotos en nuevas carpetas")
    opciones.append("7. Crear estructura de carpetas(pasar del anterior al nuevo esquema)")
    opciones.append("8. Mover fotos de estructura antigua a estructura nueva")
    opciones.append("9. Web Scrapping Mantum(para materiales siniestrados)")
    opciones.append("0. SALIR")

    [print(x) for x in opciones]
    opcion = input('\n')
    bloque(opcion, opciones, programa)
        
#PROGRAMA PRINCIPAL
if __name__ == '__main__':
    programa()