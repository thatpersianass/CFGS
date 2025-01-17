# try:
#     fichero = open('dir_trab/fichero02.txt','r')
#     textoaux = fichero.readlines()
#     for linea in textoaux[:-1]:
#         print(linea[:-1])
#     print(textoaux[-1])
# except:
#     print('Error al abrir el fichero')

# else:
#     print('Fin de la ejecicion')

def contar_numeros_y_letras():
    nombre_fichero = 'dir_trab/coocoo.txt'
    try:
        with open(nombre_fichero, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()

        contador_numeros = sum(1 for c in contenido if c.isdigit())
        contador_letras = sum(1 for c in contenido if c.isalpha())

        print(f"Cantidad de números: {contador_numeros}")
        print(f"Cantidad de letras: {contador_letras}")

    except FileNotFoundError:
        print(f"El fichero '{nombre_fichero}' no existe. Por favor, verifica el nombre y la ruta.")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

contar_numeros_y_letras()
