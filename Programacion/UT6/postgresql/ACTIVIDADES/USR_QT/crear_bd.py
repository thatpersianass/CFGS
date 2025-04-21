import psycopg2
from psycopg2 import Error
from getpass import getpass

try:
    # Conectamos a la BD prueba con el usuario usrpostgre
    connection = psycopg2.connect(user="usrpostgre",
                                #   password=getpass("Introduzca la contraseña: "),
                                password = "usrpostgre",
                                host="localhost",
                                port="5432",
                                database="usuarios")

    query = '''CREATE TABLE usuarios
            (id INT PRIMARY KEY NOT NULL,
            nombre VARCHAR(30) NOT NULL,
            apellidos VARCHAR(40) NOT NULL,
            nif CHAR(9) NOT NULL,
            username VARCHAR(12) NOT NULL,
            contrasenya VARCHAR(12) NOT NULL);'''

    # Creamos el cursor y ejecutamos la consulta 
    cursor = connection.cursor()
    cursor.execute(query)
    # consolidamos la modificación de la BD
    connection.commit()
    print("La tabla Usuarios ha sido creada satisfactoriamente")

    # agregamos las restricciones

    query =  """alter table usuarios add constraint USERNAME_UNICO unique (username);"""
    cursor.execute(query)
    connection.commit()
    query =  """alter table usuarios add constraint NIF_UNICO unique (nif);"""
    cursor.execute(query)
    connection.commit()
    print("La tabla Usuarios ha sido creada satisfactoriamente")

except (Exception, Error) as error:
    print("Error...al intentar conectar con PostgreSQL", error)
finally:
    if (connection):
        # cursor.close()
        connection.close()
        print("La conexión con PostgreSQL está cerrada")
