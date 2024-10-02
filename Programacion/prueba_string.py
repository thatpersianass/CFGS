import random

# Opciones del juego
opciones = ['piedra', 'papel', 'tijeras']

# Función para determinar el resultado del juego
def resultado(jugador, computadora):
    if jugador == computadora:
        return "¡Empate!"
    elif (jugador == 'piedra' and computadora == 'tijeras') or \
         (jugador == 'tijeras' and computadora == 'papel') or \
         (jugador == 'papel' and computadora == 'piedra'):
        return "¡Ganaste!"
    else:
        return "Perdiste..."

# Loop del juego
while True:
    print("Elige: piedra, papel o tijeras (o 'salir' para terminar)")
    jugador = input("Tu elección: ").lower()

    if jugador == 'salir':
        print("Gracias por jugar. ¡Hasta luego!")
        break

    if jugador not in opciones:
        print("Elección inválida. Intenta de nuevo.")
        continue

    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")

    # Mostrar el resultado
    print(resultado(jugador, computadora))
