# BITCOINS

n= float(input("Introduce la cantidad de bitcoins que posees: "))

import requests

# Consultando la API de CoinDesk
try:
    response= requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response.raise_for_status()
    data= response.json()
    precio_bitcoin= data['bpi']['USD']['rate_float']
except requests.RequestException as e:
    print(f"Error al consultar la API: {e}")
    exit()

costo_total= n * precio_bitcoin

print(f"El costo actual de {n} bitcoins es: ${costo_total:,.4f} USD")