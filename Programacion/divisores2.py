valor = int(input('Escribe un numero:  '))
auxiliar = valor
suma = 0

while auxiliar != 0:
    auxiliar,resto = divmod(auxiliar, 10) #divmod retorna una tupla de dos elementos
    suma += resto
print(f"La suma de los digitos de {valor} es {suma}")