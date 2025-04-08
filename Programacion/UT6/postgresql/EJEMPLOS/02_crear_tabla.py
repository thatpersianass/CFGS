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
    query = '''CREATE TABLE mobile
                (ID INT PRIMARY KEY NOT NULL,
                MODEL TEXT NOT NULL,
                PRICE REAL);'''
    
    # Ejecutando la consulta
    cursor.execute(query)
    # Consolidamos la modificacion de la BD
    connection.commit()
    print("La tabla mobile ha sido creada satisfactoriamente")

except (Exception, Error) as error:
    print("Error... al intentar conectar con PostgreSQL", error)

finally:
    if (connection):
        # cursor.close()
        connection.close()
        print("La conexión con PostgreSQL está cerrada")