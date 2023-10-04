import tkinter as tk
from tkinter import *
from tkinter import messagebox, PhotoImage
import xml.etree.ElementTree as ET
from lectura import lectura, generar_xml
from gestion_drones import GestionDrones
from gestion_sistemas import GestionSistemas
from gestion_mensajes import GestionMensajes
from linked_lists import lista_drones, lista_sistemas, lista_alturas, lista_contenidos, lista_mensajes, lista_instrucciones


Drones = lista_drones()
Sistemas = lista_sistemas()
Contenidos = lista_contenidos()
Alturas = lista_alturas()
Mensajes = lista_mensajes()
Instrucciones = lista_instrucciones()






class app:

    #-------------Ventana Gestion Drones--------------------
    def GestionDron(self):
        GestionDrones(Drones, Alturas)
    
    #-------------Ventana Gestion Mensajes--------------------
    def GestionMsj(self):
        GestionMensajes(Mensajes, Instrucciones)

     #-------------Ventana Gestion Mensajes--------------------
    def GestionSistemasDrones(self):
        GestionSistemas(Sistemas)
    
     #-------------Ventana Gestion Mensajes--------------------
    def xml_file(self):
        generar_xml(Drones, Sistemas, Mensajes)

    #---------Método para salir de la aplicación--------------
    def Salir(self):
        opcion = messagebox.askquestion("Salir","¿Deseas salir del Menú?")
        if opcion =="yes":
            self.Ventana.destroy()

    #-------------Método para cargar archivos-----------------
    def CargarArchivo(self):
        lectura(Drones, Sistemas, Contenidos, Alturas, Mensajes, Instrucciones)
        
        drones = tk.Button(self.Ventana, text = "Gestion Drones", bg="#5e6472", fg="white", font=("Poppins", 14), command=self.GestionDron, state=NORMAL).place(x=600, y=90)
        sistemas = tk.Button(self.Ventana, text = "Gestion Sistemas", bg="#5e6472", fg="white", font=("Poppins", 14), command=self.GestionSistemasDrones).place(x=600, y=170)
        mensajes = tk.Button(self.Ventana, text = "Gestion Mensajes", bg="#5e6472", fg="white", font=("Poppins", 14), command=self.GestionMsj, state=NORMAL).place(x=600, y=250)
        generar = tk.Button(self.Ventana, text="Generar archivo",bg="#5e6472",fg="white", font=("Poppins", 14), command=self.xml_file, state=NORMAL).place(x=600, y=330)

    """ Aquí empieza mi ventana principal """
    def __init__(self):

        self.Ventana = tk.Tk()
        self.Ventana.title("[PROYECTO 2 | IPC2]")
        self.Ventana.geometry("800x600")
        self.Ventana.configure(bg="#5e6472")
        self.Ventana.resizable(0,0)
        

        """ Etiquetas "label """
        title = tk.Label(self.Ventana, text = "MINISTERIO DE LA DEFENSA DE GUATEMALA", bg="#5e6472", fg="white", font=("Poppins", 24)).place(x=20, y=10)
        img = tk.PhotoImage(file=".\iconos\zumbido.png")
        logo = tk.Label(self.Ventana,  image=img,bg="#5e6472").place(x=100, y=100)
        img2 = tk.PhotoImage(file=".\iconos\guatemala.png")
        logo2 = tk.Label(self.Ventana,  image=img2,bg="#5e6472").place(x=700, y=5)

        
        """ Botones """
        Salir = tk.Button(self.Ventana, text="Salir",bg="#5e6472", fg="white", font=("Poppins", 14), command=self.Salir).place(x=730, y=515)
        Cargar = tk.Button(self.Ventana, text="Cargar Archivo",bg="#5e6472",fg="white", font=("Poppins", 14), command=self.CargarArchivo).place(x=30, y=90)
        drones = tk.Button(self.Ventana, text = "Gestion Drones", bg="#5e6472", fg="white", font=("Poppins", 14), command=self.GestionDron, state=DISABLED).place(x=600, y=90)
        sistemas = tk.Button(self.Ventana, text = "Gestion Sistemas", bg="#5e6472", fg="white", font=("Poppins", 14),command=self.GestionSistemasDrones, state=DISABLED).place(x=600, y=170)
        mensajes = tk.Button(self.Ventana, text = "Gestion Mensajes", bg="#5e6472", fg="white", font=("Poppins", 14), command=self.GestionMsj, state=DISABLED).place(x=600, y=250)
        Ayuda = tk.Button(self.Ventana, text="Ayuda",bg="#5e6472",fg="white", font=("Poppins", 14), command=self.Txt).place(x=600, y=410)
        generar = tk.Button(self.Ventana, text="Generar archivo",bg="#5e6472",fg="white", font=("Poppins", 14), command=self.xml_file, state=DISABLED).place(x=600, y=330)
        """ Para que todo sea visible """
        self.Ventana.mainloop()

    def Txt(self):
        txt = """
        PROYECTO 2 | IPC2 | 202000549

        LINK DEL REPOSITORIO:
        -> https://github.com/Luisalan16/IPC2_PROYECTO_2_202000549/tree/master

        LINK DRIVE:
        -> https://drive.google.com/drive/folders/1OOFc9fd4TtNlrQH_DqZFZW__b6ZkT_dK?usp=share_link
        """
        Link = open("./Extra/Autor_202000549.txt","w+")
        Link.write(txt)
        Link.close()
        messagebox.showinfo(message="Archivo Creado!, Revise la carpeta 'Extra'", title="Información")
        print("Archivo con datos del autor creado exitosamente!")
