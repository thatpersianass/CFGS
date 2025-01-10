# Se quiere crear una función de nombre numFibonacci que recibe como parámetro un número y retorna el n-esimo número de Fibonacci.

# La función de Fibonacci se define de la siguiente forma:

# Fib(0) = 0
# Fib(1) = 1

# Fib(n) = Fib(n-1) + Fib(n-2) para n >= 2

# Ejemplo

# Fib(3) = 2
# Fib(4) = 3
# Fib(5) = 5

def numFibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            
            a, b = b, a + b
            
        return b

n = int(input("Introduce un Numero\n-->     "))

print(f"Fib({numFibonacci(n)})")
