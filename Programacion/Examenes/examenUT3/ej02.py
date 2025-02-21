# Se quiere diseñar un programa de autenticacion de usuarios en el que se use como persistencia de los datos la libreria pickle

#  La estructura de datos que se debe utilizar es un diccionario donde la clave será el NIF, y el valor una lista con el resto de valores que se deben guardar del usuario.

# Nombre de usuario: un string de 8 caracteres
# Nombre completo
# Edad: un numero entero >= 18 y < 70
# Estado civil: un string con el siguente rango (casad@, divorciad@, viud@, solter@)
# Contraseña: un string de longitud entre 6 y 10 que debe tener letras y numeros, no puede empezar por numero y debe contener letras mayus y minus

# Menu del usuario "Seleccione una opción:\n  1. Entrar\n  2. Salir\n  -->"
# Si se pulsa la opcion 1 se pregunta al usuario quiere introducir el NIF o el nombre de usuario
import os
import pickle
directorio_actual = os.getcwd()
ruta_archivo = os.path.join(directorio_actual, 'usuarios.pckl')

def leer_archivo(ruta_pickle:str):
    try:
        with open(ruta_pickle, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
        return []
    except:
        print("Error al intentar abrir el archivo.")
        return []

def escribir_archivo(ruta_pickle:str, datos: list):
    try:
        with open(ruta_pickle, "wb") as f:
            pickle.dump(datos, f)
    except:
        print("Error al intentar escribir el archivo.")

datos = leer_archivo(ruta_archivo)

while True:
    try:
        opt = int(input('Seleccione una opción:\n  1. Entrar\n  0. Salir\n -->  '))
    except ValueError:
        print('Por favor, introduce un número entero válido.\n')
    else:
        if opt == 1:
            while True:
                try:
                    opt = int(input('\nDesea acceder a través del NIF o el nombre de usuario?\n  1. NIF\n  2. Nombre de usuario\n  0. Atrás\n ->  '))
                except ValueError:
                    print('Por favor, introduce un número entero válido.\n')
                else:
                    if opt == 1:
                        nif = input('Introduzca su NIF:\n ->  ')
                        if nif not in datos:
                            try:
                                opt = int(input('NIF no encontrado, ¿Desea crear una cuenta?\n  1. Si\n  2. No\n ->'))
                            except ValueError:
                                print('Por favor, introduce un número entero válido.\n')
                            else:
                                if opt == 1:
                                    while True:
                                        user = input('Introduzca su nombre de usuario:\n ->  ')
                                        if len(user) != 8:
                                            print('El nombre de usuario debe tener 8 caracteres.')
                                        else:
                                            break
                                        
                                    nombre = input('Introduzca su nombre completo:\n ->  ')
                                    while True:
                                        edad = int(input('Introduzca su edad:\n ->  '))
                                        if edad < 18 and edad >= 70:
                                            print('Introduzca una edad mayor de 18 y menor que 70.')
                                        else:
                                            break
                                        
                                    while True:
                                        estado_civil = input('Introduzca su estado civil (casad@, divorciad@, viud@, solter@):\n ->  ')
                                        if estado_civil in ['casad@', 'divorciad@', 'viud@','solter@']:
                                            break
                                        else:
                                            print('Por favor, introduce un estado civil válido.\n')
                                    contrasena = reversed(nif)
                                    datos.append({'NIF': nif, 'Nombre de Usuario': user, 'Nombre completo': nombre, 'Edad': edad, 'Estado civil': estado_civil, 'Contrasena': contrasena})
                                    escribir_archivo(ruta_archivo, datos)
                                elif opt == 2:
                                    break
                                else:
                                    print('Opcion no valida')

                    elif opt == 2:
                        user = input('Introduzca su nombre de usuario:\n ->  ')
                        if len(user) == 8:
                            if user not in datos:
                                try:
                                    opt = int(input('Nombre de usuario no encontrado, ¿Desea crear una cuenta?\n  1. Si\n  2. No\n ->'))
                                except ValueError:
                                    print('Por favor, introduce un número entero válido.\n')
                                else:
                                    if opt == 1:
                                        nif = input('Introduzca su NIF:\n ->  ')
                                        nombre = input('Introduzca su nombre completo:\n ->  ')
                                        edad = int(input('Introduzca su edad:\n ->  '))
                                        while True:
                                            estado_civil = input('Introduzca su estado civil (casad@, divorciad@, viud@, solter@):\n ->  ')
                                            if estado_civil in ['casad@', 'divorciad@', 'viud@','solter@']:
                                                break
                                            else:
                                                print('Por favor, introduce un estado civil válido.\n')
                                        contrasena = reversed(nif)
                                        datos.append({'NIF': nif, 'Nombre de Usuario': user, 'Nombre completo': nombre, 'Edad': edad, 'Estado civil': estado_civil, 'Contrasena': contrasena})
                                        escribir_archivo(ruta_archivo, datos)
                                    elif opt == 2:
                                        break

                                    else:
                                        print('Opcion no valida')
                        else:
                            print('El nombre de usuario debe tener 8 caracteres.\n')
                    elif opt == 0:
                        break
        elif opt == 0:
            print('Saliendo...\n')
            break
        else:
            print('Por favor, introduce un número entero válido.\n')