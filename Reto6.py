from flask import Flask, jsonify, abort

import json


api_url = "https://localhost/"

api = Flask(__name__)

def cargar_posiciones_vehiculo():
    vehiculos={}
    with open("vehiculos_por_fecha.txt", 'r', encoding='utf-8')as fichero_txt:
        for linea in fichero_txt:
            matricula = linea.split(": ")[0].strip()
            fecha = linea.split(": ")[1].strip()
            vehiculos[matricula] = {"matricula": matricula, "fecha": fecha}    
    return vehiculos


@api.route('/<matricula>', methods=['GET'])
def get_vehiculo(matricula):
    vehiculos = cargar_posiciones_vehiculo()

    if matricula in vehiculos:
        return jsonify({
            "Matricula": matricula,
            "Fecha": vehiculos[matricula]["fecha"]
        })
    else:
        abort(404, "Vehiculo no encontrado")
    
if __name__ == '__main__':
    api.run(debug=True)