#funcion que elimina los simbolos no deseados, y convierte todos los textos en minusculas
def Normalizacion_datos(lista_texto, simbolos = ['-','¿','?','.',',','¡','!',':','"']):
    #['-','¿','?','.',',','¡','!',':','"']              #simbolos a eliminar del texto
    datos = []                                          #lista que contiene los datos de salida
    for palabra in lista_texto:                         #recorrer cada palabra de lista_texto
        cadena = palabra.lower()                        #colocar todo en minuscula
        for simbolo in simbolos:                        #recorre la lista de simbolos
            if simbolo in palabra:                      #compara si hay simbolos en cada palabra
                cadena = cadena.replace(simbolo,'')     #si hay simbolos los elimina
        datos.append(cadena)                            #agrega la palabra normalizada a la lista 'datos'
    return datos 


#funcion que devuelve los valores unicos de una lista, cadena, tupla, entero o float
def unicos(entrada):                    
    tipo = type(entrada)                #determina el tipo de dato del parametro de entrada
    if tipo == str:                     #si el tipo de dato es string, salida es de tipo string
        salida = ''
    elif tipo == list or tipo == tuple: #si el tipo de dato es lista o tupla, salida es de tipo lista
        salida = []
    elif tipo == int or tipo == float:  #si el tipo de dato es entero o flotante, salida es de tipo string
        entrada = str(entrada)          #convierte tipo numerico a string
        salida = ''
    else:
        print('esta funcion no aplica para ese tipo de datos')
        return None

    for i in range(len(entrada)):                           #recorre cada elemento de la entrada    
        if entrada[:i].count(entrada[i]) == 0:              #si no encuentra otro valor anteriormente...
            if tipo == str or tipo == int or tipo == float: #si es de tipo string entero o float...
                salida += entrada[i]                        #...agrega dicho valor a string salida
            elif tipo == list or tipo == tuple:             #si es de tipo lista o tupla....
                salida.append(entrada[i])                   #...agrega dato a lista salida
            else:
                None

    numero = lambda x: float(x) if tipo == float else int(x)    #funcion anonima que convierte string a entero o flotante
    return numero(salida) if tipo == int or tipo == float else salida   #Devuelve lista 'salida' con los valores unicos


# recibe lista y devuelve diccionario: Las llaves son los datos
# y los valores son las veces que encuentra esos datos en la lista
def conteo_palabras(lista):             
    listaUnicos = unicos(lista)     #llama funcion unicos 
    diccionario = {}                #diccionarip vacio de salida
    for palabra in listaUnicos:     #recoore lista de unicos
        diccionario.update({palabra: lista.count(palabra)}) #agrega item a diccionario 
    return diccionario              #retorna diccionario


# Funcion que recibe un diccionario y devuelve una lista de sublistas de par de elementos: clave,valor.
# De la lista resultante la organiza de mayor a menor y solo se sacan los primeros n datos que se le 
# indiquen en el parametro 'top'
def seleccionar_top(diccionario, top = 0):          
    lista = [[k,v] for k,v in diccionario.items()]      #crea la lista apartir del diccionario
    ordenados = sorted(lista, key=lambda frecuencia: frecuencia[1], reverse=True)   #ordena descendente la lista apartir del segundo elemento de la sublista (clave) 
    return [ordenados[i] for i in range(20)]            #devuelve los primeros 20 datos de la lista

def seccionImpresion(caracter, repeticion=70):
    salida = ""
    print("\n"+salida.center(repeticion,caracter)+"\n")

