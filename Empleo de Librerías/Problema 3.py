#COMPRIMIENDO IMAGEN A ZIP

import zipfile
import os

ruta_imagen = input("Introduce la ruta completa de la imagen descargada: ")

ruta_zip = input("Introduce la ruta completa donde quieres guardar "+
                  "el archivo ZIP: ")

directorio_extraccion = input("Introduce la ruta del directorio donde "+
                               "quieres extraer la imagen: ")

# Creando un archivo ZIP
with zipfile.ZipFile(ruta_zip, 'w') as zipf:
    zipf.write(ruta_imagen, os.path.basename(ruta_imagen))

print(f"Imagen {ruta_imagen} ha sido comprimida como {ruta_zip}")

# Extraer la imagen del archivo ZIP
with zipfile.ZipFile(ruta_zip, 'r') as zipf:
    zipf.extractall(directorio_extraccion)

print(f"Imagen ha sido extraída en el directorio {directorio_extraccion}")

# Nota: Fijarse el directorio desde donde se ejecuta este Script