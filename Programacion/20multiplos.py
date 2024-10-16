# calcular los 20 multiplos de un numero

num = input('Introduce un numero:    ')

if not num.isdigit():
    print('EEEEEH, no')
else:
    for i in range(1, 21):
        if i % 5 != 0:
            print(f'{int(num) * i:4d}' , end=' ')
        else:
            print(f'{int(num) * i:4d}')