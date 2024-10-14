# Escriba un programa en Python, que pida al usuario un número entero. El número
# será valido si es mayor o igual a 2 y menor o igual a 10 o menor o igual a -2 y
# mayor o igual que -10. El programa deberá imprimir según el número leído el
# patrón de figura que se muestra en el cuadro de abajo


                                                                                                    # Solicitar un número entero al usuario
choose = int(input("Introduzca un número entero entre 2 y 10 o entre -20 y -10: "))

                                                                                                    # Verificar si el número es válido
if (2 <= choose <= 10) or (-10 <= choose <= -2):
                                                                                                    # Trabajamos con el valor absoluto para construir el patrón
    num_abs = abs(choose)
    
                                                                                                    # Si el número es positivo
    if choose > 0:
                                                                                                    # Generamos el patrón normal, donde el número de asteriscos disminuye con cada línea
        for i in range(num_abs, 0, -1):
                                                                                                    # Imprimir i asteriscos, seguido de espacios y luego i asteriscos nuevamente
            print("*" * i + " " * (2 * (num_abs - i)) + "*" * i)
    
                                                                                                    # Si el número es negativo
    elif choose < 0:
                                                                                                    # Generamos el patrón invertido, donde el número de asteriscos aumenta con cada línea
        for i in range(1, num_abs + 1):
                                                                                                    # Imprimir i asteriscos, seguido de espacios y luego i asteriscos nuevamente
            print("*" * i + " " * (2 * (num_abs - i)) + "*" * i)
else:
                                                                                                    # Si el número no es válido, se muestra un mensaje de error
    print("Número inválido. Debe ser entre 2 y 10, o entre -2 y -10.")