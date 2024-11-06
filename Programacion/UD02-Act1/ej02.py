# Escriba un programa en Python para comprobar si la lista contiene tres números
# comunes consecutivos.
# Lista : [4, 5, 5, 5, 3, 8]
# La salida debe ser [5]
# Lista : [1, 1, 1, 64, 23, 64, 22, 22, 22]
# La salida debe ser: [1,22]

try:
    lista = []
    while True:
        opt = input('Introduce los números de la lista, o escriba "fin" para terminar de escribir ->     ').lower()         # Se le pide al usuario rellenar la lista
        if opt == 'fin':                                                                                                    # Si la selección del usuario es "fin", se cierra el bucle
            break
        lista.append(int(opt))                                                                                              # Si la selección del usuario es un entero, se añade a la lista

except:
    print('Selección inválida...')                                                                                          # Gestor de errores

else:
    lista_completa = []                                                                                                     # La lista con los caracteres que se repiten 3 veces, se pueden repetir. Si se repite, por ejemplo, 6 veces

    num_encontrado = -632763712                                                                                             # Esto luego se reemplaza, se coloca un número largo para reducir las probabilidades de que el usuario ingrese este número de manera inintencionada
    contador = 1                                                                                                            # El contador, para saber cuantas veces se ha encontrado un número

    for i in lista:
        # print (f'i es {i} y contador es {contador}')
        # print()
        if i == num_encontrado:                                                                                             # Si el número iterado es igual al número encontrado de la iteración anterior, se añade 1 al contador y se pasa a la siguiente iteración
            contador = contador + 1
        
        else:                                                                                                               # Si no se repite, se coloca el contador de nuevo a uno y se añade el número iterado a num_encontrado
            contador = 1
            num_encontrado = i

        
        if contador == 3:                                                                                                   # Si contador es 3, es decir, si el número ha aparecido 3 veces, se añade a la lista_completa
            contador = 1
            lista_completa.append(i)
    if lista_completa:
        print(f'Numeros repetidos más de tres veces consecutivamente: {lista_completa}')                                    # Si lista_completa NO está vacía, se imprime el resultado
    
    else:
        print('No hay números que se repiten consecutivamente 3 veces')                                                     # Si lista_completa está vacía, no se imprime el resultado