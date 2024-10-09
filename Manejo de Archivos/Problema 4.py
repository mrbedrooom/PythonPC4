# RESUMEN DE TEMPERATURAS

import csv

def leer_temperaturas(nombre_archivo):
    temperaturas= []
    with open(nombre_archivo, 'r') as archivo:
        lector_csv= csv.reader(archivo)
        next(lector_csv)  # Saltar la cabecera
        for fila in lector_csv:
            fecha, temperatura= fila
            temperaturas.append(float(temperatura))
    return temperaturas

def calcular_estadisticas(temperaturas):
    temperatura_maxima= max(temperaturas)
    temperatura_minima= min(temperaturas)
    temperatura_promedio= sum(temperaturas) / len(temperaturas)
    return temperatura_maxima, temperatura_minima, temperatura_promedio

def escribir_resumen(nombre_archivo, temperatura_maxima, 
                     temperatura_minima, temperatura_promedio):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(f"Temperatura máxima: {temperatura_maxima}\n")
        archivo.write(f"Temperatura mínima: {temperatura_minima}\n")
        archivo.write(f"Temperatura promedio: {temperatura_promedio:.2f}\n")


archivo_entrada= 'temperaturas.txt'
archivo_salida= 'resumen_temperaturas.txt'

temperaturas= leer_temperaturas(archivo_entrada)

# Calcular estadísticas
temperatura_maxima, temperatura_minima, temperatura_promedio= calcular_estadisticas(temperaturas)

# Escribir resumen
escribir_resumen(archivo_salida, temperatura_maxima, temperatura_minima, temperatura_promedio)

print("Resumen de temperaturas generado correctamente.")
