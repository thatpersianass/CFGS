# Se quiere simular un juego en el que participan N jugadores y otra persona que
# hace de árbitro. Cada jugador elige 4 números en el rango [1, 10], pudiendo estar
# repetidos. A continuación, el árbitro, sin conocer los números que ha elegido cada
# jugador, selecciona 2 números A y B.


# El programa debe ser capaz de calcular cuántos números de los seleccionados
# por cada jugador están comprendidos entre los valores A y B. Ganará el jugador
# que más números tenga en dicho intervalo.


# Se pide implementar un programa modular que simule el juego para 3 jugadores,
# teniendo en cuenta que:

# Tanto los 4 datos de cada jugador, como los valores para A y B se introducirán por
# teclado. En todos los casos, el programa detectará la entrada de números
# erróneos, solicitando nuevamente el dato hasta que sea válido.

# Se deben mostrar por pantalla no solo los aciertos de cada jugador sino los datos
# que ha introducido cada jugador y los que ha seleccionado el árbitro. Por último,
# hay que imprimir la media aritmética de los aciertos de todos los jugadores

jugadores = [[],[],[]]
aciertos = [0,0,0]
arbitro = []
ganadores = []

for i in range(3):                                                                                                  # Itera el número de jugadores
    while True:
        try:
            opt = int(input(f'Jugador {i + 1},\nintroduzca 4 números enteros entre el 1 y el 10 --> '))

        except ValueError:                                                                                          # Gestor de errores
            print('El caracter introducido no es un número entero...')

        else:
            if 1 <= opt <= 10:                                                                                      # Si está dentro del rango, se añade a la lista del jugador
                jugadores[i].append(opt)
            else:
                print("Número fuera del rango...")
            
            if len(jugadores[i]) == 4:                                                                              # Verifica que el jugador ya haya introducido sus 4 números
                break

# Comienzo del Juego
print()

while True:                                                                                                         # Pide los números a adivinar del arbitro
    try:
        a = int(input('Arbitro,\nintroduzca un número entre 1 y 10 como su opción A -->     '))

        b = int(input('Arbitro,\nintroduzca un número entre 1 y 10 como su opción B -->     '))
    
    except:
        print('El caracter introducido no es un número entero...')                                                  # Gestor de errores

    else:
        if 1 <= a <= 10 and 1 <= b <= 10:                                                                           # Si está dentro del rango, se añade a la lista del arbitro
            if a < b:
                arbitro.extend([a,b])
                break
            else:
                print('Los números no forman un rango válido...')
        
        else:
            print('Los números no se encuentran en el rango especificado...')
            print()

for i in range(len(jugadores)):                                                                                     # Se itera el número del jugador, para ir verificando cuál fallo o acertó el número
    jugador_numero = i + 1
    for num in jugadores[i]:
            if a <= num <= b:                                                                                       # Se verifica que el jugador no haya ganado anteriormente, si lo hizo, se le agrega uno a su contador de aciertos
                aciertos[i] += 1

if sum(aciertos) > 0:                                                                                               # Si hay al menos 1 acierto entre todos los jugadores, se imprimen las elecciones de los jugadores y sus aciertos
    print(f'Jugador 1: {jugadores[0]}, ha acertado {aciertos[0]} números')
    print(f'Jugador 2: {jugadores[1]}, ha acertado {aciertos[1]} números')
    print(f'Jugador 3: {jugadores[2]}, ha acertado {aciertos[2]} números')
    print(f'\nEl rango del arbitro fue entre {arbitro[0]} y {arbitro[1]}')

else:                                                                                                               # Si no hay aciertos, se imprimen las elecciones de los jugadores
    print('Ningún jugador adivinó el número del arbitro')
    print(f'\nJugador 1: {jugadores[0]}')
    print(f'Jugador 2: {jugadores[1]}')
    print(f'Jugador 3: {jugadores[2]}')
    print(f'\nEl rango del arbitro fue entre {arbitro[0]} y {arbitro[1]}')

print()

media_aciertos = sum(aciertos) / len(aciertos)                                                                      # Se calcula la media de aciertos, y se limitan los decimales a dos
print(f'La media de aciertos fue: {media_aciertos:.2f}')
print()