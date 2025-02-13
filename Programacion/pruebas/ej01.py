# Escribe una función recursiva en Python llamada contar_digitos(n) que reciba un número entero positivo n y devuelva la cantidad de dígitos que tiene.
def contar_digitos(n):
    if n < 10:
        return 1
    else:
        return 1 + contar_digitos(n // 10)

n = input('Mete tu pene: ')

print(f'El número {n} tiene {contar_digitos(int(n))} dígitos.')