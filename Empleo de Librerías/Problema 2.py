#IMPRIMIENDO CON FIGLET

from pyfiglet import Figlet
import random

figlet = Figlet()

# Obteniendo la lista de fuentes disponibles
fuentes_disponibles= figlet.getFonts()

fuente_seleccionada= input("Ingrese el nombre de una fuente " +
                           "(o presione Enter): ")

# Si no se ingresa ninguna fuente, selecciona una aleatoria
if not fuente_seleccionada:
    fuente_seleccionada= random.choice(fuentes_disponibles)

figlet.setFont(font=fuente_seleccionada)

texto_imprimir = input("Ingrese el texto a imprimir: ")

print(figlet.renderText(texto_imprimir))
