import psycopg2
from psycopg2 import Error

def crearTabla(cursor):
    try:
        consulta = """
        CREATE TABLE IF NOT EXISTS usuarios (
            ID SERIAL PRIMARY KEY,
            NOMBRE VARCHAR(100),
            APELLIDOS VARCHAR(100),
            NIF VARCHAR(20),
            USERNAME VARCHAR(50) UNIQUE,
            CONTRASENYA VARCHAR(255)
        );
        """
        
        # Imprime la consulta antes de ejecutarla para verificar
        print("Ejecutando consulta para crear tabla:")
        print(consulta)

        cursor.execute(consulta)  # Ejecuta la consulta SQL
        print("Tabla 'usuarios' creada o ya existe.")

    except Exception as e:
        print(f"Error al crear la tabla: {e}")

def main():
    try:
        # Conexión a la base de datos
        conexion = psycopg2.connect(user="usrpostgre",  # Reemplaza con tu usuario
                                     password="usrpostgre",  # Reemplaza con tu contraseña
                                     host="localhost",
                                     port="5432",
                                     database="usuarios")  # Nombre de la base de datos

        cursor = conexion.cursor()

        # Verifica la base de datos a la que estás conectado
        db_name = conexion.get_dsn_parameters()['dbname']
        print(f"Conectado a la base de datos: {db_name}")

        # Verifica que estés conectado a la base de datos correcta
        if db_name != 'usuarios':
            print(f"¡Error! Estás conectado a la base de datos {db_name}, pero se esperaba 'usuarios'.")
            return

        # Llama a la función para crear la tabla
        crearTabla(cursor)

    except (Exception, Error) as error:
        print("Error... al intentar conectar con PostgreSQL:", error)

    finally:
        if conexion:
            conexion.close()
            print("\nCerrando conexión con BD")
            print('Finalizando el programa\n')

if __name__ == '__main__':
    main()
