# Lectura de números positivos

bucle = 0

while bucle == 0:
    valor = input("Escriba un número positivo:")

    try:
        numero = float(valor)

    except:
        print("Tu la comprensión lectora como que no... ¿Verdad? N U M E R O")

    else:
        if numero >= 0:
            print(f"Número leido: {numero}")

        # elif valor == "un número positivo" or "número positivo" or "numero positivo" or "un numero positivo":
        #     print("¿Chistochito tú, no?")

        else:
            print("Pa' casita por tonto")
            bucle = 1