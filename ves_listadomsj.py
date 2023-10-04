import tkinter as tk
from tkinter import *


class lista_msjs():

    def regresar(self):
        self.Ventana.destroy()

    def __init__(self, Mensaje):

        self.Mensaje = Mensaje
        self.Ventana = tk.Toplevel()
        self.Ventana.title("Lista")
        self.Ventana.geometry("600x400")
        self.Ventana.configure(bg="#6e44ff")
        self.Ventana.resizable(0,0)

        #-------------Etiquetas--------------------
        titulo = tk.Label(self.Ventana, text="Mensajes cargados",fg="white",bg="#6e44ff", font=("Poppins", 24)).place(x=20, y=10)

        scrollbar = Scrollbar(self.Ventana)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.Txt=tk.Text(self.Ventana, width="50", height="10", yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.Txt.yview)
        
        
        self.Txt.insert("1.0", self.Mensaje.print_mensajes())
        self.Txt.place(x=20, y=100)

        #-------------Botones--------------------
        Regresar = tk.Button(self.Ventana, text="Regresar",bg="#0cca4a", fg="white", font=("Poppins", 14), command=self.regresar).place(x=20, y=300)
        """ Graficar = tk.Button(self.Ventana, text="Graficar",bg="#0cca4a", fg="white", font=("Poppins", 14), command=self.graficar).place(x=150, y=300) """
        self.Ventana.mainloop()