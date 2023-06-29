import csv
import sys
import pandas as pd
import pymysql

# Configuración de la conexión a la base de datos
host = 'localhost'
user = 'root'
password = '0001'
database = 'Informacion_territorial'
port = 3306

# Configuración del archivo CSV
csv_file1 = 'Entretenimiento.csv'
csv_file2 = 'Establecimientos.csv'
delimiter = ';'

# Establecer la conexión a la base de datos
connection = pymysql.connect(host=host, user=user, password=password, database=database, port=port)

csv.field_size_limit(sys.maxsize)

try:
    with connection.cursor() as cursor:
        with open(csv_file2, 'r') as file:
            csv_data = csv.reader(file, delimiter=delimiter)
            header = next(csv_data)

            insert_query = '''
            INSERT INTO Salud (ID_Establecimiento, N_Establecimiento, Telefono_Establecimiento)
            VALUES (%s,%s,%s)
            '''
            i=0
            for row in csv_data:
                if(row[4]==''):
                    row[4] = 0
                print((i, row[3], row[4]))
                try:    
                    cursor.execute(insert_query, (i, row[3],row[4]))
                    i+=1
                except pymysql.err.DataError as e:
                    print("Error de datos:", e)
                    # Imprime el valor que causó el error
                    print("Valor que causó el error:", row[4])  

        # Confirmar los cambios en la base de datos
        connection.commit()

        print('Datos cargados correctamente.')
finally:
    # Cerrar la conexión a la base de datos
    connection.close()
