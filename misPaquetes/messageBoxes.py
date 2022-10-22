from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import filedialog as FileDialog
from os import scandir, getcwd, system, listdir, walk
from os.path import isfile, join

#root = Tk()

# SHOWINFO: ventana de dialogo con informacion
def ventanaInfo(msg):
    # MessageBox.showinfo("Informacion", msg)
    None

def ventanaError(msg):
    # MessageBox.showerror("Error", msg)
    None

def ventanaAdvertencia(msg):
    # MessageBox.showwarning("Alerta", msg)
    None

def ventanaPregunta(msg):
    None
    # resultado = MessageBox.askquestion("Salir", msg)

    # if resultado == "yes":
    #     ventanaInfo(msg)
        #root.destroy()  # Destruir, alternativa a quit

def ventanaOkCancelar(msg):
    None
    # resultado = MessageBox.askokcancel("Salir", msg)

    # if resultado == True:
    #     ventanaInfo(msg)
        # Hacer algo

def ventanaReintentarCancelar(msg):
    None
    # resultado = MessageBox.askretrycancel("Reintentar", msg)

    # if resultado == True:
    #     ventanaInfo(msg)
    #     # Hacer algo

def cuadroDialogo(msj="Elija una Carpeta", ruta='.'):
    carpeta = FileDialog.askdirectory(
        title=msj,
        initialdir=ruta,
        )
    return carpeta

# este cuadro de dialogo permite seleccionar una carpeta y retorna su direccion absoluta
def cuadroDialogoGuardarArchivo(msj="Elija una carpeta", tipo='.pdf'):
    rutaArchivo = FileDialog.asksaveasfilename(
        title = msj,
        initialdir = '.',
        defaultextension = tipo,
        )
    return rutaArchivo

def cuadroDialogoAbrirArchivo(msj="Elija una carpeta",tipo=".txt",ruta='.'):
    rutaArchivo = FileDialog.askopenfilename(
        title = msj,
        initialdir = ruta,
        defaultextension = tipo,
        )
    return rutaArchivo
