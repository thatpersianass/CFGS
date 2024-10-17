# Verificar si un numero es magico, sumar todos sus divisores y si son igual al numero, es mágico

try:
    num = int(input('Introduzca un numero -->'))

except:
    print('Numero invalido')

else:
    suma = 0

    for div in range(1, num//2 +1):
        if num % div == 0:
            suma += div

    if suma == num:
        print(f'El numero {num} es mágico')
    else:
        print(f'El numero {num} NO es mágico')