from os import system

import misPaquetes.imageToPDF_2 as img_PDF_2
import misPaquetes.nuevoFormatoFotos as nuevoFotos



def opcion_1():
    nuevoFotos.formatoFotos()

def opcion_2():
    img_PDF_2.imagenToPDF()

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
    print('MENU FOTOS \n')
    print('Que accion desea realizar?:\n')
    opciones=[]
    opciones.append("1. RENOMBRAR FOTOS PARA SDM")
    opciones.append("2. Pasar fotos a PDF (Modelo desde septiembre 2022)")
    opciones.append("0. SALIR")

    [print(x) for x in opciones]
    opcion = input('\n')
    bloque(opcion, opciones, programa)
        