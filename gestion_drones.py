import tkinter as tk
from tkinter import messagebox
from linked_lists import lista_drones

mi_lista = lista_drones()


class GestionDrones:

    #---------Método para regresar a la aplicación---------------
    def Regresar(self):
        self.Ventana.destroy()

    def ver_Listado(self):
        print(mi_lista.print_drones())

    def Entry(self): #VENTANITA PARA EL ENTRY
        root = tk.Toplevel(self.Ventana)
        
        Entrada1 = tk.Entry(root, font=("Poppins", 12)).place(x=100, y=10)
        """ Entrada1.grid(row=0, column=1) """
        Nombre = tk.Label(root,text="Nombre",bg="#DA4167",fg="white", font=("Poppins", 12)).place(x=10, y=10)
        """ Numero.grid(row=0, column=0) """
        root.configure(bg="#DA4167")
        root.geometry("400x150")
    
        def agregar_dron():
            try:
                Entradaa1 = str(Entrada1.get)
                mi_lista.insertar_dron(Entradaa1)
                print(mi_lista.imprimirTexto())
            except ValueError:
                messagebox.showerror
                
        Agregar1 = tk.Button(root, text="Agregar",bg="#5E6472", fg="white", font=("Poppins", 12), command=agregar_dron).place(x=100, y=60)
        root.mainloop()

    def __init__(self):

        self.Ventana = tk.Toplevel()
        self.Ventana.title("[GESTIÓN DE DRONES]")
        self.Ventana.geometry("800x600")
        self.Ventana.configure(bg="#DA4167")
        self.Ventana.resizable(0,0)

        """ Etiquetas "label """
        title = tk.Label(self.Ventana, text = "Gestión de Drones", bg="#DA4167", fg="white", font=("Poppins", 24)).place(x=20, y=10)


        """ Botones """
        Salir = tk.Button(self.Ventana, text="Regresar",bg="#5E6472", fg="white", font=("Poppins", 14), command=self.Regresar).place(x=670, y=515)
        listado = tk.Button(self.Ventana, text="Ver listado",bg="#5E6472", fg="white",font=("Poppins", 14), command=self.ver_Listado).place(x=20, y=90)
        agregar = tk.Button(self.Ventana, text="Agregar dron",bg="#5E6472", fg="white",font=("Poppins", 14), command=self.Entry).place(x=150, y=90)
        self.Ventana.mainloop()