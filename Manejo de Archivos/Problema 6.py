# CONTADOR DE LÍNEAS DE CÓDIGO

def contar_lineas_codigo(ruta_archivo):
    try:
        if not ruta_archivo.endswith(".py"):
            print("Error: El archivo debe tener la extensión .py")
            return

        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()

        lineas_codigo = [linea for linea in lineas if linea.strip() and not 
                         linea.strip().startswith('#')]
        print(f"El archivo {ruta_archivo} tiene {len(lineas_codigo)} 
              líneas de código (sin contar comentarios y líneas en blanco).")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta {ruta_archivo}")

if __name__ == "__main__":
    ruta_archivo= input("Introduce la ruta completa del archivo .py: ")
    contar_lineas_codigo(ruta_archivo)