#       Escriba un programa en Python, que pida al usuario un número entero. El número
#       será valido si es mayor o igual a 2 y menor o igual a 10 o menor o igual a -2 y
#       mayor o igual que -10. El programa deberá imprimir según el número leído el
#       patrón de triangulo.

choose = int(input("Introduce un número entre 2 y 10 o entre -2 y -10: "))

if (2 <= choose <= 10) or (-10 <= choose <= -2):                            # Se chequea si el número está entre el rango especificado
    num = abs(choose)                                                       # La selección se convierte en un número absoluto, esto para eliminar el punto decimal y hacer más sencillo el calculo
    
    if choose > 0:                                                          # Verifica si el número es positivo

        for steps in range(num, 0, -1):                                     # Bucle for que itera de num. Va de mayor a menor porque estamos generando el patrón desde la fila más grande
            print("*" * steps + " " * (2 * (num - steps)) + "*" * steps)    # Imprime $steps como asteriscos a la izquierda, los espacios dependen de la diferencia entre $steps y $num       

    elif choose < 0:                                                        # Verifica si el número es negativo

        for steps in range(1, num + 1):                                     # Bucle for que itera desde 1 hasta num, es decir, desde la fila más pequeña
            print("*" * steps + " " * (2 * (num - steps)) + "*" * steps)
else:
    print("Número inválido. Debe ser entre 2 y 10, o entre -2 y -10.")
