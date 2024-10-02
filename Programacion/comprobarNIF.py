# se pide el NIF o NIE y se comprueba su válidez
# ej NIF(12345678X); ej NIE(X0123456A) @ = "X", "Y", "Z"

lista = "TRWAGMYFPDXBNJZSQVHLCKE"

numeros = input("Introduce tu NIF/NIE:  ")

if numeros[0].isnumeric(): # verificación de que es un NIF
    calc = int(numeros[0:8])
    letranif = str(numeros[8])
    i = calc % 23
    letra = lista[i]
    if letra == letranif:
        print(f"El NIF {numeros} es válido")

    else:
        print(f"El NIF {numeros} NO es válido")


elif numeros[0] == "X":    # verificación de que es un NIE que empieza con X
    calc = int(numeros[1:8])
    letranif = str(numeros[8])
    i = calc % 23
    letra = lista[i]
    if letra == letranif:
        print(f"El NIE {numeros} es válido")

    else:
        print(f"El NIE {numeros} NO es válido")

elif numeros[0] == "Y":     # verificación de que es un NIE que empieza con Y
    calc = int("1" + numeros[1:8])
    letranif = str(numeros[8])
    i = calc % 23
    letra = lista[i]
    if letra == letranif:
        print(f"El NIE {numeros} es válido")

    else:
        print(f"El NIE {numeros} NO es válido")

elif numeros[0] == "Z":     # verificación de que es un NIE que empieza con Z
    calc = int("2" + numeros[1:8])
    letranif = str(numeros[8])
    i = calc % 23
    letra = lista[i]
    if letra == letranif:
        print(f"El NIE {numeros} es válido")
        
    else:
        print(f"El NIE {numeros} NO es válido")

else:
    print("Inválido...")