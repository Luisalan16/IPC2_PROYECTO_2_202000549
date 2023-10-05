import graphviz
""" Nodo y Lista para Drones """
class Drones:

    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    def verDron(self):
        return  str(self.valor) + "\n"
    
class lista_drones():

    def __init__(self):
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
        contador = 1
        while tmp is not None:
            texto += f'{contador}. {tmp.verDron()}'
            tmp = tmp.siguiente
            contador += 1
        return texto
    
    def graficar_drones(self):
        dot = graphviz.Digraph('ListaDrones')
        tmp = self.cabeza

        # Crear un label en formato HTML para representar una tabla
        label = "<<TABLE BORDER='1' CELLBORDER='1' CELLSPACING='0' CELLPADDING='4'>"
        
        while tmp is not None:
            # Agregar una fila a la tabla para cada dron
            label += f"<TR><TD>{tmp.verDron()}</TD></TR>"
            tmp = tmp.siguiente
        
        label += "</TABLE>>"
        
        # Crear un nodo con el label de la tabla
        dot.node('tabla', label=label, shape='plaintext')
        
        # Renderizar y mostrar el gráfico
        dot.render('Lista_drones', format='png', view=True)



    def ordenar_alfabeticamente(self):
        if self.cabeza is None:
            return
        
        sorted = False
        while not sorted:
            sorted = True
            current = self.cabeza
            while current.siguiente is not None:
                if current.valor > current.siguiente.valor:
                    current.valor, current.siguiente.valor = current.siguiente.valor, current.valor
                    sorted = False
                current = current.siguiente
   


""" Nodo y Lista para Sistemas """
class Sistemas:

    def __init__(self, nombre, altura, cantidad):
        self.nombre = nombre
        self.altura = altura
        self.cantidad = cantidad
        self.siguiente = None

    def verSistemas(self):
        return "Nombre: " + str(self.nombre) +";" + "\t" + "Altura: " + str(self.altura) +";" + "\t" + "Cantidad: " + str(self.cantidad) + "\n"
    
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
        contador = 1
        while tmp is not None:
            texto += f'{contador}. {tmp.verSistemas()}'
            tmp = tmp.siguiente
            contador += 1
        return texto
    

    def graficar_sistemas(self):
        dot = graphviz.Digraph('ListaSistemas')
        tmp = self.cabeza
        contador = 1

        while tmp is not None:
            # Crear un label en formato HTML para representar una tabla
            label = f'<<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0">'
            label += f'<TR><TD COLSPAN="2" BGCOLOR="lightgray">{tmp.nombre}</TD></TR>'  # Nombre del sistema
            label += f'<TR><TD>Altura Máxima: {tmp.altura}</TD></TR>'
            label += f'<TR><TD>Cantidad de Drones: {tmp.cantidad}</TD></TR>'
            label += '</TABLE>>'

            dot.node(f'{contador}', label=label, shape='plaintext')
            if tmp.siguiente is not None:
                dot.edge(f'{contador}', f'{contador+1}')
            tmp = tmp.siguiente
            contador += 1

        dot.render('Lista_sistemas', format='png', view=True)

    
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
        self.valor = None

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

    def __init__(self, valor, altura, nombre):
        self.valor = valor
        self.altura = altura
        self.nombre = nombre
        self.siguiente = None

    def verAlturas(self):
        return str(self.valor) + "\n" + "Altura: " + str(self.altura) + "\n" + str(self.nombre) + "\n"
    
    def vercont(self):
        return str(self.nombre) + "\n" + str(self.altura)
    
class lista_alturas():

    def __init__(self):
        self.cabeza = None

    def insertar_alturas(self, valor, altura, nombre):
        nuevo = Alturas(valor, altura, nombre)
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

    def graficar_alturas(self):
        dot = graphviz.Digraph('Contenido')
        tmp = self.cabeza

        # Comenzar la definición de la tabla con etiquetas HTML
        label = "<<TABLE BORDER='1' CELLBORDER='1' CELLSPACING='0' CELLPADDING='4'>"

        while tmp is not None:
            label += f'<TR><TD>{tmp.nombre}</TD></TR>'  # Nombre del dron como título de columna
            label += f'<TR><TD>{tmp.altura}</TD></TR>'  # Altura como valor en la columna
            tmp = tmp.siguiente

        # Cerrar la definición de la tabla con etiquetas HTML
        label += '</TABLE>>'

        # Agregar la tabla como un nodo con etiquetas HTML
        dot.node('tabla', label=label, shape='plaintext')

        # Renderizar y mostrar el gráfico
        dot.render('Lista_contenidos', format='png', view=True)
    
    def graficar_sistema(drones, alturas):
        dot = graphviz.Digraph('Alturas')
        
        # Agregar los nombres de los drones como columnas
        for dron in drones:
            dot.node(dron, dron)
        
        # Agregar las alturas y sus letras como filas
        for altura_valor, altura_letra in alturas.items():
            dot.node(altura_valor, altura_letra)
        
        # Crear conexiones entre los drones y las alturas correspondientes
        for dron in drones:
            for altura_valor, altura_letra in alturas.items():
                dot.edge(dron, altura_valor)
        
        dot.render('Grafico_sistemas', format='png', view=True)

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
    
    def gaficar_mensajes(self):
        dot = graphviz.Digraph('Mensajes')
        tmp = self.cabeza
        contador = 1

        while tmp is not None:
            dot.node(f'{contador}', tmp.verMensajes())
            if tmp.siguiente is not None:
                dot.edge(f'{contador}', f'{contador+1}')
            tmp = tmp.siguiente
            contador += 1

        dot.render('Lista_mensajes', format='png', view=True)
    


""" Nodo y Lista para Instrucciones """
class Instrucciones:
    
    def __init__(self, valor, instruccion):
        self.valor = valor
        self.instruccion = instruccion  
        self.siguiente = None

    def verInstrucciones(self):
        return str(self.valor) + "\n" + str(self.instruccion)
    

class lista_instrucciones():

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
    
    def graficar_instrucciones(self):
        dot = graphviz.Digraph('Instrucciones')
        tmp = self.cabeza
        contador = 1

        while tmp is not None:
            # Crear un label en formato HTML para representar una tabla
            label = f'<<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0">'
            label += f'<TR><TD COLSPAN="2" BGCOLOR="lightgray">{tmp.valor}</TD></TR>'  # Nombre del dron
            label += f'<TR><TD>{tmp.instruccion}</TD></TR>'  # Instrucción
            label += '</TABLE>>'

            dot.node(f'{contador}', label=label, shape='plaintext')
            if tmp.siguiente is not None:
                dot.edge(f'{contador}', f'{contador+1}')
            tmp = tmp.siguiente
            contador += 1

        dot.render('Lista_instrucciones', format='png', view=True)