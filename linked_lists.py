
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

""" Nodo y Lista para Sistemas """
class Sistemas:

    def __init__(self, nombre, altura, cantidad):
        self.nombre = nombre
        self.altura = altura
        self.cantidad = cantidad
        self.siguiente = None

    def verSistemas(self):
        return "Nombre: " + str(self.nombre) + "\n" + "Altura: " + str(self.altura) + "\n" + "Cantidad: " + str(self.cantidad)
    
class lista_sistemas():

    def __init__(self):
        self.cabeza = None

    def insertar_sistema(self, nombre, altura, cantidad):
        nuevo = Sistemas(nombre, altura, cantidad)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            tmp = self.cabeza
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
    
    def print_sistemas(self):
        tmp = self.cabeza
        texto = ""
        while tmp is not None:
            texto += tmp.verSistemas()
            tmp = tmp.siguiente
        return texto
    
""" Nodo y Lista para Contenidos """
class Contenidos:

    def __init__(self, contenido):
        self.contenido = contenido
        self.siguiente = None


    def verContenido(self):
        return "Contenido del dron: " + str(self.contenido)
    
class lista_contenidos():
    
    def __init__(self):
        self.cabeza = None

    def insertar_contenido(self, contenido):
        nuevo = Contenidos(contenido)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            tmp = self.cabeza
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
        
    def print_contenidos(self):
        tmp = self.cabeza
        texto = ""
        while tmp is not None:
            texto += tmp.verContenido()
            tmp = tmp.siguiente
        return texto

""" Nodo y Lista para Alturas """
class Alturas:

    def __init__(self, valor, altura):
        self.valor = valor
        self.altura = altura
        self.siguiente = None

    def verAlturas(self):
        return str(self.valor) + "\n" + "Altura: " + str(self.altura)
    
class lista_alturas():

    def __init__(self):
        self.cabeza = None

    def insertar_alturas(self, valor, altura):
        nuevo = Alturas(valor, altura)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            tmp = self.cabeza
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
        
    def print_alturas(self):
        tmp = self.cabeza
        texto = ""
        while tmp is not None:
            texto += tmp.verAlturas()
            tmp = tmp.siguiente
        return texto


""" Nodo y Lista para Mensajes """
class Mensajes:
    
    def __init__(self, valor, mensaje):
        self.valor = valor
        self.mensaje = mensaje  
        self.siguiente = None

    def verMensajes(self):
        return str(self.valor) + "\n" + str(self.mensaje)
    

class lista_mensajes():

    def __init__(self):
        self.cabeza = None

    def insertar_mensajes(self, valor, mensaje):
        nuevo = Mensajes(valor, mensaje)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            tmp = self.cabeza
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
        
    def print_mensajes(self):
        tmp = self.cabeza
        texto = ""
        while tmp is not None:
            texto += tmp.verMensajes()
            tmp = tmp.siguiente
        return texto


""" Nodo y Lista para Instrucciones """
class Instrucciones:
    
    def __init__(self, valor, instruccion):
        self.valor = valor
        self.instruccion = instruccion  
        self.siguiente = None

    def verInstrucciones(self):
        return str(self.valor) + "\n" + str(self.instruccion)
    

class lista_mensajes():

    def __init__(self):
        self.cabeza = None

    def insertar_instrucciones(self, valor, instruccion):
        nuevo = Instrucciones(valor, instruccion)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            tmp = self.cabeza
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
        
    def print_instruccioes(self):
        tmp = self.cabeza
        texto = ""
        while tmp is not None:
            texto += tmp.verInstrucciones()
            tmp = tmp.siguiente
        return texto