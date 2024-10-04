# Una variación del ejercicio del código de César visto en clase, es el que se describe a continuación.

# Como sabemos el código de César se caracteriza por sumar un valor (la clave) a la posición de un caracter para obtener el caracter cifrado. Para este ejercicio, esto
# se va a modificar un poco.

# El proceso de obtener el caracter cifrado es el siguiente:
# Supongamos el siguiente alfabeto

#                   abcdefghijklmnñopqrstuvwxyz

# El caracter cifrado de un caracter es el caracter que ocupa la misma posición de éste pero contando de derecha a izquierda. Pongamos varios ejemplos
# El caracter cifrado de la ‘a’ es ‘z’, el de la ‘b’ es ‘y’, elde la ‘c’ es ‘x’ y asi sucesivamente.
# Modifique el programa de encriptado y desencriptado que se realizó en clase para que ahora aplique este nuevo método de encriptación.

ALFABETO = "abcdefghijklmnñopqrstuvwxyz"
TAMAÑO = len(ALFABETO) 

mensaje = input("Introduzca un mensaje: ")
operacion = input("(C)ifrar o (D)escifrar: ").upper()
try:
    clave = int(input("Introduzca la clave: "))
except:
    print("Error...la clave debe ser un valor entero")
else:
    if operacion == "C":             # cifrar el mensaje
        mje_cifrado = ''
        pos_letra_mensaje = 0
        tamaño_mensaje = len(mensaje)
        while pos_letra_mensaje < tamaño_mensaje:
            if mensaje[pos_letra_mensaje] in ALFABETO:
                posicion = ALFABETO.find(mensaje[pos_letra_mensaje])
                nva_posicion = (posicion - clave) % TAMAÑO
                mje_cifrado += ALFABETO[nva_posicion]
            else:
                mje_cifrado += mensaje[pos_letra_mensaje]
            pos_letra_mensaje += 1
        print(f"El mensaje cifrado es: {mje_cifrado}")
            
    elif operacion == "D":          # descifrar el mensaje
        mje_claro = ''
        pos_letra_mensaje = 0
        tamaño_mensaje = len(mensaje)
        while pos_letra_mensaje < tamaño_mensaje:
            if mensaje[pos_letra_mensaje] in ALFABETO:
                posicion = ALFABETO.find(mensaje[pos_letra_mensaje])
                nva_posicion = (posicion + clave) % TAMAÑO
                mje_claro += ALFABETO[nva_posicion]
            else:
                mje_claro += mensaje[pos_letra_mensaje]
            pos_letra_mensaje += 1
        print(f"El mensaje descifrado es: {mje_claro}")
    else:
        print("Error...Opción inválida")
finally:
    print("...fin de ejecución\n")