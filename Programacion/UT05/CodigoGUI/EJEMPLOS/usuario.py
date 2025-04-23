import psycopg2
from psycopg2 import Error
from getpass import getpass

def validarDatos():
    return True

def insertarUsuario(conexion, cursor):
    nombre_usuario = input('Introduzca el nombre de usuario: ')
    consulta = f"""SELECT * from usuarios
                  WHERE username = '{nombre_usuario}';"""
    cursor.execute(consulta)
    nro_reg_obtenidos = cursor.rowcount
    if nro_reg_obtenidos:
        print('Error...el usuario ya existe en la BD')
    else:
        identificador = int(input('Introduzca número para su identificación: '))
        nombre = input('Introduzca su nombre: ')
        apellidos = input('Introduzca su/sus apellido/s: ')
        nif_nie = input('Introduzca el NIF/NIE: ')
        contraseña = input('Introduzca el contraseña: ')
        if validarDatos():
            consulta = f"""INSERT INTO usuarios (ID, NOMBRE, APELLIDOS, NIF, USERNAME, CONTRASENYA) 
                        VALUES ({identificador}, '{nombre}', '{apellidos}', '{nif_nie}', '{nombre_usuario}', '{contraseña}');"""
            try:
                cursor.execute(consulta)
                conexion.commit()           
                if cursor.rowcount:
                    print('Registro insertado satisfactoriamente')
            except:
                print('Error... al insertar el usuario')
        else:
            print('Error...los datos no son correctos')


def modificarUsuario(conexion, cursor, opcion):
    nombre_usuario = input('Introduzca el nombre de usuario: ')
    consulta = f"""SELECT * from usuarios
                  WHERE username = '{nombre_usuario}';"""
    
    nro_reg_obtenidos = cursor.rowcount
    if nro_reg_obtenidos:
        if opcion == 1:
            nuevo_nombre_usuario = input('Introduzca el nuevo nombre de usuario: ')
            if validarDatos():
                consulta = f"""UPDATE usuarios SET username = {nuevo_nombre_usuario} WHERE username = {nombre_usuario}"""
                cursor.execute(consulta)  # try
                conexion.commit()
                if cursor.rowcount:
                    print('Registro modificado satisfactoriamente')
            else:
                print('Error...El nombre de usuario no es correcto')

        else:
            nueva_contraseña = input('Introduzca el nuevo nombre de usuario: ')
            if validarDatos():
                consulta = f"""UPDATE usuarios SET contrasenya = {nueva_contraseña} WHERE username = {nombre_usuario}"""
                cursor.execute(consulta)
                conexion.commit()   # try
                if cursor.rowcount:
                    print('Registro modificado satisfactoriamente')
            else:
                print('Error...La contraseña no es válida no es correcto')
    else:
        print('Error...el usuario NO existe en la BD')
        
def borrarUsuario():
    pass

def main():

    try:
        conexion = psycopg2.connect(user="usrpostgre",
                                        #password=getpass("Introduzca la contraseña: "),
                                        password = 'usrpostgre',
                                        host="localhost",
                                        port="5432",
                                        database="Usuarios")

    except (Exception, Error) as error:
        print("Error...al intentar conectar con PostgreSQL", error)

    else:
        cursor = conexion.cursor()
        while True:
            print ('\n1. Insertar\n2. Modificar\n3. Borrar\n4. Salir\n')
            opc = input('Introduzca opción: ')
            match opc:
                case '1':
                    insertarUsuario(conexion, cursor)
                case '2':
                    print ('\nOpciones de Modificar\n\n1. Usrname\n2. Contraseña\n3. Regresar\n')
                    opc2 = input('¿Qué desea modificar?...: ')
                    match opc2:
                        case '1'|'2':
                            modificarUsuario(conexion, cursor, opc2)
                        # case '2':
                        #     modificarUsuario()
                        case '3':
                            print('Regresando a menú principal...')
                        case _:
                            print('\nError...ha introducido una opción inválida')
                case '3':
                    borrarUsuario()
                case '4':
                    break
                case _:
                    print('\nError...ha introducido una opción inválida')
    finally:
        if (conexion):
            conexion.close()
            print("\nCerrando conexión con BD")
            print('Finalizando el programa\n')

if __name__ == '__main__':
    main()