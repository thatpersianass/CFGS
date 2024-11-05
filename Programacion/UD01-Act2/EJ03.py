    # Escribir un programa en Python que permita desarrollar un juego de adivinar palabras con las características siguientes.

    # El programa comienza pidiendo una palabra al usuario de al menos 3 letras. Se debe verificar la longitud de la palabra leída y dar error si no se cumple pero el
    # programa no termina. En esta ejercicio se debe continuar leyendo hasta que se cumpla con la condición.

    # Una vez leída la palabra, comienza el juego. Supongamos que nuestra palabra es ‘zapato’.

    # Para mostrar los resultados que va obteniendo se debe generar un string de `+ ’ de la misma longitud que la palabra leída. ‘+ + + + + + ’.

    # Ahora se pide una letra al jugador, si esta aparece una o más veces en la palabra se debe cambiar en el string de resultados los ‘+’ por la letra leída en las mismas
    # posiciones en la que se encuentra en la palabra original. En el ejemplo si se ha leído ’t’ entonces el string de respuesta debe ser ‘+ + + + t + ’. La letra leída se
    # debe añadir a otro string en el que se almacenan todas las letras usadas.

    # En el caso de que no se encuentre la letra en el string sólo se debe añadir a un string de letras usadas.

    # Se debe tener en cuenta que en el string de letras usadas no deben aparecer letras repetidas.

    # El jugador dispone de 7 intentos para adivinar la palabra.


intentos_max = 7                                                                                        # Define el número de intentos para adivinar la palabra, se coloca en una variable para ser más fácil de modificar


while True:
    palabra = input("Introduzca la palabra a adivinar (mínimo 3 letras): ").upper()                     # Pide una palabra, de más de 3 letras de largo y lo convierte en Mayúsculas
    if len(palabra) >= 3:                                                                               # Verifica si la palabra tiene más de 3 letras
        break
    print("LA PALABRA DEBE TENER MÁS DE 3 LETRAS")                                                      # Si no tiene más de 3 letras, muestra el mensaje de aviso y vuelve a preguntar la palabra


progreso = ['_' if c != ' ' else ' ' for c in palabra]                                                  # Inicializa la representación de la palabra parcial, reemplaza letras por '_' y mantiene espacios

letras_usadas = ''                                                                                      # String de letras usadas
intentos_restantes = intentos_max                                                                       # Inicializa los intentos restantes


def mostrar_estado():                                                                                   # Definir el estado del juego, como las letras usadas y los intentos restantes. Se hace así para simplificar el código
    print(f"Palabra parcial: {' '.join(progreso)}")  
    print(f"Intentos restantes: {intentos_restantes} - letras usadas: '{letras_usadas}'")  


while intentos_restantes > 0:                                                                           # Inicia el Juego
    mostrar_estado()
    
    letra = input("Indique letra a jugar -> ").upper()                                                  # Lee la letra del jugador, y la convierte en mayúsculas

    
    if len(letra) != 1:                                                                                 # Validar que se haya introducido solo una letra
        print("SOLO PUEDES ADIVINAR UNA LETRA A LA VEZ")
        continue

    
    if letra in letras_usadas:                                                                          # Verificar si la letra ya fue usada
        print(f"La letra '{letra}' ya ha sido usada")
        continue

    letras_usadas += letra                                                                              # Añadir la letra a letras_usadas (evitar letras repetidas)


    if letra in palabra:                                                                                # Verificar si la letra está en la palabra
        for i in range(len(palabra)):                                                                   # Reemplazar los '_' en las posiciones correctas con la letra adivinada
            if palabra[i] == letra:
                progreso[i] = letra
    else:                                                                                               # Restar un intento si la letra no está en la palabra
        intentos_restantes -= 1

    if ''.join(progreso).replace(" ", "") == palabra.replace(" ", ""):                                  # Verificar si se ha adivinado toda la palabra
        mostrar_estado()
        print("HAS ADIVINADO LA PALABRA")
        break
else:                                                                                                   # Si se acaban los intentos, el jugador pierde
    print(f"El jugador ha perdido. La palabra es: {palabra}")

#  Se han usado los '_' en lugar de '+' por cuestiones estéticas, mas no influye en el funcionamiento del juego