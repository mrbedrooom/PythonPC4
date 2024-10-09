# CAMBIO DEL DOLAR SEGÚN SUNAT

import requests
import sqlite3
from pymongo import MongoClient

def obtener_tipo_cambio(fecha):
    url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?fecha={fecha}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def almacenar_sqlite(data):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info (fecha TEXT, compra REAL, venta REAL)''')
    for item in data:
        cursor.execute('INSERT INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)', 
                       (item['fecha'], item['compra'], item['venta']))
    conn.commit()
    conn.close()

def almacenar_mongodb(data):
    client = MongoClient('localhost', 27017)
    db = client['base']
    collection = db['sunat_info']
    collection.insert_many(data)

def mostrar_contenido_sqlite():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM sunat_info')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

datos_sunat = []
for mes in range(1, 13):
    for dia in range(1, 32):
        fecha = f"2023-{mes:02d}-{dia:02d}"
        data = obtener_tipo_cambio(fecha)
        if data:
            datos_sunat.append({'fecha': fecha, 'compra': data['compra'], 'venta': data['venta']})

almacenar_sqlite(datos_sunat)
almacenar_mongodb(datos_sunat)
mostrar_contenido_sqlite()