import json
from datetime import datetime

with open('reto.json', 'r', encoding='utf-8') as fichero_json:
    datos_json = json.load(fichero_json)

def conversion_posix_date(pos_date):
    fecha = datetime.fromtimestamp(pos_date / 1000)
    return fecha.strftime('%d/%m/%Y %H:%M:%S')

ultima_posicion_vehiculo = {}

for fila in datos_json:
    matricula = fila['Matricula']
    fecha_posix = int(fila['Pos_date'])

    if matricula in ultima_posicion_vehiculo:
        if fecha_posix > ultima_posicion_vehiculo[matricula]["Pos_date"]:
            ultima_posicion_vehiculo[matricula] = {
                "Pos_date": fecha_posix,
                "Fecha": conversion_posix_date(fecha_posix)
            }

    else:
        ultima_posicion_vehiculo[matricula] = {
            "Pos_date": fecha_posix,
            "Fecha": conversion_posix_date(fecha_posix)
        }

vehiculos_ordenados = sorted(ultima_posicion_vehiculo.items(), key = lambda x: x[1]["Pos_date"], reverse=True)


with open('vehiculos_por_fecha.txt', 'w', encoding='utf-8') as fichero_txt:
    for matricula, datos in vehiculos_ordenados:
        fichero_txt.write(f"{matricula}: {datos['Fecha']}\n")
