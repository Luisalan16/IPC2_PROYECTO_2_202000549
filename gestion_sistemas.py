import tkinter as tk
from tkinter import messagebox
from linked_lists import lista_sistemas
from ver_listadosistemas import lista_sis

mi_lista = lista_sistemas

class GestionSistemas:

    #---------Método para regresar a la aplicación---------------
    def Regresar(self):
        self.Ventana.destroy()

    def ver_Listado(self):
        lista_sis(self.Sistema)
        print(mi_lista.print_sistemas())
        

    def __init__(self, Sistema):

        self.Sistema = Sistema
        self.Ventana = tk.Toplevel()
        self.Ventana.title("[GESTIÓN SISTEMAS DE DRONES]")
        self.Ventana.geometry("800x600")
        self.Ventana.configure(bg="#6e44ff")
        self.Ventana.resizable(0,0)

        """ Etiquetas "label """
        title = tk.Label(self.Ventana, text = "Gestión de sistemas de drones", bg="#6e44ff", fg="white", font=("Poppins", 24)).place(x=20, y=10)

        """ Botones """
        listado = tk.Button(self.Ventana, text="Ver listado",bg="#0cca4a", fg="white",font=("Poppins", 14), command=self.ver_Listado).place(x=20, y=90)
        Salir = tk.Button(self.Ventana, text="Regresar",bg="#0cca4a", fg="white", font=("Poppins", 14), command=self.Regresar).place(x=670, y=515)

        self.Ventana.mainloop()