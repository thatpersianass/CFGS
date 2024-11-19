# Una empresa de comidas fast-food quiere implementar un programa para llevar información de sus platos y los ingredientes que estos contienen.

# El valor de cada clave es una lista que contiene diccionarios con los platos que ofrece el restaurante. Estos diccionarios tienen dos claves: plato e ingredientes el
# primero representa el nombre del plato y el segundo una lista de los ingredientes que contiene.

# La empresa quiere tener un menú como el siguiente:
# 1. Añadir plato.
# 2. Buscar platos por ingredientes
# 3. Eliminar plato.
# 4. Salir
import time
import os
import random

comidas = {}

# Menú

while True:
    print(f'Seleccione una opción con los números indicados abajo:\n1. Añadir plato\n2. Buscar platos por ingredientes\n3. Eliminar plato\n4. Ver Menú\n0. Salir')
    try:
        opt = int(input('-->   '))
    except:                                                                                                                                                             # Si el usuario no ingresa un número entero, se muestra un mensaje de error.
        print('La selección tiene que ser un número entero....')
        print()

    else:
        if 0 <= opt <= 4:                                                                                                                                               # Si la opción es válida (0-4), se continúa con la lógica.


#           Opcion 1
            if opt == 1:
                ingredientes = []                                                                                                                                       # Se inicializa la lista de ingredientes vacía.
                plato = input(f'Introduce el nombre del plato a añadir \n-->   ')
                categoria = input(f'Introduce la categoría del plato a añadir \n-->   ')

                if len(plato) != 0 and len(categoria) != 0:                                                                                                             # Se verifica que el nombre del plato y la categoría no estén vacíos.
                    if categoria not in comidas:                                                                                                                        # Si la categoría no existe en el diccionario "comidas", se crea una nueva categoría.
                        comidas[categoria] = []

                    if not any(item['plato'] == plato for item in comidas[categoria]):                                                                                  # Si el plato no existe ya en la categoría.
                        while True:                                                                                                                                     # Se entra en un bucle para pedir ingredientes hasta que el usuario presione ENTER sin agregar ninguno.
                            i = input('Introduzca un ingrediente, presione ENTER para finalizar\n-->   ')

                            if i == '':
                                if len(ingredientes) > 0:                                                                                                               # Se verifica que haya al menos un ingrediente.
                                    break
                                else:
                                    print("Debe ingresar al menos un ingrediente...")                                                                                   # Si no hay ingredientes, se muestra un mensaje de error.
                                    print()

                            ingredientes.append(i)                                                                                                                      # Se agrega el ingrediente a la lista.

                        comidas[categoria].append({'plato': plato, 'ingredientes': ingredientes})                                                                       # Se añade el plato con su lista de ingredientes a la categoría.

                        print(f'Plato "{plato}" añadido a la categoría "{categoria}" con los ingredientes {ingredientes}.\n')

                    else:
                        print('El plato ya existe... ')                                                                                                                 # Si el plato ya existe en la categoría, se muestra un mensaje de error.
                        print()
                else:
                    print(f'Ni el nombre del plato ni la categoría pueden estar vacíos... \n')                                                                          # Si el plato o la categoría están vacíos, se muestra un mensaje de error.


#           Opcion 2
            elif opt == 2:
                if not comidas:                                                                                                                                         # Si no hay platos en el menú, se muestra un mensaje de error.
                    print("No hay platos en el menú.\n")
                else:
                    ingredientes_buscar = []
                    while True:
                        ingrediente = input(f'Introduce un ingrediente o presiona ENTER para terminar\n-->   ')
                        if ingrediente == '':
                            break
                        ingredientes_buscar.append(ingrediente)                                                                                                         # Se agrega el ingrediente a la lista.

                    encontrados = False                                                                                                                                 # Se inicializa la variable que indicará si se encontraron platos que coincidan.
                    for categoria, platos in comidas.items():                                                                                                           # Se recorre cada categoría y sus platos.
                        for plato in platos:
                            if all(i in plato['ingredientes'] for i in ingredientes_buscar):                                                                            # Si todos los ingredientes solicitados están en el plato.
                                print(f"En la categoría '{categoria}' el plato '{plato['plato']}' con ingredientes {plato['ingredientes']}.\n")
                                encontrados = True                                                                                                                      # Se marca como encontrado.

                    if not encontrados:                                                                                                                                 # Si no se encontraron platos con todos los ingredientes solicitados, se muestra un mensaje.
                        print("No hay platos que contengan todos los ingredientes solicitados.\n")


