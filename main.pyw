#################### Bloc de Notas con Python ######################

from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import font
import os
from tkinter.filedialog import *

#---------- Funciones para el manejo de archivos ---------------

def nuevo_archivo(event=None):
    
    root.title("Sin título")
    area_texto.delete(1.0, END)

def abrir_archivo():
    
    archivo=askopenfilename(defaultextension=".txt", file=[("Todos los archivos", "*.*"), ("archivos de texto", "*.txt")])

    try:
        root.title(os.path.basename(archivo))
        area_texto.delete(1.0, END)
        archivo=open(archivo, "r")
        area_texto.insert(1.0, archivo.read())
    except Exception:
        messagebox.showerror(message="No se puede abrir el archivo")
    finally:
        archivo.close()

def guardar_archivo(event=None):
    
    archivo=asksaveasfilename(defaultextension=".txt", file=[("Todos los archivos", "*.*"), ("archivos de texto", "*.txt")])
   
    try:
        root.title(os.path.basename(archivo))
        archivo=open(archivo, "w")
        archivo.write(area_texto.get(1.0, END))
    except Exception:
        messagebox.showerror(message="No se puede guardar el archivo")
    finally:
        archivo.close()

def cerrar_archivo(event=None):
    
    if (root.title()=="Block de Notas" or root.title()=="Sin título"):
        pregunta=messagebox.askquestion(message="Cerrar sin guardar?")
        print(pregunta)
        if pregunta=="yes": 
            area_texto.delete(1.0, END)
    else:
        area_texto.delete(1.0, END)


#----------- Funciones de edición -------------------------------

def copiar(event=None):
    
    area_texto.event_generate("<<Copy>>")

def cortar(event=None):

    area_texto.event_generate("<<Cut>>")

def pegar(event=None):

    area_texto.event_generate("<<Paste>>")

#----------- Funciones para el manejo de fuentes ----------------

def cambiar_color():
    
    color=colorchooser.askcolor(title="Seleciona el color de la fuente")
    area_texto.config(fg=color[1])

def cambiar_fuente(*args):
    
    area_texto.config(font=(fuente.get(), tamanno.get()))

#----------- Otras funciones --------------------------------------

def salir(event=None):
    
    root.destroy()

def ayuda():
    
    messagebox.showinfo("Block de notas", "Con este Block de Notas puedes:\n"
    "-Escribir texto\n"
    "-Editarlo\n"
    "-Guardarlo\n"
    "-Cambiar el color y\n" 
    " tamaño de la fuente")


def acerca_de():
    messagebox.showinfo("Block de Notas", "Block de Notas de uso libre\nVersión 1.0.0")

#----------- Fin de las  funciones ---------------------------------

#----------- Interfaz gráfica --------------------------------------

root=Tk()
root.title("Block de Notas")
root.geometry("500x500")
frame_selectores=Frame(root)

fuente=StringVar(root)
fuente.set("Arial")

t_fuente=StringVar(root)
t_fuente.set(15)

barraMenu=Menu()

#----------- Menú archivo -------------------------------------------

menu_archivo=Menu(barraMenu, tearoff=False)

menu_archivo.add_command(label="Nuevo", accelerator="Ctrl+N", command=lambda:nuevo_archivo())
root.bind_all("<Control-n>", nuevo_archivo)

menu_archivo.add_command(label="Abrir", accelerator="Ctrl+A", command=lambda:abrir_archivo())
root.bind_all("<Control-a>", abrir_archivo)

menu_archivo.add_command(label="Guardar", accelerator="Ctrl+G", command=lambda:guardar_archivo())
root.bind_all("<Control-g>", guardar_archivo)

menu_archivo.add_command(label="cerrar", accelerator="Ctrl+W", command=lambda:cerrar_archivo())
root.bind_all("<Control-w>", cerrar_archivo)

menu_archivo.add_separator()

menu_archivo.add_command(label="Salir", accelerator="Ctrl+S", command=salir)
root.bind_all("<Control-s>", salir)

barraMenu.add_cascade(menu=menu_archivo, label="Archivo")

#---------- Menú editar -----------------------------------------

menu_editar=Menu(barraMenu, tearoff=False)

menu_editar.add_command(label="Copiar", accelerator="Ctrl+C", command=copiar)
root.bind_all("<Control-c>", copiar)

menu_editar.add_command(label="Cortar", accelerator="Ctrl+X", command=cortar)
root.bind_all("<Control-x>", cortar)

menu_editar.add_command(label="Pegar", accelerator="Ctrl+P", command=pegar)
root.bind_all("<Control-p>", pegar)

barraMenu.add_cascade(menu=menu_editar, label="Editar")

#----------- Menú ayuda -------------------------------------------

menu_ayuda=Menu(barraMenu, tearoff=False)

menu_ayuda.add_command(label="Ayuda", command=ayuda)
menu_ayuda.add_command(label="Acerca de...", command=acerca_de)

barraMenu.add_cascade(menu=menu_ayuda, label="Ayuda")

root.config(menu=barraMenu)

#----------- Opciones de fuente -----------------------------------


color=Button(frame_selectores, text="Color", command=cambiar_color)
color.grid(row=0, column=0)

selec_fuente=OptionMenu(frame_selectores, fuente, *font.families(), command=cambiar_fuente)
selec_fuente.grid(row=0, column=1)

tamanno=Spinbox(frame_selectores, from_=1, to=100, textvariable=t_fuente, command=cambiar_fuente)
tamanno.grid(row=0, column=2)

frame_selectores.pack()

#----------- Área de texto ----------------------------------------

area_texto=Text(root)

barra_scroll=Scrollbar(area_texto)
barra_scroll.pack(side=RIGHT, fill=Y)
barra_scroll.config(command=area_texto.yview)

area_texto.config(yscrollcommand=barra_scroll.set)
area_texto.pack(side=LEFT, fill="both", expand=True)

root.mainloop()
