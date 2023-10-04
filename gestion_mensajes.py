import tkinter as tk
from tkinter import *
from linked_lists import lista_mensajes
from ves_listadomsj import lista_msjs


mi_lista = lista_mensajes()


class GestionMensajes:

    #---------Método para regresar a la aplicación---------------
    def Regresar(self):
        self.Ventana.destroy()

    def graficar_lista(self):
        self.Instrucciones.graficar_instrucciones()

    def ver_Listado(self):
        lista_msjs(self.Mensaje)
        print(mi_lista.print_mensajes())

    def __init__(self, Mensaje, Instrucciones):

        self.Mensaje = Mensaje
        self.Instrucciones = Instrucciones
        self.Ventana = tk.Toplevel()
        self.Ventana.title("[GESTIÓN DE MENSAJES]")
        self.Ventana.geometry("400x200")
        self.Ventana.configure(bg="#6e44ff")
        self.Ventana.resizable(0,0)

        """ Etiquetas "label """
        title = tk.Label(self.Ventana, text = "Gestión de Mensajes", bg="#6e44ff", fg="white", font=("Poppins", 24)).place(x=20, y=10)

        """ Botones """
        listado = tk.Button(self.Ventana, text="Ver listado",bg="#0cca4a", fg="white",font=("Poppins", 14), command=self.ver_Listado).place(x=20, y=90)
        Salir = tk.Button(self.Ventana, text="Regresar",bg="#0cca4a", fg="white", font=("Poppins", 14), command=self.Regresar).place(x=150, y=90)
        graficar = tk.Button(self.Ventana, text="Ver Grafica",bg="#0cca4a", fg="white",font=("Poppins", 14), command=self.graficar_lista).place(x=280, y=90)


        self.Ventana.mainloop()