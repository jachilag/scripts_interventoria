from os import system

import misPaquetes.extraerPaginaPDF as extraerPg
import misPaquetes.unirPDFsiniestros as unirPDFsiniestros
import misPaquetes.unirPDFs as unirPDFs


def opcion_1():
    extraerPg.separarPDFsiniestros()

def opcion_2():
    unirPDFsiniestros.unirPDFsiniestros()

def opcion_3():
    unirPDFs.unirPDFs()

def opcion_4():
    print("Aun en etapa de desarrollo :(")

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
    print('MENU SINIESTROS \n')
    print('Que accion desea realizar?:\n')
    opciones=[]
    opciones.append("1. Extraer paginas de protocolos.pdf o bitacora.pdf")
    opciones.append("2. Generar archivos COMPILADOS")
    opciones.append("3. Unir todos los PDFs de una carpeta (uso general)")
    opciones.append("4. Web Scrapping Mantum(para materiales siniestrados)")
    opciones.append("0. SALIR")

    [print(x) for x in opciones]
    opcion = input('\n')
    bloque(opcion, opciones, programa)