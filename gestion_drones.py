import tkinter as tk


class GestionDrones:

    #---------Método para regresar a la aplicación---------------
    def Regresar(self):
        self.Ventana.destroy()

    def __init__(self, Dron, Sistemas, Contenido, Alturas, Mensajes, Instrucciones):

        self.Ventana = tk.Toplevel()
        self.Ventana.title("[GESTIÓN DE DRONES]")
        self.Ventana.geometry("750x600")
        self.Ventana.configure(bg="#5e6472")
        self.Ventana.resizable(0,0)


        self.Ventana.mainloop()