# Escriba un programa en Python que mediante un diccionario cuente el número de
# veces que aparece una letra en una frase leída.

# Una vez creado el diccionario se debe recorrer para mostrar por línea el número de
# ocurrencia de cada letra. 

# alphabet = {}

# word = input('Inserte una palabra -->     ').lower()

# for letra in word:
#     if letra not in alphabet and letra != ' ':
#         alphabet[letra] = 1
        
#     else:
#         alphabet[letra] += 1

# print(alphabet)

# alphabet = {}

# word = input('Inserte una palabra -->     ').lower()

# for letra in word:
#     alphabet.setdefault(letra, 0)
#     alphabet[letra] += 1

# print('Se han encontrado las siguientes letras:')

# for find in alphabet:
#     if find != ' ':
#         print(f'{find} = {alphabet[find]} veces')

diccionario = {
    'a':1,
    'b':1,
    'c':1,
    'd':1,
}

# for k in diccionario:
#     comp = diccionario[k]
#     break

comp = diccionario['a']

find = True

for i in diccionario:
    if diccionario[i] != comp:
        find = False
        break

if find:
    print('Todos sus valores son iguales')

else:
    print('Todos sus valores NO son iguales')