import tkinter as tk
from tkinter import messagebox, PhotoImage
import xml.etree.ElementTree as ET
from lectura import lectura
from gestion_drones import GestionDrones


""" Dron = lista_drones() """






class app:

     #-------------Ventana Gestion Maquinas--------------------
    def GestionDrones(self):
        GestionDrones(""" Drones """)

     #---------Método para salir de la aplicación--------------
    def Salir(self):
        opcion = messagebox.askquestion("Salir","¿Deseas salir del Menú?")
        if opcion =="yes":
            self.Ventana.destroy()

    #-------------Método para cargar archivos-----------------
    def CargarArchivo(self):
        lectura(""" Drones, Sistemas, Mensajes """)
        
        drones = tk.Button(self.Ventana, text = "Gestion Drones", bg="#ffa69e", fg="black", font=("Poppins", 14)).place(x=500, y=70)
        sistemas = tk.Button(self.Ventana, text = "Gestion Sistemas", bg="#ffa69e", fg="black", font=("Poppins", 14)).place(x=500, y=130)
        mensajes = tk.Button(self.Ventana, text = "Gestion Mensajes", bg="#ffa69e", fg="black", font=("Poppins", 14)).place(x=500, y=180)


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
        drones = tk.Button(self.Ventana, text = "Gestion Drones", bg="#5e6472", fg="white", font=("Poppins", 14)).place(x=600, y=90)
        sistemas = tk.Button(self.Ventana, text = "Gestion Sistemas", bg="#5e6472", fg="white", font=("Poppins", 14)).place(x=600, y=170)
        mensajes = tk.Button(self.Ventana, text = "Gestion Mensajes", bg="#5e6472", fg="white", font=("Poppins", 14)).place(x=600, y=250)

        """ Para que todo sea visible """
        self.Ventana.mainloop()