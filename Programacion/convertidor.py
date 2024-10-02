# Programa que pase de Cº a Farenheit (Y viceversa)...

bucle = 1

while bucle == 1: # Realizar el bucle
    print("Inserte su elección:")
    print(" (1) Grados Celcius > Farenheit")
    print(" (2) Farenheit > Grados Celcius")
    print(" (0) Salir")
    choose = input("Inserte su elección:")

    if choose == "1": # Grados Celcius > Farenheit
        try:
            temp = float(input("¿Qué número quieres pasar a Farenheit?:"))
            temp_gf = temp * 1.8 + 32.0
            print(f"{temp}ºC son {temp_gf} F")
            print()

        except:
            print("Eeeeh... No")

    elif choose == "2": # Farenheit > Grados Celcius
        try:
            temp = float(input("¿Qué número quieres pasar a Grados Celcius?:"))
            temp_gc = (temp - 32.0) * 5/9
            print(f"{temp}F son {temp_gc} ºC")
            print()
        except:
            print("Eeeeh... No")

    elif choose == "0": # Salir
        print("Saliendo...")
        print()
        bucle = 0
    
    else: # Elección no válida
        print("Inserte una opción válida...")
        print()
        print()

# Fin del bucle