import tkinter as tk
from tkinter import messagebox
from linked_lists import lista_drones
from ver_listadron import lista_d

mi_lista = lista_drones()


class GestionDrones:

    #---------Método para regresar a la aplicación---------------
    def Regresar(self):
        self.Ventana.destroy()

    def ver_Listado(self):
        lista_d(self.Dron)
        print(mi_lista.print_drones())

    def graficar_lista(self):
        self.Dron.graficar_drones()
    
    def graficar_sis(self):
        self.Altura.graficar_sistema()
    
    def graficar_contenido(self):
        self.Altura.graficar_alturas()

    def Entry(self): #VENTANITA PARA EL ENTRY
        root = tk.Toplevel(self.Ventana)
        
        Entrada1 = tk.Entry(root, font=("Poppins", 12))
        Entrada1.place(x=100, y=10)
        """ Entrada1.grid(row=0, column=1) """
        Nombre = tk.Label(root,text="Nombre",bg="#DA4167",fg="white", font=("Poppins", 12)).place(x=10, y=10)
        """ Numero.grid(row=0, column=0) """
        root.configure(bg="#DA4167")
        root.geometry("400x150")

        def salir():
            root.destroy()
    
        def agregar_dron():
            try:
                Entradaa1 = str(Entrada1.get())
                self.Dron.insertar_dron(Entradaa1)
                self.Dron.ordenar_alfabeticamente()
                """ print(mi_lista.print_drones()) """
            except ValueError:
                messagebox.showerror()
                
        nota = tk.Label(root, text="Nota: Utiliza solo letras*", bg="#DA4167", fg="white", font=("Poppins", 10)).place(x=100, y=50)
        Agregar1 = tk.Button(root, text="Agregar",bg="#5E6472", fg="white", font=("Poppins", 14), command=agregar_dron).place(x=100, y=80)
        Salir = tk.Button(root, text="Regresar",bg="#5E6472", fg="white", font=("Poppins", 14), command=salir).place(x=200, y=80)
        root.mainloop()

    def __init__(self, Dron, Altura):

        self.Dron = Dron
        self.Altura = Altura
        self.Ventana = tk.Toplevel()
        self.Ventana.title("[GESTIÓN DE DRONES]")
        self.Ventana.geometry("650x200")
        self.Ventana.configure(bg="#DA4167")
        self.Ventana.resizable(0,0)

        """ Etiquetas "label """
        title = tk.Label(self.Ventana, text = "Gestión de Drones", bg="#DA4167", fg="white", font=("Poppins", 24)).place(x=20, y=10)


        """ Botones """
        Salir = tk.Button(self.Ventana, text="Regresar",bg="#5E6472", fg="white", font=("Poppins", 14), command=self.Regresar).place(x=410, y=90)
        listado = tk.Button(self.Ventana, text="Ver listado",bg="#5E6472", fg="white",font=("Poppins", 14), command=self.ver_Listado).place(x=20, y=90)
        agregar = tk.Button(self.Ventana, text="Agregar dron",bg="#5E6472", fg="white",font=("Poppins", 14), command=self.Entry).place(x=150, y=90)
        graficar = tk.Button(self.Ventana, text="Graficar",bg="#5E6472", fg="white",font=("Poppins", 14), command=self.graficar_lista).place(x=302, y=90)
        contenido = tk.Button(self.Ventana, text="Graficar Contenido",bg="#5E6472", fg="white",font=("Poppins", 14), command=self.graficar_contenido).place(x=402, y=90)
        self.Ventana.mainloop()