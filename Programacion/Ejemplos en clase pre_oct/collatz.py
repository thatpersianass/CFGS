try:
    i = 0
    num = int(input('Introduzca un numero:  '))

except:
    print('No')

else:
    if num > 0:
        while num != 1:
            print(num, end=' ')
            if num %2 == 0:
                num //= 2
            else:
                num = num * 3 + 1
        else:
            print(1)
    else:
        print('Debe ser mayor que 0')