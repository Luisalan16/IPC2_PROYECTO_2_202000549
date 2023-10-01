import tkinter as tk
from tkinter import *

class lista_d():

 #---------Método para regresar a la aplicación---------------
    def regresar(self):
        self.Ventana.destroy()
    #------------------------------------------------------------
    
    def __init__(self, Dron):
        
        self.Ventana = tk.Toplevel()
        self.Ventana.title("Lista")
        self.Ventana.geometry("600x400")
        self.Ventana.configure(bg="#DA4167")
        self.Ventana.resizable(0,0)

        #-------------Etiquetas--------------------
        """ img = tk.PhotoImage(file=".\Iconos\checklist.png") """
        titulo = tk.Label(self.Ventana, text="Drones cargados",fg="white",bg="#DA4167", font=("Poppins", 24)).place(x=20, y=10)
        """ logo = tk.Label(self.Ventana,bg="#DA4167", image=img).place(x=400, y=10) """
        

        scrollbar = Scrollbar(self.Ventana)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.Txt=tk.Text(self.Ventana, width="50", height="10", yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.Txt.yview)
        
        
        self.Txt.insert("1.0", Dron.print_drones())
        self.Txt.place(x=20, y=100)

        #-------------Botones--------------------
        Regresar = tk.Button(self.Ventana, text="Regresar",bg="#5e6472", fg="white", font=("Poppins", 14), command=self.regresar).place(x=20, y=300)
        self.Ventana.mainloop()