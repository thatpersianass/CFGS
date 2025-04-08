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
    
    print("Informacion del servidor PostgreSQL")
    print(f"\n{connection.get_dsn_parameters()}\n")
    # Creamos un cursor para la ejecución de una consulta
    cursor = connection.cursor()
    # Creando una consulta
    consulta = "SELECT version();"
    # Ejecutando la consulta
    cursor.execute(consulta)
    # Obteniendo los resultados
    record = cursor.fetchone()
    print(f"Estas conectado - {record}\n")

except (Exception,Error) as error:
    print("Error... al intentar conectar con PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("La conexión con PostgreSQL está cerrada")