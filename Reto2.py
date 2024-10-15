import csv
import json
import pandas as pd


with open('reto.csv', 'r', encoding='utf-8') as fichero_csv:
    reader = csv.DictReader(fichero_csv)
    filas_json = []
    for row in reader:
        filas_json.append(row)
    

with open('reto.json', 'w', encoding='utf8') as fichero_json:
    json.dump(filas_json, fichero_json, indent=4)



print(json.dumps(filas_json, indent=4))