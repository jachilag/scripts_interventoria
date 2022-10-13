from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import filedialog as FileDialog
from os import scandir, getcwd, system, listdir, walk
from os.path import isfile, join

#root = Tk()

# SHOWINFO: ventana de dialogo con informacion
def ventanaInfo(msg):
    MessageBox.showinfo("Informacion", msg)

def ventanaError(msg):
    MessageBox.showerror("Error", msg)

def ventanaAdvertencia(msg):
    MessageBox.showwarning("Alerta", msg)

def ventanaPregunta(msg):
    resultado = MessageBox.askquestion("Salir", msg)

    if resultado == "yes":
        ventanaInfo(msg)
        #root.destroy()  # Destruir, alternativa a quit

def ventanaOkCancelar(msg):
    resultado = MessageBox.askokcancel("Salir", msg)

    if resultado == True:
        ventanaInfo(msg)
        # Hacer algo

def ventanaReintentarCancelar(msg):
    resultado = MessageBox.askretrycancel("Reintentar", msg)

    if resultado == True:
        ventanaInfo(msg)
        # Hacer algo

def cuadroDialogo(msj="Elija una Carpeta", ruta='././'):
    carpeta = FileDialog.askdirectory(
        title=msj,
        initialdir=ruta,
        # initialdir='C:/',
        )
    return carpeta

# este cuadro de dialogo permite seleccionar una carpeta y retorna su direccion absoluta
def cuadroDialogoGuardarArchivo(msj="Elija una carpeta", tipo='.pdf'):
    rutaArchivo = FileDialog.asksaveasfilename(
        title = msj,
        initialdir = 'C:/',
        defaultextension = tipo,
        )
    return rutaArchivo

def cuadroDialogoAbrirArchivo(msj="Elija una carpeta",tipo=".txt"):
    rutaArchivo = FileDialog.askopenfilename(
        title = msj,
        initialdir = 'C:/',
        defaultextension = tipo,
        )
    return rutaArchivo
