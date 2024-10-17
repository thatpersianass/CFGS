# se pide un programa en Python que genere contraseñas seguras de forma aleatoria según las siguientes pautas:
# Tener min. 12 max. 15 caracteres
# Letras minúsculas desde la a hasta la z
# Letras mayúsculas desde la A hasta Z
#  Los dígitos desde el 0 al 9.
#  Los caracteres especiales siguientes: @ # % $ & ? ¿ ¡ ! * 


import random


simbolos = '@#%$&?¿¡!*'                                                                                     # String con los símbolos predefinidos para la contraseña


while True:
    long = random.randint(12, 15)                                                                           # Genera la longitud de la contraseña ( de 12 a 15 )
    password = ''
    digitos_encontrados = []                                                                                # Lista para llevar el control de los dígitos añadidos
    simbolos_usados = set()                                                                                 # Conjunto para evitar repetición de caracteres especiales
    min_count = 0  # Contador de letras minúsculas
    mayus_count = 0  # Contador de letras mayúsculas

    for i in range(long):
        abc_min = 'abcdefghijklmnñopqrstuvwxyz'                                                             # Letras minúsculas
        abc_mayus = abc_min.upper()                                                                         # Genera una letra aleatoria en mayúscula
        eleccion = random.randrange(1,5)                                                                    # Genera un numero aleatorio para determinar si se va a imprimir mayúsculas, minusculas, números o símbolos

        if eleccion == 1:                                                                                   # Si eleccion es 1, añade una letra minuscula a la contraseña (password)
            password += random.choice(abc_min)
            min_count += 1

        elif eleccion == 2:                                                                                 # Si eleccion es 2, añade una letra mayuscula a la contraseña (password)
            password += random.choice(abc_mayus)
            mayus_count += 1

        elif eleccion == 3:                                                                                 # Si eleccion es 3, añade un simbolo a la contraseña (password)
            simbolo = random.choice(simbolos)
            if simbolo not in simbolos_usados:
                password += simbolo
                simbolos_usados.add(simbolo)

        elif eleccion == 4:
            digito = str(random.randint(0, 9))
            password += digito                                                                              # Si eleccion es 4, añade un numero a la contraseña (password)
            digitos_encontrados.append(digito)                                                              # Registrar el dígito añadido

    if password[0].isalpha():
        break

    if min_count >= 2 and mayus_count == 2:
        # Comprobar si al menos 2 dígitos se repiten
        if any(digitos_encontrados.count(d) >= 2 for d in set(digitos_encontrados)):
            break

print(password)