# Esriba un programa en python que defina una función recursiva, que recibe una lista
# cuyos elementos pueden ser numeros o letras y retorne dos listas, una de las cuales tiene
# que dar todos los numeros de la lista original, y la otra tendrá todas las letras
# Ambas listas deberán estar ordenadas de forma creciente y NO DEBEN CONTENER VALORES DUPLICADOS

# EJEMPLO

#  lista = ['a', 1, 'z', 9, 'c', 3, 'b', 2, 'a', 3, 7, 'c', 9, 'a']

#  lista_numeros = [1,2,7,9] lista_letras = ['a', 'b', 'c', 'z']
lista_numeros = []
lista_letras = []
def separar_numeros_letras(lst:list):    

    if lst: # Si la lista no está vacia se filtran los datos
        if isinstance(lst[0], int):
            if lst[0] not in lista_numeros:
                lista_numeros.append(lst[0])

                return separar_numeros_letras(lst[1:])
            
        else:
            if lst[0] not in lista_letras:
                lista_letras.append(lst[0])
                return separar_numeros_letras(lst[1:])

lista = ['a', 1, 'z', 9, 'c', 3, 'b', 2, 'a', 3, 7, 'c', 9, 'a']

separar_numeros_letras(lista)
print(f"Numeros: {sorted(lista_numeros)}\nLetras: {sorted(lista_letras)}")