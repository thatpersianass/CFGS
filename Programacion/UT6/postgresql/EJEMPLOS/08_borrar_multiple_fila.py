import psycopg2
from psycopg2 import Error
from getpass import getpass

try:
    # Conectamos a la BD prueba2 con el usuario usrpostgre
    connection = psycopg2.connect(user="usrpostgre",
                                password=getpass("Introduzca la contraseña: "),
                                host="localhost",
                                port="5432",
                                database="prueba2")
    
    cursor = connection.cursor()

    # borrado de datos en la tabla mobile
    query_insertar = '''DELETE FROM mobile WHERE id = %s'''
    records = [(5,), (4,), (3,)]
    result = cursor.executemany(query_insertar, records)
    connection.commit()
    count = cursor.rowcount
    print(f"{count} Registros borrados correctamente")
    
except (Exception, Error) as error:
    print("Error... al intentar conectar con PostgreSQL", error)

finally:
    if (connection):
        # cursor.close()
        connection.close()
        print("La conexión con PostgreSQL está cerrada")