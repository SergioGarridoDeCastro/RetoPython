import json 
import numpy as np

# Solucion utilizando el fichero JSON
with open('reto.json', 'r', encoding='utf-8') as fichero_json:
    datos_json = json.load(fichero_json)

def distancia_harvesine(latitud1, longitud1, latitud2, longitud2):
    R = 6371 # Radio de la Tierra en km

    # Conversion a radianes
    lat1 = np.radians(float(latitud1))
    long1 = np.radians(float(longitud1))
    lat2 = np.radians(float(latitud2))
    long2 = np.radians(float(longitud2))

    dif_lat = lat2 - lat1
    dif_long = long2 - long1

    a = (np.sin(dif_lat/2)**2) + (np.cos(lat1) * np.cos(lat2) * (np.sin(dif_long/2)**2))
    c = 2 * np.arcsin(np.sqrt(a))
    dist = R*c

    return dist

distancias_vehiculo = {}
ultima_posicion_vehiculo = {}

for fila in datos_json:
    matricula = fila['Matricula']
    latitud = fila['Latitud']
    longitud = fila['Longitud']
    distancia = float(fila['Distance'])

    if matricula in ultima_posicion_vehiculo:
        lat_anterior, lon_anterior = ultima_posicion_vehiculo[matricula]
        distancia = distancia_harvesine(lat_anterior, lon_anterior, latitud, longitud)

    else:
        distancia = 0

    ultima_posicion_vehiculo[matricula] = (latitud, longitud)
    if matricula in distancias_vehiculo:
        distancias_vehiculo[matricula] += distancia
    else:
        distancias_vehiculo[matricula] = distancia

for matricula, distancia in distancias_vehiculo.items():
    print(f"El vehiculo {matricula} ha recorrido una distancia total de: {distancia}")


