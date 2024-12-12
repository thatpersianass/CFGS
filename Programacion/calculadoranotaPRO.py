# Hacer un programa que calcule la media.

def calcular_nota_final():
    print("Ingresa las notas que cuentan el 10% de la nota final (presiona Enter sin escribir nada para finalizar):")
    notas_10 = []
    
    while True:
        entrada = input("Nota (0-10): ")
        if entrada == "":
            break
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas_10.append(nota)
            else:
                print("Por favor, ingresa una nota válida entre 0 y 10.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    if notas_10:
        promedio_10 = sum(notas_10) / len(notas_10)
    else:
        promedio_10 = 0
        print("No se ingresaron notas para el 10%. Se asumirá un promedio de 0.")

    while True:
        try:
            nota_25 = float(input("Ingresa la nota que cuenta el 25% de la nota final (0-10): "))
            if 0 <= nota_25 <= 10:
                break
            else:
                print("Por favor, ingresa una nota válida entre 0 y 10.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    while True:
        try:
            nota_65 = float(input("Ingresa la nota que cuenta el 65% de la nota final (0-10): "))
            if 0 <= nota_65 <= 10:
                break
            else:
                print("Por favor, ingresa una nota válida entre 0 y 10.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

    nota_final = promedio_10 * 0.10 + nota_25 * 0.25 + nota_65 * 0.65
    print(f"\nLa nota final es: {nota_final:.2f}")

# Ejecutar el programa
calcular_nota_final()
