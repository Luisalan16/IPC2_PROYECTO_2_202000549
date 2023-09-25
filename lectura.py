import easygui
import xml.etree.ElementTree as ET



def lectura(Dron, Sistema, Contenido, Altura, Mensaje, Instruccion):
    try:
        archivo =  easygui.fileopenbox(title="Seleccione el archivo", filetypes=("Archivos xml","*.xml"))
        tree = ET.parse(archivo)
        root = tree.getroot()

        """ Lista drones """
        for lista_drones in root.findall('listaDrones'):
            for drones in lista_drones.findall('dron'):
                dron = drones.text
                Dron.insertar_dron(dron)
        
        """ Lista sistemas drones """
        for lista_sistema_drones in root.findall('listaSistemasDrones'):
            for sistema_drones in lista_sistema_drones.findall('sistemaDrones'):
                system_name = sistema_drones.get('nombre')
                altura_maxima = sistema_drones.find('alturaMaxima').text
                qty_drones = sistema_drones.find('cantidadDrones').text
                Sistema.insertar_sistema(system_name, altura_maxima, qty_drones)

                """ Leyendo contenido """
                for content in sistema_drones.findall('contenido'):
                    for dron_content in content.findall('dron'):
                        dron_c = dron_content.text
                        Contenido.insertar_contenido(dron_c)

                for altura_content in sistema_drones.findall('contenido'):
                    for altura_c in altura_content.findall('alturas'):
                        altura_valor = altura_c.get('valor')
                        altura = altura_c.text
                        Altura.insertar_alturas(altura_valor, altura)
        """ Lista mensajes """                
        for lista_mensajes in root.findall('listaMensajes'):
            for mensajes in lista_mensajes.findall('Mensaje'):
                mensaje = mensajes.get('nombre')
                system_dron_msj = mensajes.find('sistemaDrones').text
                Mensaje.insertar_mensajes(mensaje, system_dron_msj)


                """ instrucciones """
                for instrucciones in mensajes.findall('instrucciones'):
                    for instruccion in instrucciones.findall('instruccion'):
                        dron_instruccion = instruccion.get('nombre')
                        dron_altura = instruccion.text
                        Instruccion.insertar_instrucciones(dron_instruccion, dron_altura)


    
    except:
        print("Messi")