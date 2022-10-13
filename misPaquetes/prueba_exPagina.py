from estructura_datos import *
from messageBoxes import *
from progress.bar import Bar, ChargingBar
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
import PyPDF2
import os

RUTA_ORIGEN = 'C:/Users/User/Desktop/jonathan/DIGITALIZACION FOTOS/documentos prueba siniestros'+os.sep+'bitacoraMarzo.pdf'
RUTA_DESTINO = 'C:/Users/User/Desktop/jonathan/DIGITALIZACION FOTOS/QUINCENA 2/3. BITACORA'+os.sep
RUTA_TXT = 'C:/Users/User/Desktop/jonathan/DIGITALIZACION FOTOS/QUINCENA 2'+os.sep+'datosOTs.txt'

# RUTA_ORIGEN = 'C:/Users/User/Desktop/jonathan/DIGITALIZACION FOTOS/documentos prueba siniestros'+os.sep+'protocolosMarzo.pdf'
# RUTA_DESTINO = 'C:/Users/User/Desktop/jonathan/DIGITALIZACION FOTOS/QUINCENA 2/2. PROTOCOLOS'+os.sep
# RUTA_TXT = 'C:/Users/User/Desktop/jonathan/DIGITALIZACION FOTOS/QUINCENA 2'+os.sep+'datosOTs.txt'

def separarPDFsiniestros():

    archivoTXT = RUTA_TXT
    if archivoTXT == "":return;
    pdfGeneral = RUTA_ORIGEN
    if pdfGeneral == "":return;
    rutaGuardado = RUTA_DESTINO
    if rutaGuardado == "":return;

    def leerArchivoOTs():
        """ 
        Devuelve un diccionario con los valores de las OTs asociadas a un mismo caso de siniestro
        la llave es el nombre de archivo de salida, y la clave es una lista con las OTs asociadas a su llave 
        """
        with open(archivoTXT,'r',encoding="utf-8") as data:
            datos = data.readlines()

        OTs = []
        NombresSalida = []
        
        for i in datos:
            temp = i.split(",")
            OTs.append(temp[1].replace(chr(10),""))
            NombresSalida.append(temp[2].replace(chr(10),"")) #se elimina el dato salto de linea
        
        return {i:[OTs[j] for j in range(len(OTs)) if NombresSalida[j]==i] for i in unicos(sorted(NombresSalida))}

    def paginasOTs(casosSiniestros):
        """
        funcion que recibe como argumento un diccionario con las claves del nombre de archivo de salida que tendra el PDF,
        y como llaves los valores de las ots correspondientes a dicho caso de sinestro.
        como salida entrega la pagina donde se encuentra dicha ot. si no encuentra una ot, tomara valor de -1 
        """
        paginas = casosSiniestros.copy()
        read_pdf = PyPDF2.PdfFileReader(open(pdfGeneral, 'rb'))

        bar2 = Bar('Buscando Paginas:', max=read_pdf.getNumPages())
        for i in range(read_pdf.getNumPages()):
            texto = (read_pdf.getPage(i)).extractText()
            for k,v in paginas.items():
                for j in range(len(v)):
                    if type(v[j])==int:continue
                    if texto.find(v[j]) >= 0:
                        v[j] = i+1
            bar2.next()
        bar2.finish()
        
        return paginas

    def listaNoEncontrados(paginas):
        """
        funcion que devuelve un diccionario con llave el nombre del archivo salida y
        el valor con un vector con cada uno de las ot que no encontro 
        """
        noEncontrados = paginas.copy()

        # ciclo para dejar solos los no encontrados
        for k,v in noEncontrados.items():
            [v.pop(ot) for ot in range(len(v)-1,-1,-1) if type(v[ot]) == int]
        
        # elimina del diccionario los valores con vectores vacios
        noEncontrados = {k: v for k, v in noEncontrados.items() if v}
        seccionImpresion('-')
        print("NO SE AGREGARON LAS SIGUIENTES OT'S CORRESPONDIENTES A DICHOS CASOS DE SINIESTROS:")
        [print(k,"-",v) for k,v in noEncontrados.items()]
        
    def negativosNoEncontrados(paginas):
        """ 
        recibe un diccionario con llaves los nombres de los archivos de salida, y devuelve
        los valores no encontrados en -1 
        """
        temp = paginas.copy()
        
        # ciclo para dejar en negativo los valores no encontrados y asi la funcion extraer paginas no lo tendra en cuenta
        for k,v in temp.items():
            v = [-1 if type(v[ot]) != int else v[ot] for ot in range(len(v))]
            temp[k] = unicos(v) # deja en cada lista del valor del diccionario, los valores unicos de las paginas
        return temp

    def extraerPaginas(dictPaginas):
        """ 
        funcion que toma como parametro de entrada un diccionario, en donde las llaves contiene los nombres de los
        archivos de salida tipo pdf, y sus valores son las paginas que va a buscar en el archivo fuente de PDF para 
        extraer las paginas y separarlas en archivos de salida. util para protocolos enviados por el contratista y 
        bitacora enviada por movilidad 
        """
        pdf_reader = PdfFileReader(open(pdfGeneral, 'rb'))

        bar2 = Bar('Extrayendo Paginas:', max=len(dictPaginas))
        for k,v in dictPaginas.items():
            if v == [-1]:continue

            pdf_writer = PdfFileWriter()
            [pdf_writer.addPage(pdf_reader.getPage(pg-1)) for pg in v if pg!=-1]

            with open(f'{rutaGuardado}{k}.pdf', 'wb') as doc_file:
                pdf_writer.write(doc_file)

            bar2.next()
        bar2.finish()
            
    salida = paginasOTs(leerArchivoOTs())
    conNegativos = negativosNoEncontrados(salida)
    extraerPaginas(conNegativos)
    listaNoEncontrados(salida)




separarPDFsiniestros()