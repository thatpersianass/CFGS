import time
import os
import random

# Configura tu dibujo aquí
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
    time.sleep(0.1)

clear_console()
