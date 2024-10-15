from flask import Flask, jsonify, abort
import psycopg2
import json


api_url = "https://localhost/"

api = Flask(__name__)


conn = psycopg2.connect(
    dbname="vehiculos_db", user="admin", password="password", host="localhost", port='5432'
)
cursor =conn.cursor()

def load_datos_db():
    
    vehiculos =  cursor.execute("""
                    SELECT * FROM vehiculos
                """)
            
    conn.commit()  
    vehiculos = cursor.fetchall()  
    cursor.close()
    conn.close() 
    vehiculos_dict = {row[0]: row[1] for row in vehiculos}
    return vehiculos_dict


@api.route('/<matricula>', methods=['GET'])
def get_vehiculo(matricula):
    vehiculos = load_datos_db()

    if matricula in vehiculos:
        return jsonify({
            "Matricula": matricula,
            "Fecha": vehiculos[matricula]
        })
    else:
        abort(404, "Vehiculo no encontrado")
    
if __name__ == '__main__':
    api.run(debug=True)