#           Opcion 3
            elif opt == 3:
                if comidas:                                                                                                                                             # Si hay platos en el menú.
                    print("Estas son las categorías disponibles:")                                                                                                      # Se muestra una lista de categorías.
                    for categoria in comidas:
                        print(categoria)

                    categoria = input("Introduce la categoría del plato a eliminar\n-->   ")

                    if categoria in comidas and comidas[categoria]:                                                                                                     # Si la categoría existe y tiene platos.
                        print(f"\nPlatos disponibles en la categoría '{categoria}'\n-->   ")
                        for item in comidas[categoria]:
                            print(f"- {item['plato']} - Ingredientes: {', '.join(item['ingredientes'])}")                                                               # Se imprimen los platos disponibles.

                        plato_a_eliminar = input(f"Introduce el nombre del plato a eliminar de la categoría '{categoria}', o presiona ENTER para salir\n-->    ")

                        if plato_a_eliminar != "":                                                                                                                      # Si el nombre del plato no está vacío.
                            plato_encontrado = None                                                                                                                     # Inicializamos la variable que almacenará el plato encontrado.
                            for item in comidas[categoria]:
                                if item['plato'] == plato_a_eliminar:                                                                                                   # Si el plato existe en la categoría.
                                    plato_encontrado = item
                                    break

                            if plato_encontrado:                                                                                                                        # Si el plato fue encontrado, se elimina.
                                comidas[categoria].remove(plato_encontrado)                                                                                             # Se elimina el plato de la lista de la categoría.
                                print(f"El plato '{plato_a_eliminar}' ha sido eliminado de la categoría '{categoria}'.\n")
                            else:
                                print(f"No se encontró el plato '{plato_a_eliminar}' en la categoría '{categoria}'.\n")                                                 # Si no se encontró el plato, se muestra un mensaje de error.
                        else:
                            print("Operación cancelada.\n")                                                                                                             # Si el usuario presiona ENTER sin ingresar el nombre del plato, se cancela la operación.
                    else:
                        print(f"No hay platos en la categoría '{categoria}' o la categoría no existe.\n")                                                               # Si la categoría no existe o no tiene platos, se muestra un mensaje de error.
                else:
                    print("No hay platos disponibles en el menú.\n")                                                                                                    # Si no hay platos en el menú, se muestra un mensaje de error.


#           Opcion 4
            elif opt == 4:                                                                                                                                              # Si la opción seleccionada es 4 (Ver Menú).
                if not comidas:                                                                                                                                         # Si no hay platos en el menú, se muestra un mensaje de error.
                    print("No hay platos en el menú.\n")
                else:
                    for categoria, platos in comidas.items():                                                                                                           # Se recorre cada categoría y sus platos.
                        print(categoria)
                        if platos:                                                                                                                                      # Si hay platos en la categoría, se imprimen.
                            for plato in platos:
                                print(f"  - {plato['plato']}: {', '.join(plato['ingredientes'])}")
                        else:
                            print(f"  No hay platos en la categoría '{categoria}'")                                                                                     # Si no hay platos en la categoría, se indica.
                    print()


            # Opcion 0
            elif opt == 0:
                drawing = """
                        ⠟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⢻⣿
                        ⡆⠊⠈⣿⢿⡟⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣎⠈⠻
                        ⣷⣠⠁⢀⠰⠀⣰⣿⣿⣿⣿⣿⣿⠟⠋⠛⠛⠿⠿⢿⣿⣿⣿⣧⠀⢹⣿⡑⠐⢰
                        ⣿⣿⠀⠁⠀⠀⣿⣿⣿⣿⠟⡩⠐⠀⠀⠀⠀⢐⠠⠈⠊⣿⣿⣿⡇⠘⠁⢀⠆⢀
                        ⣿⣿⣆⠀⠀⢤⣿⣿⡿⠃⠈⠀⣠⣶⣿⣿⣷⣦⡀⠀⠀⠈⢿⣿⣇⡆⠀⠀⣠⣾
                        ⣿⣿⣿⣧⣦⣿⣿⣿⡏⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠐⣿⣿⣷⣦⣷⣿⣿
                        ⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⣿⣿⣿⣿⣿⣿⣿
                        ⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⣾⣿⣿⠋⠁⠀⠉⠻⣿⣿⣧⠀⠠⣿⣿⣿⣿⣿⣿⣿
                        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⣿⡿⠁⠀⠀⠀⠀⠀⠘⢿⣿⠀⣺⣿⣿⣿⣿⣿⣿⣿
                        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣠⣂⠀⠀⠀⠀⠀⠀⠀⢀⣁⢠⣿⣿⣿⣿⣿⣿⣿⣿
                        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣄⣤⣤⣔⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                """

                # Divide el dibujo en líneas
                lines = drawing.split('\n')
                height = len(lines)
                width = max(len(line) for line in lines)

                # Generar coordenadas aleatorias para cada carácter
                coords = [(x, y) for y in range(height) for x in range(len(lines[y]))]

                # Función para limpiar la consola
                def clear_console():
                    os.system('cls' if os.name == 'nt' else 'clear')

                # Mostrar el dibujo inicialmente con el texto
                clear_console()
                print("Saliendo. Borrando datos")
                for line in lines:
                    print(line)
                time.sleep(0.5)  # Mostrar el dibujo durante unos milisegundos

                # Mostrar el dibujo rompiéndose en pedazos y moviéndose hacia afuera, con texto animado
                for step in range(20):
                    clear_console()
                    print("Saliendo. Borrando datos" + "." * (step % 4))
                    new_drawing = [[" " for _ in range(width)] for _ in range(height)]
                    for x, y in coords:
                        if random.random() < step * 0.05:
                            continue
                        offset_x = random.choice([-step, step])
                        offset_y = random.choice([-step, step])
                        new_x = x + offset_x
                        new_y = y + offset_y
                        if 0 <= new_x < width and 0 <= new_y < height:
                            new_drawing[new_y][new_x] = lines[y][x]
                    for line in new_drawing:
                        print("".join(line))
                    time.sleep(0.095)

                clear_console()
                break

        else:
            print('Seleccione una opción válida... ')                                                                                                               # Si la opción no es válida (no está entre 0 y 4), se muestra un mensaje de error.
            print()
