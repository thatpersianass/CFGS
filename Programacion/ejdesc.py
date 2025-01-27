import os

path_dir_trabajo = os.path.join(os.getcwd(),"ficheros")
os.chdir(path_dir_trabajo)
print(f"La ruta del directorio de trabajo:\n-->{os.getcwd()}")

nombre = input('Indique el nombre a buscar: ')

if os.path.exists(nombre):
    if os.path.isdir(nombre):
        print(f"{nombre} es un archivo.")
    else:
        print(f"{nombre} es un directorio.")