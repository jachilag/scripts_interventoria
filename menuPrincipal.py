from os import system

from menuSiniestros import programa as menuSiniestros
from menuFotos import programa as menuFotos
from menuOtros import programa as menuOtros


def opcion_1():
    menuFotos()

def opcion_2():
    menuSiniestros()

def opcion_3():
    menuOtros()

def bloque(opcion,opciones,programa):   #para cada opcion seleccionada se ejecuta el bloque de instrucciones
    system("cls")
    try:
        if opcion != '0':
            extrae = lambda lista: lista[0]
            print(extrae([i for i in opciones if i.find(opcion+'.') != -1]),'\n')
            eval(f'opcion_{str(opcion)}()') 
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
    opciones.append("1. MENU FOTOS INTERVENTORIA")
    opciones.append("2. MENU SINIESTROS")
    opciones.append("3. MENU OTROS")
    opciones.append("0. SALIR")

    [print(x) for x in opciones]
    opcion = input('\n')
    bloque(opcion, opciones, programa)
        
#PROGRAMA PRINCIPAL
if __name__ == '__main__':
    programa()