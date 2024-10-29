# Se quiere escribir un programa en Python que pida una frase al usuario y que
# compruebe si esta contiene todas las letras del alfabeto español.
# Las letras del alfabeto español son las siguientes:

# a b c d e f g h i j k l m n ñ o p q r s t u v w x y z

# Se debe tener en cuenta que además de las letras minúsculas están las
# correspondientes mayúsculas.

# En relación a las vocales recordar que estás pueden estar acentuadas, por tanto á,
# é, í, ó, ú se deben reconocer como si fueran vocales sin acentos, al igual que las
# vocales mayúsculas acentuadas.

alfabeto = 'abcdefghijklmnñopqrstuvwxyz'

opt = input('Introduce una frase -->  ').lower()

caracteres_encontrados = ('')

for i in opt:
    if i != (' '):                                                                      # Verifica si no es un espacio
        for k in alfabeto:
            if i == k:                                                                  # Verifica si la letra actual coincide con el alfabeto
                caracteres_encontrados += i
                break

if len(set(caracteres_encontrados)) == len(alfabeto):                                   # Se utiliza el 'SET' para retirar los caracteres duplicados
    print('La palabra contiene todos los caracteres del alfabeto')

else:
    print('La palabra NO contiene todos los caracteres del alfabeto')