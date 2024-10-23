# Escriba un programa en Python que pida al usuario una frase y muestre los números y la cantidad total de números que aparecen en la cadena leída desde el
# teclado.

# Con número no queremos decir dígito entre letras , sino número propiamente dicho, es decir, secuencia de dígitos separados del resto de caracteres por medio
# del espacio en blanco


opt = input('Introduce una frase ---->  ')
num = []                                                                                    # Crea una lista vacía para almacenar los números encontrados

palabras = opt.split()                                                                      # Divide la frase por los espacios, ya que los números tienen que estar separados de los caracteres para contar como un digito

for palabra in palabras:                                                                    # Concatena por los elementos de la lista $palabras para ir recorriendola, verificando que el campo es un dígito y añadiendolo a la lista de numeros
    if palabra.isdigit():
        num.append(palabra)

if num:
    print("Números encontrados en la cadena:")
    print(" ".join(num))                                                                    # Se usa un espacio mas el join para imprimir los numeros encontrados, quitando el formato de lista
    print(f"En total se han encontrado {len(num)} números en la cadena")
else:
    print("Números encontrados en la cadena:")
    print("Ninguno")
    print("En total se han encontrado 0 números en la cadena")