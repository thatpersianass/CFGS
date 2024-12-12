# Supongamos que se quiere multiplicar x * y ( x es el multiplicador e y es el multiplicando). El método ruso de
# multiplicar consiste en multiplicar sucesivamente por 2 el multiplicando y dividir por 2 el multiplicador hasta que
# el multiplicador tome el valor 1. Luego, se suman todos los multiplicandos correspondientes a los multiplicadores
# impares.

# Dicha suma es el producto de los dos números. La siguiente tabla muestra el cálculo realizado para multiplicar 37 por 12,
# cuyo resultado final es 12 + 48 + 384 = 444.

# Diseñe un programa que implemente mediante una función de nombre
# multiplicación_rusa(multiplicando, multiplicador) y retorne el resultado de la multiplicación.
# El programa principal debe leer los números a multiplicar.


# Programa
def multiplicacion_rusa(x:int, y:int) -> int:
    
    signo = 1
    if (x<0):
        signo = -1
        x = -x
        
    if (y<0):
        signo = -1
        y = -y
    
    producto = 0
    while abs(x) != 1:
        if x % 2:
            producto += y
        y *= 2
        x //= 2
    return producto * signo


if __name__ == '__main__':
    print(multiplicacion_rusa(37,12))