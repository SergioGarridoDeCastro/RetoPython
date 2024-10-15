import psycopg2



conn = psycopg2.connect(
    dbname="vehiculos_db", user="admin", password="password", host="localhost", port='5432'
)
cursor =conn.cursor()

def load_datos_fichero():
    with open("vehiculos_por_fecha.txt",'r', encoding='utf-8') as fichero_txt:
        for linea in fichero_txt:
            matricula = linea.split(": ")[0].strip()
            fecha = linea.split(": ")[1].strip()

            cursor.execute("""
                    INSERT INTO vehiculos (matricula, fecha) 
                    VALUES (%s, %s)
                """, (matricula, fecha))
            
    conn.commit()   

load_datos_fichero()

cursor.close()
conn.close()

print("Datos cargados correctamente en la base de datos.")