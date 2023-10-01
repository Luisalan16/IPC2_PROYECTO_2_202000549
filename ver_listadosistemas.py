import tkinter as tk
from tkinter import *
from linked_lists import lista_mensajes


class lista_sis():

    def regresar(self):
        self.Ventana.destroy()

    def graficar(self):
        self.Sistema.gaficar_sistemas()

    def __init__(self, Sistema):

        self.Sistema = Sistema
        self.Ventana = tk.Toplevel()
        self.Ventana.title("Lista")
        self.Ventana.geometry("600x400")
        self.Ventana.configure(bg="#6e44ff")
        self.Ventana.resizable(0,0)

        #-------------Etiquetas--------------------
        """ img = tk.PhotoImage(file=".\Iconos\checklist.png") """
        titulo = tk.Label(self.Ventana, text="Sistemas cargados",fg="white",bg="#6e44ff", font=("Poppins", 24)).place(x=20, y=10)
        """ logo = tk.Label(self.Ventana,bg="#DA4167", image=img).place(x=400, y=10) """
        

        scrollbar = Scrollbar(self.Ventana)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.Txt=tk.Text(self.Ventana, width="50", height="10", yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.Txt.yview)
        
        
        self.Txt.insert("1.0", self.Sistema.print_sistemas())
        self.Txt.place(x=20, y=100)

        #-------------Botones--------------------
        Regresar = tk.Button(self.Ventana, text="Regresar",bg="#0cca4a", fg="white", font=("Poppins", 14), command=self.regresar).place(x=20, y=300)
        Graficar = tk.Button(self.Ventana, text="Graficar",bg="#0cca4a", fg="white", font=("Poppins", 14), command=self.graficar).place(x=80, y=300)
        self.Ventana.mainloop()

