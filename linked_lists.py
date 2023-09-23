
""" Nodo y Lista para Drones """
class Drones:

    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    def verDron(self):
        return "Dron: " + str(self.valor)
    
class lista_drones():

    def __inint__(self):
        self.cabeza = None

    def insertar_dron(self, valor):
        nuevo = Drones(valor)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            tmp = self.cabeza
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
    
    def print_drones(self):
        tmp = self.cabeza
        texto = ""
        while tmp is not None:
            texto += tmp.verDron()
            tmp = tmp.siguiente
        return texto