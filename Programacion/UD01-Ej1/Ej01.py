# Escriba un programa en Python, que pida al usuario un número entero. El número
# será valido si es mayor o igual a 2 y menor o igual a 10 o menor o igual a -2 y
# mayor o igual que -10. El programa deberá imprimir según el número leído el
# patrón de figura que se muestra en el cuadro de abajo


# Solicitar un número entero al usuario
numero = int(input("Introduce un número entero: "))

# Verificar si el número es válido
if (2 <= numero <= 10) or (-10 <= numero <= -2):
    # Trabajamos con el valor absoluto para construir el patrón
    num = abs(numero)
    
    # Si el número es positivo
    if numero > 0:
        # Generamos el patrón normal
        for i in range(num, 0, -1):
            print("*" * i + " " * (2 * (num - i)) + "*" * i)
    
    # Si el número es negativo
    elif numero < 0:
        # Generamos el patrón invertido
        for i in range(1, num + 1):
            print("*" * i + " " * (2 * (num - i)) + "*" * i)
else:
    # Si el número no es válido, se muestra un mensaje de error
    print("Número inválido. Debe ser entre 2 y 10, o entre -2 y -10.")
