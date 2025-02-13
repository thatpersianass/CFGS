# Se tiene un CSV con informacion de productos de un almacen. Cada fila representa un producto con los siguientes campos:
# ID: identificador del producto, unico
# Nombre del producto
# categoria del producto
# precio del producto
# stock del producto

# se tiene que escribir un programa en python que implemente la siguiente funcion:
# convertirCSV2JSON(csv_filename, json_filename, categoria_filtro) que:

#  Lea los datos del archivo CSV
#  Filtre solo los productos de la categoria especificada en categoria_filtro
#  Guarde los productos filtrados en un archivo JSON, donde cada producto debe representarse como un diccionario

# Datos de ejemplo
# ID,Nombre,Categoria,Precio,Stock

import json
import os

productos = []

directorio_actual = os.getcwd()

dir_csv = os.path.join(directorio_actual, 'entrada.csv')

dir_json = os.path.join(directorio_actual, 'salida.json')


def convertirCSV2JSON(csv_filename:str, json_filename:str, categoria_filtro:str) -> str:
    try:
        file = open(csv_filename, "r")
    except FileNotFoundError:
        print("El archivo csv no fue encontrado.")
        return None
    except:
        print("Ocurrió un error al leer el archivo csv.")
        return None
    else:
        csv_cont = file.read()
        csv_cont = csv_cont.split('\n')

    for i in csv_cont:
        if i!= '':
            datos = i.split(',')
            if datos[2] == categoria_filtro:
                productos.append({'ID': datos[0], 'Nombre': datos[1], 'Categoria': datos[2], 'Precio': float(datos[3]), 'Stock': int(datos[4])})



    try:
        file = open(json_filename, "w")
    except FileNotFoundError:
        print("El archivo json no fue encontrado.")
        return None
    except:
        print("Ocurrió un error al crear o abrir el archivo json.")
        return None
    else:
        json.dump(productos, file, indent=4)
        print('Productos agregados de manera exitosa al archivo JSON')

print(directorio_actual)

categoria = input('Ingrese la categoría que se desea\n -->  ')

print(convertirCSV2JSON(dir_csv, dir_json, categoria))