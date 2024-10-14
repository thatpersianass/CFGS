# for num in range(10):
#     if num == 5:
#         continue
#     print(num)

# for var in range ( valor_inicial , último_valor , incremento/decremento)         ----        de valor_inicial a último_valor se ejecuta el bucle. El incremento/decremento es si decrece o crece

for i in 'abc':
    if '*' == i:
        print('hay *')
        break
else:
    #solo se ejecuta si no se hace el break
    print('no hay *')