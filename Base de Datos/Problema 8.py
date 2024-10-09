# CONVERSIÓN DE DOLARES A SOLES PARA UN PRODUCTO

import sqlite3
import csv
from pymongo import MongoClient

# Conectando a la base de datos mongodb
client = MongoClient('mongodb://localhost:27017/')
db = client['tu_base_de_datos']
coleccion = db['tipo_cambio']

# Conectando a la base de datos sqlite
conn = sqlite3.connect('ventas.db')
cursor = conn.cursor()

# Creando una tabla para las ventas
cursor.execute('''
CREATE TABLE IF NOT EXISTS ventas (
    id INTEGER PRIMARY KEY,
    producto TEXT,
    cantidad INTEGER,
    precio_dolares REAL,
    fecha_compra TEXT
)
''')

# Cargando los datos del csv a la tabla
with open('ventas.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Saltar la cabecera
    ventas = [(row[1], int(row[2]), float(row[3]), row[0]) for row in reader]

cursor.executemany('''
INSERT INTO ventas (producto, cantidad, precio_dolares, fecha_compra) 
                   VALUES (?, ?, ?, ?)
''', ventas)

conn.commit()

# Obteniendo los tipos de cambio de mongodb
tipos_cambio = {doc['fecha']: doc['tipo_cambio'] for doc in coleccion.find()}
print("Tipos de cambio obtenidos de MongoDB:")
print(tipos_cambio)

# Creando una tabla para los tipos de cambio
cursor.execute('''
CREATE TABLE IF NOT EXISTS tipo_cambio (
    fecha TEXT PRIMARY KEY,
    tipo_cambio REAL
)
''')

# Insertando los tipos de cambio en la tabla sqlite
for fecha, tipo in tipos_cambio.items():
    cursor.execute('''
    INSERT OR IGNORE INTO tipo_cambio (fecha, tipo_cambio) VALUES (?, ?)
    ''', (fecha, tipo))

conn.commit()

# Realizando la conversión de precios y calculando los totales
cursor.execute('''
SELECT
    producto,
    SUM(precio_dolares * cantidad) AS total_dolares,
    SUM(precio_dolares * cantidad * tipo_cambio) AS total_soles
FROM
    ventas
JOIN
    tipo_cambio
ON
    ventas.fecha_compra = tipo_cambio.fecha
GROUP BY
    producto
''')

# Obteniendo y mostrando los resultados
resultados = cursor.fetchall()
for row in resultados:
    print(f"Producto: {row[0]}, Total en Dólares: {row[1]:.2f}, Total en Soles: {row[2]:.2f}")

conn.close()