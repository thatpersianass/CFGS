import json
import os

directorio_actual = os.getcwd()
archivo = os.path.join(directorio_actual, 'tareas.json')
print(directorio_actual)
# archivo = 'tareas.json'

def cargar_tareas():
    try:
        with open(archivo, 'r') as f: # Se abre el archivo en modo lectura
            return json.load(f) # Convertir los datos json a una lista de diccionarios
        
    except FileNotFoundError: # Si el archivo no se encuentra se asume que no existe y se crea uno nuevo
        print(f"El archivo {archivo} no existe. Se creará uno nuevo.")
        return []
    
    except: # En tal caso de surgir algún otro error, se ensñará este mensaje generico
        print('Ocurrió un error al intentar cargar el archivo...')
        return []

def guardar_tareas(tareas):
    with open(archivo, 'w') as f:
        json.dump(tareas, f, indent=4) # Se usan 4 tabuladores para hacer el archivo JSON más comodo de leer para el usuario

def agregar_tarea(): # Se piden los datos al usuario para poder agregarlos al archivo
    nombre = input("Ingrese el nombre de la tarea: ")
    fecha_limite = input("Ingrese la fecha límite (DD-MM-YYYY): ")
    tareas = cargar_tareas() # Se cargan las tareas ya existentes, ya que se va a sobreescribir todo el contenido del archivo
    tareas.append({"nombre": nombre, "fecha_limite": fecha_limite, "estado": "pendiente"}) # Se agregan los nuevos datos a la lista
    guardar_tareas(tareas) # Se ejecuta la función para guardar las tareas
    print("Tarea añadida correctamente.")

def modificar_estado(): 
    nombre = input("Ingrese el nombre de la tarea a modificar: ") # se pide el nombre de la tarea
    tareas = cargar_tareas() # Se cargan todas las tareas en una lista
    for tarea in tareas:
        if tarea['nombre'] == nombre: # Si se encuentra la tarea solicitada, se cambia el estado a completado, en el caso opuesto, se le notifica al usuario
            tarea['estado'] = 'completada'
            guardar_tareas(tareas)
            print("Estado de la tarea modificado a 'completada'.")
            return
    print("Tarea no encontrada.")

def eliminar_tarea(): 
    nombre = input("Ingrese el nombre de la tarea a eliminar (solo completadas serán eliminadas): ") # Se solicita el nombre de la tarea al usuario, y se le notifica que solo aquellas que estén completadas se borrarán
    tareas = cargar_tareas()
    tareas = [tarea for tarea in tareas if not (tarea['nombre'] == nombre and tarea['estado'] == 'completada')]
    guardar_tareas(tareas)
    print("Tarea eliminada si estaba completada.")

def listar_tareas():
    tareas = cargar_tareas()
    if tareas: # Si la lista no está vacía, se muestran las tareas existentes
        for tarea in tareas:
            print(f"Nombre: {tarea['nombre']}, Fecha Límite: {tarea['fecha_limite']}, Estado: {tarea['estado']}")
    else:
        print("No hay tareas registradas.")

if __name__ == '__main__':
    while True:
        print("\nSeleccione una opción con los números indicados abajo:")
        print("1. Añadir tarea")
        print("2. Modificar estado de tarea")
        print("3. Eliminar tarea")
        print("4. Listar tareas")
        print("0. Salir")
        
        try:
            opt = int(input("-->   "))
        except:
            print("La selección tiene que ser un número entero....")
        else:
            if opt == 1:
                agregar_tarea()
            elif opt == 2:
                modificar_estado()
            elif opt == 3:
                eliminar_tarea()
            elif opt == 4:
                listar_tareas()
            elif opt == 0:
                print("Terminando programa...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")