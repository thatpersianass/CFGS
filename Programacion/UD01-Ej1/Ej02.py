# Se desea realizar un programa que permita convertir datos de tiempo expresado
# en días, horas, minutos y segundos a milisegundos y viceversa.

# El programa debe pedir al usuario el tipo de conversión a realizar y debe validar
# todos los datos de entrada. Deben decidir como debe ser la entrada de datos en
# ambos casos y una vez realizados los cálculos correspondientes se debe mostrar
# como respuesta tanto los datos originales y el resultado de la conversión.
bucle = 1 # Se declara el bucle

while bucle == 1:                                                                                   # Mientras $bucle sea 1, el código se ejecuta infinitamente
    try:                                                                                            # Condición por si el usuario introduce una letra en lugar de un número entero
        choose = int(input("¿Qué tipo de conversión desea hacer? D-Ms(1), H-Ms(2), M-Ms(3), S-Ms(4), Más opciones(5):  "))

        if choose == 1:
            i = float(input("Inserte el valor que desea convertir:   "))
            resultado = i * 86400000                                                                # Operación para pasar de Días a Ms
            print(f"{i} Días son {resultado} Ms")
            bucle = 0                                                                               # Se cierra el bucle

        elif choose == 2:
            i = float(input("Inserte el valor que desea convertir:   "))
            resultado = i * 3600000                                                                 # Operación para pasar de Horas a Ms
            print(f"{i} Horas son {resultado} Ms")
            bucle = 0                                                                               # Se cierra el bucle

        elif choose == 3:
            i = float(input("Inserte el valor que desea convertir:   "))
            resultado = i * 60000                                                                   # Operación para pasar de Minutos a Ms
            print(f"{i} Minutos {resultado} Ms")
            bucle = 0                                                                               # Se cierra el bucle

        elif choose == 4:
            i = float(input("Inserte el valor que desea convertir:   "))
            resultado = i * 1000                                                                    # Operación para pasar de Segundos a Ms
            print(f"{i} Segundos son {resultado} Ms")
            bucle = 0                                                                               # Se cierra el bucle

        elif choose == 5:
            choose = int(input("¿Qué tipo de conversión desea hacer? Ms-D(1), Ms-H(2), Ms-M(3), Ms-S(4): "))
            
            if choose == 1:
                i = float(input("Inserte el valor que desea convertir:   "))
                resultado = i / 86400000                                                            # Operación para pasar de Ms a Días
                parte_entera = int(resultado)                                                       # Separa la parte entera de la decimal
                parte_decimal = round(resultado - parte_entera, 2)                                  # Separa la parte decimal de la entera
                resultado2 = parte_decimal * 24                                                     # Operación para pasar de Días a Horas

                parte_entera2 = int(resultado2)                                                     # Separa la parte entera de la decimal
                parte_decimal2 = round(resultado2 - parte_entera2, 2)                               # Separa la parte decimal de la entera
                resultado3 = parte_decimal2 * 60                                                    # Operación para pasar de Horas a Minutos

                parte_entera3 = int(resultado3)                                                     # Separa la parte entera de la decimal
                parte_decimal3 = round(resultado3 - parte_entera3, 2)                               # Separa la parte decimal de la entera
                resultado4 = parte_decimal3 * 60                                                    # Operación para pasar de Minutos a segundos

                parte_entera4 = int(resultado4)                                                     # Separa la parte entera de la decimal

                print(f"{i} milisegundos son {parte_entera} días, {parte_entera2} horas, {parte_entera3} minutos y {parte_entera4} segundos")
                bucle = 0                                                                           # Se cierra el bucle

            elif choose == 2:
                i = float(input("Inserte el valor que desea convertir:   "))
                resultado = i / 3600000                                                             # Operación para pasar de Ms a Horas
                parte_entera = int(resultado)                                                       # Separa la parte entera de la decimal
                parte_decimal = round(resultado - parte_entera, 2)                                  # Separa la parte decimal de la entera 
                resultado2 = parte_decimal * 60                                                     # Operación para pasar de Horas a Minutos

                parte_entera2 = int(resultado2)                                                     # Separa la parte entera de la decimal
                parte_decimal2 = round(resultado2 - parte_entera2, 2)                               # Separa la parte decimal de la entera 
                resultado3 = parte_decimal2 * 60                                                    # Operación para pasar de Minutos a segundos

                parte_entera3 = int(resultado3)                                                     # Separa la parte entera de la decimal

                print(f"{i} milisegundos son {parte_entera} horas, {parte_entera2} minutos y {parte_entera3} segundos")
                bucle = 0

            elif choose == 3:
                i = float(input("Inserte el valor que desea convertir:   "))
                resultado = i / 60000                                                               # Operación para pasar de Ms a Minutos
                parte_entera = int(resultado)                                                       # Separa la parte entera de la decimal
                parte_decimal = round(resultado - parte_entera, 2)                                  # Separa la parte decimal de la entera 
                resultado2 = parte_decimal * 60                                                     # Operación para pasar de Minutos a Segundos

                parte_entera2 = int(resultado2)                                                     # Separa la parte entera de la decimal

                print(f"{i} milisegundos son {parte_entera} minutos y {parte_entera2} segundos")
                bucle = 0                                                                           # Se cierra el bucle

            elif choose == 4:
                i = float(input("Inserte el valor que desea convertir:   "))
                resultado = i / 1000                                                                # Operación para pasar de Ms a Segundos
                parte_entera = int(resultado)                                                       # Separa la parte entera de la decimal

                print(f"{i} milisegundos son {parte_entera} segundos")
                bucle = 0                                                                           # Se cierra el bucle

        else: # Si el usuario no introduce una opción del menú (1-5)
            print("Inserte una opción válida...")

    except:
        print("Inserte una opción válida...")
        bucle = 0                                                                                   # Se cierra el bucle