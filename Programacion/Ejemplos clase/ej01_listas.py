# dada una lista de temperaturas como la siguiente:

# temperaturas = [
#     ['Tfe', 27.3, 14.5],\
#         ['Lpa', 26.2, 16.3],\
#             ['Gom', 24.3, 17.3],\
#                 ['Hie', 25.2, 13.7]]

# ordenado = []

# lugar_max = [temperaturas[0][0]]
# max_temp = temperaturas[0][1]

# lugar_min = [temperaturas[0][0]]
# min_temp = temperaturas[0][2]

# for datos in temperaturas:
#     if datos[1] > max_temp:
#         max_temp = datos[1]
#         lugar_max = datos[0]

#     if datos[2] < min_temp:
#         min_temp = datos[2]
#         lugar_min = datos[0]

# print(f'La temperatura máxima es {max_temp} en {lugar_max}')
# print(f'La temperatura mínima es {min_temp} en {lugar_min}')

temperaturas = [['tfe',25.3, 14.5],\
                ['lpa',26.2, 16.3],\
                    ['gom',27.3, 17.3],\
                        ['hie',25.2, 13.7],\
                            ['gca',27.3, 15.7],\
                                ['fue',27.2, 16.7],\
                                    ['lnz',25.8, 14.7],\
                                        ['lgr',24.2, 13.7] ]

lugar_max = [ temperaturas[0][0] ]
max_temp = temperaturas[0][1]

lugar_min = [temperaturas[0][0]]
min_temp = temperaturas[0][2]

for datos in temperaturas[1:]:
    if datos[1] > max_temp:
        max_temp = datos[1]
        lugar_max = datos[0]

    elif datos[1] == max_temp:
        if datos[0] not in lugar_max:
            lugar_max.append(datos[0])

    if datos[2] < min_temp:
        min_temp = datos[2]
        lugar_min = datos[0]

    elif datos[1] == min_temp:
        if datos[0] not in lugar_min:
            lugar_min.append(datos[0])

print(f'La temperatura máxima es {max_temp} en:', end=' ')
# print(f'La temperatura mínima es {min_temp} en {lugar_min}')

for isla in lugar_max:
    print(isla, end=' ')

print()

# print(f'La temperatura máxima es {max_temp} en:', end=' ')
print(f'La temperatura mínima es {min_temp} en:', end=' ')

for isla in lugar_min:
    print(isla, end=' ')

print()