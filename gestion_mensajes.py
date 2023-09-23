import tkinter as tk


class GestionMensajes:

    #---------Método para regresar a la aplicación---------------
    def Regresar(self):
        self.Ventana.destroy()

    def __init__(self):

        self.Ventana = tk.Toplevel()
        self.Ventana.title("[GESTIÓN DE MENSAJES]")
        self.Ventana.geometry("800x600")
        self.Ventana.configure(bg="#6e44ff")
        self.Ventana.resizable(0,0)

        """ Etiquetas "label """
        title = tk.Label(self.Ventana, text = "Gestión de Mensajes", bg="#6e44ff", fg="white", font=("Poppins", 24)).place(x=20, y=10)

        """ Botones """
        Salir = tk.Button(self.Ventana, text="Regresar",bg="#0cca4a", fg="white", font=("Poppins", 14), command=self.Regresar).place(x=670, y=515)

        self.Ventana.mainloop()