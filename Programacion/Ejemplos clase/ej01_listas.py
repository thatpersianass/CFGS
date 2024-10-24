# dada una lista de temperaturas como la siguiente:

# [['Tfe',27.3,14.5],
# ['Lpa',26.2,16.3],
# ['Gom',20.3,17.3],
# ['hie',25.2,13.7]]

# temperaturas = [
#     ['Tfe', 27.3, 14.5],
#     ['Lpa', 26.2, 16.3],
#     ['Gom', 20.3, 17.3],
#     ['Hie', 25.2, 13.7]
# ]
# def temp_max():
#     temperaturas.sort(reverse=True)

# temp_max()

# for isla in temperaturas:
#     print(isla, end=' ')


temperaturas = [
    ['Tfe', 27.3, 14.5],\
        ['Lpa', 26.2, 16.3],\
            ['Gom', 2.3, 17.3],\
                ['Hie', 25.2, 13.7]]

ordenado = []

lugar_max = [temperaturas[0][0]]
max_temp = temperaturas[0][1]

lugar_min = [temperaturas[0][0]]
min_temp = temperaturas[0][2]

for datos in temperaturas:
    if datos[1] > max_temp:
        max_temp = datos[1]
        lugar_max = datos[0]

    if datos[2] < min_temp:
        max_temp = datos[2]
        lugar_max = datos[0]
    
    if datos[1] == max_temp:
        lugar_max = lugar_max.append(datos[0])
    
    if datos[2] == min_temp:
        lugar_min = lugar_min.append(datos[0])

print(f'La temperatura máxima es {max_temp} en {lugar_max}')
print(f'La temperatura mínima es {min_temp} en {lugar_min}')
