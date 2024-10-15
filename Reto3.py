import json

# Solucion utilizando el fichero JSON
with open('reto.json', 'r', encoding='utf-8') as fichero_json:
    datos_json = json.load(fichero_json)


distancias_vehiculo = {}

for fila in datos_json:
    matricula = fila['Matricula']
    distancia = float(fila['Distance'])

    if matricula in distancias_vehiculo:
        distancias_vehiculo[matricula] += distancia
    else:
        distancias_vehiculo[matricula] = distancia

for matricula, distancia in distancias_vehiculo.items():
    print(f"El vehiculo {matricula} ha recorrido una distancia total de: {distancia}")