# Programa que escriba los 20 primeros números de Fibonasiu

bucle = 2
fib = 0
fibn_1 = 0
fibn_2 = 1

print(0)
while bucle <= 20:
    fib = fibn_1 + fibn_2
    print(f"{fib}")
    fibn_2 = fibn_1
    fibn_1 = fib
    bucle += 1