import csv
import pandas as pd

#Solucion con Pandas
df = pd.read_csv('reto.csv')
print(df)

#Solucion utilizando el modulo csv de Python
with open('reto.csv', 'r', newline='') as fichero_csv:
    reader = csv.reader(fichero_csv, delimiter=' ')
    for row in reader:
        print(', '.join(row))