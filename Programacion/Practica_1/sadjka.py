def es_bien_estructurado(numero):
    # Convertir el número a string para poder iterar sobre cada dígito
    numero_str = str(numero)

    # Iterar sobre el número de derecha a izquierda
    for i, digito in enumerate(reversed(numero_str), start=1):
        digito = int(digito)  # Convertir el dígito a un número entero

        # Verificar la posición impar (posiciones 1, 3, 5, ...) debe tener dígito impar
        if i % 2 != 0 and digito % 2 == 0:
            return False  # Si la posición es impar y el dígito es par, no está bien estructurado

        # Verificar la posición par (posiciones 2, 4, 6, ...) debe tener dígito par
        if i % 2 == 0 and digito % 2 != 0:
            return False  # Si la posición es par y el dígito es impar, no está bien estructurado

    return True  # Si pasa todas las verificaciones, el número está bien estructurado

# Solicitar número al usuario
numero = input("Ingrese un número: ")

# Verificar si el número está bien estructurado
if es_bien_estructurado(numero):
    print(f"El número {numero} está posicionalmente bien estructurado.")
else:
    print(f"El número {numero} NO está posicionalmente bien estructurado.")
