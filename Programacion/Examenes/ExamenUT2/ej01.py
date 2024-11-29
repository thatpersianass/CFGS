# Una lista se considera capicúa si los elementos que la conforman mantienen el
# mismo orden recorridos de izquierda a derecha como de derecha a izquierda. 

# Una lista se considera suma-capicúa si todos los elementos que están en la parte
# izquierda están en la parte derecha en otro orden (sino sería capicúa) y la suma de
# los valores sellado izquierdo es la misma que la suma de valores de la mitad
# derecha.

# Escriba un programa en Python que dada una lista verifique si es suma-capicúa

lista = [1,2,8,2,1]                                             # Lista dada para verificar
lista2 = [2,1,8,2,1]

lista1_capi = True                                              # Todo el mundo es inocente hasta que se demuestre lo contrario
lista2_capi = True

lita_valida = True
lista_suma = []
lista_suma2= []
iter = 1

for k in lista:                                                 # Verificar si hay caracteres invalidos en la lista
    try:
        k + 1
    except:
        lita_valida = False
        break

for k in lista2:                                                 # Verificar si hay caracteres invalidos en la lista
    try:
        k + 1
    except:
        lita_valida = False
        break
        
if lita_valida:
    if len(lista) % 2 == 0:                                     # Verificar si la longitud de la lista es par
        lista_len = int(len(lista) / 2)                         # Guarda la mitad de la longitud de la lista
        
        for i in lista:
            if iter <= lista_len:                               # Si el número de la iteración es menor que la longitud de la lista, va sumando a la primera suma
                lista_suma.append(i)
                iter += 1
            
            else:                                               # Sino, suma a la segunda suma
                lista_suma2.append(i)

    else:                                                       # En caso de ser impar, se cambia la iteración
        lista_len = int(len(lista) / 2)                         # Guarda la mitad de la longitud de la lista
        
        for i in lista:
            if iter <= lista_len:                               # Si el número de la iteración es menor que la longitud de la lista, va sumando a la primera suma
                lista_suma.append(i)
                iter += 1

            elif iter == lista_len + 1:                         # Cuando llegue al numero de la mitad, este se suma a las dos sumas
                lista_suma.append(i)
                lista_suma2.append(i)
                iter += 1
            
            else:                                               # Sino, suma a la segunda suma
                lista_suma2.append(i)

    if sorted(lista_suma) != sorted(lista_suma2):
        lista1_capi = False

    lista_suma = []
    lista_suma2 = []
    iter = 1



    if len(lista2) % 2 == 0:                                     # Verificar si la longitud de la lista es par
        lista_len = int(len(lista2) / 2)                         # Guarda la mitad de la longitud de la lista
        
        for i in lista2:
            if iter <= lista_len:                               # Si el número de la iteración es menor que la longitud de la lista, va sumando a la primera suma
                lista_suma.append(i)
                iter += 1
            
            else:                                               # Sino, suma a la segunda suma
                lista_suma2.append(i)

    else:                                                       # En caso de ser impar, se cambia la iteración
        lista_len = int(len(lista2) / 2)                         # Guarda la mitad de la longitud de la lista
        
        for i in lista2:
            if iter <= lista_len:                               # Si el número de la iteración es menor que la longitud de la lista, va sumando a la primera suma
                lista_suma.append(i)
                iter += 1

            elif iter == lista_len + 1:                         # Cuando llegue al numero de la mitad, este se suma a las dos sumas
                lista_suma.append(i)
                lista_suma2.append(i)
                iter += 1
            
            else:                                               # Sino, suma a la segunda suma
                lista_suma2.append(i)

    if sorted(lista_suma) != sorted(lista_suma2):
        lista2_capi = False
    else:
        lista_suma = []
        lista_suma2 = []

    if lista1_capi:
        print(f'La lista 1 es capicúa\n{lista}')
    
    else:
        print(f'La lista 1 no es capicúa\n{lista}')

    if lista2_capi:
        print(f'La lista 2 es capicúa\n{lista2}')
    else:
        print(f'La lista 2 no es capicúa\n{lista2}')

else:
    print('Hay caracteres que no son enteros en la lista, por favor, eliminelos y vuelva a ejecutar el programa...')