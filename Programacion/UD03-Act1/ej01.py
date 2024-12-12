# La idea es realizar un programa en Python que defina la función
# puedecomer( pieza1, pieza2 ) y que retorna un valor booleano. Este valor
# retornado será True si la pieza1 puede comer a la pieza2 y False en caso contrario.

# Definimos los parámetros de la siguiente forma.
# pieza1 y pieza2 son tuplas que tienen el siguiente formato: ( figura, posición )

# Donde

# • figura: es un string que indica una pieza del ajedrez. Los valores que puede
# tomar son los siguientes: peón, torre, caballo, alfil, reina y rey

# • posición: es una tupla con dos elementos que indican la posición de la pieza en
# el tablero de ajedrez ( fila, columna ) donde

# • fila es un valor entre 1 y 8

# • columna una letra entre A y H

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

def puedecomer(pieza1, pieza2):
    figura1, (fila1, col1) = pieza1
    figura2, (fila2, col2) = pieza2

    col1 = ord(col1.upper()) - ord('A') + 1
    col2 = ord(col2.upper()) - ord('A') + 1
    
    if figura1 == 'peón':
        if fila1 < fila2:  # Peones solo avanzan hacia adelante
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

def solicitar_pieza():
    """
    Solicita una pieza y su posición al usuario y valida la entrada.
    """
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
                print(f"Entrada inválida. Reintenta.\nPiezas váldas: {figuras_validas}")
        except ValueError:
            print("Formato incorrecto. Asegúrate de separar los datos con comas y usar el formato correcto.")

def programa():
    pass