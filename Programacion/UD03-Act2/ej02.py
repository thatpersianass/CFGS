# Se quiere crear una función recursiva de nombre cuentaParImpar que recibe como
# parámetro un número entero y retorna una tupla en la que el primer elemento es la
# cantidad de dígitos pares que tiene el número y el segundo la cantidad de dígitos
# impares.

def cuentaParImpar(numero):
    if numero < 10:
        if numero % 2 == 0:
            return (1, 0)
        else:
            return (0, 1)
    else:
        ultimo_digito = numero % 10
        pares, impares = cuentaParImpar(numero // 10)
        if ultimo_digito % 2 == 0:
            return (pares + 1, impares)
        else:
            return (pares, impares + 1)
