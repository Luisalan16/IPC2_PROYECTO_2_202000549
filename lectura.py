import easygui
import xml.etree.ElementTree as ET



def lectura(Dron, Sistema, Contenido, Altura, Mensaje, Instruccion):
    try:
        archivo = easygui.fileopenbox(title="Seleccione el archivo", filetypes=("Archivos xml", "*.xml"))
        tree = ET.parse(archivo)
        root = tree.getroot()

        """ Lista drones """
        for lista_drones in root.findall('listaDrones'):
            for dron in lista_drones.findall('dron'):
                dron_nombre = dron.text
                Dron.insertar_dron(dron_nombre)
                Dron.ordenar_alfabeticamente()

        """ Lista sistemas drones """
        for sistema_drones in root.findall('listaSistemasDrones/sistemaDrones'):
            system_name = sistema_drones.get('nombre')
            altura_maxima = sistema_drones.find('alturaMaxima').text
            qty_drones = sistema_drones.find('cantidadDrones').text
            Sistema.insertar_sistema(system_name, altura_maxima, qty_drones)

            """ Leyendo contenido """
            for contenido in sistema_drones.findall('contenido'):
                dron_nombre = contenido.find('dron').text
                Contenido.insertar_contenido(dron_nombre)

                """ Alturas """
                alturas = contenido.findall('alturas/altura')
                for altura in alturas:
                    altura_valor = altura.get('valor')
                    altura_texto = altura.text
                    Altura.insertar_alturas(altura_valor, altura_texto, dron_nombre)

        """ Lista mensajes """
        for mensaje in root.findall('listaMensajes/Mensaje'):
            mensaje_nombre = mensaje.get('nombre')
            system_dron_msj = mensaje.find('sistemaDrones').text
            Mensaje.insertar_mensajes(mensaje_nombre, system_dron_msj)

            """ Instrucciones """
            instrucciones = mensaje.findall('instrucciones/instruccion')
            for instruccion in instrucciones:
                dron_instruccion = instruccion.get('dron')
                dron_altura = instruccion.text
                Instruccion.insertar_instrucciones(dron_instruccion, dron_altura)

    except Exception as e:
        print("Ocurrió un error:", e)


def generar_xml(Dron, Sistema, Mensaje):
    respuesta = ET.Element("respuesta")

    # Agregar la lista de drones
    listaDrones = ET.SubElement(respuesta, "listaDrones")
    for dron in Dron:
        dron_element = ET.SubElement(listaDrones, "dron")
        dron_element.text = dron.nombre

    # Agregar la lista de sistemas de drones
    listaSistemasDrones = ET.SubElement(respuesta, "listaSistemasDrones")
    for sistema in Sistema:
        sistema_element = ET.SubElement(listaSistemasDrones, "sistemaDrones", nombre=sistema.nombre)
        alturaMaxima = ET.SubElement(sistema_element, "alturaMaxima")
        alturaMaxima.text = sistema.altura_maxima
        cantidadDrones = ET.SubElement(sistema_element, "cantidadDrones")
        cantidadDrones.text = sistema.cantidad_drones

        # Agregar el contenido de cada sistema de drones
        contenido = ET.SubElement(sistema_element, "contenido")
        for contenido_dron in sistema.contenido:
            dron_element = ET.SubElement(contenido, "dron")
            dron_element.text = contenido_dron

        # Agregar las alturas de cada sistema de drones
        alturas = ET.SubElement(sistema_element, "alturas")
        for altura, valor in sistema.alturas.items():
            altura_element = ET.SubElement(alturas, "altura", valor=valor)
            altura_element.text = altura

    # Agregar la lista de mensajes
    listaMensajes = ET.SubElement(respuesta, "listaMensajes")
    for mensaje in Mensaje:
        mensaje_element = ET.SubElement(listaMensajes, "Mensaje", nombre=mensaje.nombre)
        sistemaDrones = ET.SubElement(mensaje_element, "sistemaDrones")
        sistemaDrones.text = mensaje.sistema_drones

        # Agregar las instrucciones para cada mensaje
        instrucciones = ET.SubElement(mensaje_element, "instrucciones")
        for instruccion in mensaje.instrucciones:
            instruccion_element = ET.SubElement(instrucciones, "instruccion", nombre=instruccion.nombre)
            instruccion_element.text = instruccion.text

    # Crea un objeto ElementTree y escribe el archivo XML
    tree = ET.ElementTree(respuesta)
    tree.write("Salida.xml")
