from os import system
from misPaquetes.messageBoxes import *
import misPaquetes.copiarFotos as copiarFotos
import misPaquetes.imageToPDF_1 as img_PDF_1
import misPaquetes.creacion_carpetas as carpetas 

def opcion_1():
    carpetas.crearCarpetasNuevas(cuadroDialogo("seleccione carpeta donde estan los pdfs con los nombres"))

def opcion_2():
    img_PDF_1.imagenToPDF()

def opcion_3():
    copiarFotos.moverFotos()

def bloque(opcion,opciones,programa):   #para cada opcion seleccionada se ejecuta el bloque de instrucciones
    system("cls")
    try:
        if opcion != '0':
            extrae = lambda lista: lista[0]
            print(extrae([i for i in opciones if i.find(opcion+'.') != -1]),'\n')
            eval(f'opcion_{str(opcion)}()') 
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
    print('MENU OTROS\n')
    print('Que accion desea realizar?:\n')
    opciones=[]
    opciones.append("1. Crear estructura de carpetas(pasar del anterior al nuevo esquema)")
    opciones.append("2. Pasar fotos a PDF (ANTES de septiembre 2022)")
    opciones.append("3. Mover fotos de estructura antigua a estructura nueva")
    opciones.append("0. SALIR")

    [print(x) for x in opciones]
    opcion = input('\n')
    bloque(opcion, opciones, programa)