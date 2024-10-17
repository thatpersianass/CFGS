# # Se lee un número por teclado y se imprime por pantalla todos los divisores que tiene
# opt = int(input('Inserte un número -->   '))

# for i in range(1, opt + 1):
#     if opt % i == 0:
#         print(i, end = ' ')

            # opt = int(input('Inserta un numeroso -->   '))
            # # Inicializamos la variable 'suma' en 0, que almacenará la suma de los dígitos
            # suma = 0

            # # Mientras el valor de 'opt' sea mayor que 0, el ciclo continuará
            # while opt > 0:
            #     # Extraemos el último dígito de 'opt' usando el operador módulo (%)
            #     # El valor de 'digit' será el último dígito de 'opt'
            #     digit = opt % 10
                
            #     # Sumamos el valor de 'digit' a la variable 'suma'
            #     suma += digit
                
            #     # Eliminamos el último dígito de 'opt' dividiendo entre 10 y descartando el decimal
            #     # Esta operación acorta el número para la siguiente iteración
            #     opt //= 10

            # # Una vez que el ciclo termina (cuando 'opt' llega a 0), mostramos la suma total de los dígitos
            # print(f"La suma de los digitos es {suma}")

# opt = input('Inserta un numeroso -->   ')
# suma = 0

# for digito in opt:
#     suma += int(digito)
# print(f"La suma de los digitos es {suma}")
opt = int(input('Inserte un número -->   '))

for i in range(1, opt//2):
    if opt % i == 0:
        print(i, end = ' , ')
else:
    print(opt)