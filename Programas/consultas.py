import pymysql

host = 'localhost'
user = 'root'
password = '0001'
database = 'Informacion_territorial'
port = 3306

connection = pymysql.connect(host=host, user=user, password=password, database=database, port=port)

consultas = [
"SELECT Nombre_C FROM Comuna c JOIN Entretencion e ON c.ID_C = e.ID_C WHERE c.ID_R = 'RM';",
"SELECT COUNT(*) AS cantidad_hospitales_clinicas FROM Salud s JOIN Comuna c ON s.ID_C = c.ID_C WHERE c.Nombre_C = 'Valdivia';",
"SELECT c.Nombre_C FROM Comuna c JOIN Seguridad s ON c.ID_C = s.ID_C WHERE s.Zona <> 0;",
"SELECT c.Nombre_C FROM Comuna c JOIN Seguridad s ON c.ID_C = s.ID_C WHERE s.Comisarias > 0 AND s.Reten > 0;",
"SELECT SUM(H_Ocupados + M_Ocupadas) AS personas_ocupadas FROM Trabajo t JOIN Comuna c ON t.ID_C = c.ID_C WHERE c.ID_R = 'LR';",
"SELECT Nombre_C, PoblacionT FROM Comuna ORDER BY PoblacionT DESC;",
"SELECT Nombre_Estadio FROM Entretencion WHERE Capacidad_Estadio > 10000;",
"SELECT c.Nombre_C AS Ciudad, r.Nombre_R AS Region, e.Capacidad_Estadio AS Capacidad FROM Comuna c JOIN Entretencion e ON c.ID_C = e.ID_C JOIN Region r ON c.ID_R = r.ID_R WHERE e.Equipos_Locales LIKE '%Deportes Puerto Montt%';",
"SELECT Nombre_C FROM Comuna WHERE PoblacionT > 200000;",
"SELECT Nombre_C, Densidad_C FROM Comuna WHERE Nombre_P = 'Santiago';",
"SELECT Telefono_Establecimiento FROM Salud s WHERE s.ID_C = 15101;",
"SELECT c.Nombre_C, t.M_Desocupadas FROM Trabajo t JOIN Comuna c ON t.ID_C = c.ID_C WHERE c.ID_R = 'LR';",
"SELECT r.Nombre_R AS Region, r.Nombre_CP AS Capital FROM Region r;",
]

cursor = connection.cursor()

for query in consultas:
    print(query)
    cursor.execute(query)
    respuesta = cursor.fetchall()
    for row in respuesta:
        print(row)
    print()