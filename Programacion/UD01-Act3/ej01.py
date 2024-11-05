# Dada una lista, extraer todos los elementos cuya frecuencia sea superior a n. Los
# elementos de la lista deben leerse mediante un bucle del cual se sale con la
# secuencia *fin.
# Posteriormente se debe leer el valor de n.
# Ejemplos
# Lista = [4, 6, 4, 3, 0, 3, 4, 3, 0, 4, 3, 8], n = 3 

# La salida debe ser [4,3]
# Lista = [4, 6, 4, 5, 3, 3, 4, 3, 4, 1, 6, 6], n = 2
# La salida debe ser [4, 3, 6] 

try:
    lista = []
    while True:
        opt = input('Introduce los números de la lista, o escriba "fin" para terminar de escribir ->     ').lower()         # Se le pide al usuario rellenar la lista
        if opt == 'fin':                                                                                                    # Si la selección del usuario es "fin", se cierra el bucle
            break
        
        try:
            lista.append(int(opt))                                                                                              # Si la selección del usuario es un entero, se añade a la lista
        except ValueError:
            print('Por favor, introduce un número entero válido.')                                                              # Si la selección del usuario No es un entero, se repite el bucle
    
    n = int(input('Inserte un número entero ->   '))

except:
    print('Selección inválida...')                                                                                          # Gestor de errores

else:
    lista_completa = []

    for i in range(len(lista)):
        elto = lista[i]
        if elto not in lista_completa:
            cuenta = lista.count(elto)
            if cuenta > n:
                lista_completa.append(elto)

print(f'Los números que se repiten más veces que {n} son {lista_completa}')