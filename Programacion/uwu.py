def imprimir_flecha(n):
    if n < 3 or n % 2 == 0:
        print("El número debe ser impar y mayor o igual a 3.")
        return
    
    for i in range(n):
        for j in range(n):
            if j == i or j == n - 1 or i == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

n = int(input("Ingrese un número impar mayor o igual a 3: "))
imprimir_flecha(n)
