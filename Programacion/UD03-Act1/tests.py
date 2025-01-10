def es_posicion_valida(posicion):
    '''
    Verifica que la fila esté entre 1 y 8, y la columna entre A y H.
    '''
    if len(posicion) != 2:
        return False
    
    fila, columna = posicion
    
    if not (1 <= fila <= 8):
        return False
    
    if columna not in 'ABCDEFGH':
        return False
    return True

def puedecomer(pieza1, pieza2, color='blancas'):
    '''
    Verifica si la pieza1 puede comer a la pieza2 según las reglas del ajedrez.
    '''
    def columna_a_numero(columna):
        alphabet = "ABCDEFGH"
        for i, letra in enumerate(alphabet, start=1):
            if letra == columna.upper():
                return i
        raise ValueError("Columna inválida")

    figura1, (fila1, col1) = pieza1
    figura2, (fila2, col2) = pieza2

    col1 = columna_a_numero(col1)
    col2 = columna_a_numero(col2)

    if figura1 == 'peón':
        if color == 'blancas':
            if fila1 < fila2:  # Peón blanco avanza hacia adelante
                return abs(fila2 - fila1) == 1 and abs(col2 - col1) == 1
        elif color == 'negras':
            if fila1 > fila2:  # Peón negro avanza hacia adelante
                return abs(fila2 - fila1) == 1 and abs(col2 - col1) == 1
    elif figura1 == 'torre':
        return fila1 == fila2 or col1 == col2
    elif figura1 == 'caballo':
        return (abs(fila1 - fila2), abs(col1 - col2)) in [(2, 1), (1, 2)]
    elif figura1 == 'alfil':
        return abs(fila1 - fila2) == abs(col1 - col2)
    elif figura1 == 'reina':
        return fila1 == fila2 or col1 == col2 or abs(fila1 - fila2) == abs(col1 - col2)
    elif figura1 == 'rey':
        return max(abs(fila1 - fila2), abs(col1 - col2)) == 1
    return False

def solicitar_pieza():
    '''
    Solicita una pieza y su posición al usuario y valida la entrada.
    '''
    figuras_validas = ['peón', 'torre', 'caballo', 'alfil', 'reina', 'rey']

    while True:
        entrada = input("Introduce la pieza y su posición (figura,fila,columna): ")
        try:
            figura, fila, columna = entrada.split(',')
            figura = figura.strip().lower()
            fila = int(fila.strip())
            columna = columna.strip().upper()

            if figura in figuras_validas and es_posicion_valida((fila, columna)):
                return figura, (fila, columna)
            else:
                print(f"Entrada inválida. Reintenta.\nPiezas válidas: {figuras_validas}")
        except ValueError:
            print("Formato incorrecto. Asegúrate de separar los datos con comas y usar el formato correcto.")

def programa():
    '''
    Programa principal para probar la función puedecomer.
    '''
    while True:
        print("Introduce los datos de las piezas:")
        pieza1 = solicitar_pieza()
        pieza2 = solicitar_pieza()

        color = input("Introduce el color de la pieza 1 (blancas/negras, por defecto blancas): ").strip().lower()
        if color not in ['blancas', 'negras', '']:
            print("Color inválido. Usando 'blancas' por defecto.")
            color = 'blancas'

        resultado = puedecomer(pieza1, pieza2, color or 'blancas')
        print(f"La pieza {pieza1[0]} en {pieza1[1]} {'puede' if resultado else 'no puede'} comer a la pieza {pieza2[0]} en {pieza2[1]}.")

        continuar = input("¿Quieres probar con otras piezas? (sí/no): ").strip().lower()
        if continuar == 'no':
            print("Gracias por jugar.")
            break

# Ejecutar el programa
programa() 