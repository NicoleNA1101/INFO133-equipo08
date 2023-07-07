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
csv_file3 = 'Comunas.csv'
csv_file4 = 'Trabajo.csv'
csv_file5 = 'Regiones.csv'
csv_file6 = 'Seguridad.csv'

# Establecer la conexión a la base de datos
connection = pymysql.connect(host=host, user=user, password=password, database=database, port=port)

csv.field_size_limit(sys.maxsize)

try:
    with connection.cursor() as cursor:

        #Carga Regiones
        with open(csv_file5, 'r') as file:
            csv_data = csv.reader(file, delimiter=';')
            header = next(csv_data)
            insert_query = '''
            INSERT INTO Region (`ID_R`, `Cantidad_C`, `Nombre_CP`, `Nombre_R`, `Nombre_Pais`)
            VALUES (%s,%s,%s,%s,%s)
            '''
            for row in csv_data:
                #print((row[0], 0 ,row[5], row[1], 'Chile'))
                cursor.execute(insert_query, (row[0], 0 ,row[5], row[1], 'Chile'))

        #Carga Comunas
        with open(csv_file3, 'r') as file:
            csv_data = csv.reader(file, delimiter=';')
            header = next(csv_data)
            insert_query = '''
            INSERT INTO Comuna (ID_C, Nombre_P, PoblacionT, Nombre_C, ID_R)
            VALUES (%s,%s,%s,%s,%s)
            '''
            for row in csv_data:
                print((row[0],row[2],row[4],row[1]))
                try:
                    cursor.execute(insert_query, (row[0],row[2],row[5],row[1],row[3]))
                except pymysql.err.IntegrityError as e:
                    print("Error de datos:", e)
                    # Imprime el valor que causó el error
                    print("Valor que causó el error:", (row[0],row[2],row[5],row[1],row[3])) 

        #Cuenta las comunas por region
        with open(csv_file5, 'r') as file:
            csv_data = csv.reader(file, delimiter=';')
            header = next(csv_data)
            for row in csv_data:
                consulta = "SELECT COUNT(*) FROM Comuna WHERE ID_R = %s"
                cursor.execute(consulta, (row[0],))
                cantidad_comunas = cursor.fetchone()[0]
                consulta_actualizacion = "UPDATE Region SET Cantidad_C = %s WHERE ID_R = %s"
                cursor.execute(consulta_actualizacion, (cantidad_comunas, row[0]))

        #Carga Trabajo
        with open(csv_file4, 'r') as file:
            csv_data = csv.reader(file, delimiter=',')
            header = next(csv_data)
            insert_query = '''
            INSERT INTO Trabajo (ID_Tipo_Ocupación, H_ParaTrabajar, M_ParaTrabajar, H_Desocupados, M_Desocupadas, H_Ocupados, M_Ocupadas, ID_C)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            '''       
            i=0
            for row in csv_data:
                #print(row)
                cursor.execute(insert_query, (i,row[6],row[3],row[8],row[5], row[7],row[4],row[0]))
                i+=1

        #Carga Salud
        with open(csv_file2, 'r') as file:
            csv_data = csv.reader(file, delimiter=';')
            header = next(csv_data)
            insert_query = '''
            INSERT INTO Salud (ID_Establecimiento, N_Establecimiento, Telefono_Establecimiento)
            VALUES (%s,%s,%s)
            '''
            i=0
            for row in csv_data:
                if(row[4]==''):
                    row[4] = 0
                #print((i, row[3], row[4]))
                try:    
                    cursor.execute(insert_query, (i, row[3],row[4]))
                    i+=1
                except pymysql.err.DataError as e:
                    print("Error de datos:", e)
                    # Imprime el valor que causó el error
                    print("Valor que causó el error:", row[4]) 


        #Carga Seguridad
        with open(csv_file6, 'r') as file:
            csv_data = csv.reader(file, delimiter=',')
            header = next(csv_data)
            insert_query = '''
            INSERT INTO Seguridad (ID_Establecimientos, Comisarias, Reten, Subcomisaria, Prefactura, Tenencia, Zona, ID_C)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            '''       
            i=0
            for row in csv_data:
                print((i,row[2],row[3],row[4],row[5], row[6],row[7],row[0]))
                cursor.execute(insert_query, (i,row[2],row[3],row[4],row[5], row[6],row[7],row[0]))
                i+=1

        """
        with open(csv_file1, 'r') as file:
            csv_data = csv.reader(file, delimiter=',')
            header = next(csv_data)
            insert_query = '''
            INSERT INTO Entretencion (ID_Estadio, Nombre_Estadio, Region_Estadio, Ciudad_Estadio, Ano_Apertura, Equipos_Locales, Capacidad_Estadio )
            VALUES (%s,%s,%s,%s,%s,%s,%s)
            '''       
            i=0
            for row in csv_data:
                print((i,row[0],row[2],row[1],row[3], row[5],row[4]))
                cursor.execute(insert_query, (i,row[0],row[2],row[1],row[3], row[5],row[4]))
                i+=1
        """      

        # Confirmar los cambios en la base de datos
        connection.commit()

        print('Datos cargados correctamente.')
finally:
    # Cerrar la conexión a la base de datos
    connection.close()
