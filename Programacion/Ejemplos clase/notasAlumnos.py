# Almacenar datos de los alumnos de 1ro DAM
#  alumnos = [(Nombre,[bae,pro,lnd,ets,ssf,djk,itk,jkl])]

alumnos = []
asignaturas = ('BAE','PRO','LND','ETS','SSF','DJK','ITK','JKL')
medias = []

while True:
    nombre = input('Cuál es tu nombre? (Si desea salir, escriba @) -->     ')

    if nombre == '@':
        break

    else:
        tupla = (nombre,[])

    for i in range(len(asignaturas)):
        if nombre == '@':
            break

        else:
            while True:
                try:
                    nota = int(input(f'Inserte la nota ponderada de {asignaturas[i]} del alumno -->     '))
                    
                except:
                    print('Entrada inválida...')
                    
                else:
                    if 0 <= nota <= 10:
                        tupla[1].append(nota)
                        break

                    if nota.upper == 'NO':
                        tupla[1].append(nota)
                    else:
                        print('Entrada inválida...')

    for k in range(len(tupla[1])):
        if tupla[1][k] == 'NO':
            continue
    
    alumnos.append(tupla)

for i in range(len(alumnos)):
    print(f'El alumno {alumnos[i][0]}, con las notas {alumnos[i][1]}, tiene una media de {medias[i]}')