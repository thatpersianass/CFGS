# explicación teoría de las listas.

# creación de una lista

# crea la lista vacía

# lista01 = list()  
# lista02 = []
# print(lista01, lista02)

# lista01 = list('123')  # crear una lista a partir de un iterable
# lista02 = list([1,2,3])
# lista03 = ['a','b','c']
# lista04 = [1,'a', ['b', 2], (3,4), {1:'a'}, True]
# print(lista01, lista02, lista03, lista04)

# acceder a los elementos de una lista
# de izq a der (0..nro_eltos-1)

# lista = [0,1,2,3,4,5,6,7,8,9]
# print(lista[0], lista[5], lista[8]+lista[9])

# de der a izq (-nro_eltos..-1)

# lista = [0,1,2,3,4,5,6,7,8,9]
# print(lista[-1], lista[-4], lista[-9]+lista[-10])

# error al acceder a una posición que no existe
# a = [3]
# print(a[1])

# tener cuidado con las asignaciones

# a = [1,2]
# b = a
# print(a,b)
# b[0] = 9
# a[1] = 7
# print(a,b)

# a = [1,2]
# b = a
# print(a,b)
# a = ['a']
# print(a,b)

# a = [[1,2],['a','b'], ['c','d']]
# b = a
# print(a,b)
# print(a[0], a[1])
# print(a[0][1])

# b[0] = 9
# a[1] = 7
# print(a,b)

# a = b = [3]
# print(a,b)
# a[0] = 8
# print(a,b)

# recorrer una lista
# con for .. in

# lista = [0,1,2,3,'a',5,6,7,8,9]
# for elto in lista:
#     print(elto, end = ' ')
# print()

# con for .. range()
# lista = [0,1,2,3,4,5,6,7,8,9]
# for pos in range(len(lista)):
#     print(lista[pos], end = ' ')
# print()

# recorrido con while
# lista = [0,1,2,3,4,5,6,7,8,9]
# pos = 0
# while pos < len(lista):
#     print(lista[pos], end = ' ')
#     pos += 1
# print()

# recorrido con enumerate()
# lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# for pos,elto in enumerate(lista):
#     print(pos, elto)

# for tupla in enumerate(lista):
#     print(tupla)

# recorrer listas anidadas
# lista = [[1,2,3],[4,5,6],[7,8,9]]
# for fila in range(len(lista)):
#     for columna in range(len(lista[fila])):
#         print(lista[fila][columna], end = ' ')
#     print()

# También puede utilizar la comprensión de listas para recorrer la lista:
# lista = [0,1,2,3,4,5,6,7,8,9]
# [print(elto, end =' ') for elto in lista]
# print()

# slicing  [valor_inical:valor_final:salto]

# lista = [0,1,2,3,4,5,6,7,8,9]
# lista2 = lista[3:1:-1]
# print(lista2)

# lista = [0,1,2,3,4,5,6,7,8,9]
# lista2 = lista[-7:-3:2]
# print(lista2)

# lista = [0,1,2,3,4,5,6,7,8,9]
# lista2 = lista[::-1]
# print(lista2)

# cambio de valor de un elto

# lista = ['a',1,2,3,4,5,6,7,8,9]
# lista[0] = 100
# print(lista)

# añadir elementos

# lista = list()  # = []
# lista.append(1)
# lista.append(2)
# # 
# lista = [3,4,5] + lista
# print(lista)

# lista = [0,2]
# lista.insert(9,'b')
# print(lista)

# remover elementos

# prevenir error al borrar

# lista = ['a','b','c', 'b']
# if lista.count('b') != 0:
#     lista.remove('b')
# print(lista)

# remover todas las ocurrencias

# lista = ['a','b','c', 'b']
# while lista.count('z') != 0:
#     lista.remove('z')
# print(lista)

# lista = ['b','b']
# for car in lista:
#     print('++++',lista)
#     if car == 'b':
#         lista.remove(car)
#         print(lista)
# print('***',lista)

# lista = ['b','b']
# for car in lista:
#     print('++++',lista)
#     if lista.count('b') > 0:
#         lista.remove(car)
#         print(lista)
# print('***',lista)

# pop()

# lista = ['a','b','c','d']
# caracter_borrado = lista.pop()
# lista[0] = lista.pop()
# print(lista)
# print(caracter_borrado)

lista = ['a','b','c','d']
# caracter_borrado = lista.pop()
lista[0] = lista.pop(0)
# lista[0] = lista.pop(0)
print(lista)
# print(caracter_borrado)

# ejemplo index

# lista = ['a','b','c','d','c']
# print(lista.index('c'))

# lista = ['a','b','c','d','c']
# try:
#     print(lista.index('x'))
# except:
#     print('Error el elto no está en la lista')

# index tiene un segundo parámetro

# lista = ['a','b','c','d','c'] 
# print(lista.index('c', 3)) # el segundo parámetro es la posición de comienzo de la búsqueda

# lista = ['a','b','c','d','3', 'a','c'] 
# print(lista.index('c', 3, 7)) # el tercer parámetro es la posición final de la búsqueda (recordar -1)

# lista = ['a','b','c','d','c']
# lista.extend('123')
# print(lista)

# # lista = ['a','b','c','d','c']
# # lista.extend(range(2))
# # print(lista)

# lista = ['a','b','c','d','c']
# lista.extend({0:'a', 1:'b'})
# print(lista)

# lista = ['a','b','c','d','c']
# lista.insert(3,'x')
# print(lista)

# lista = ['a','b','c','d','c']
# lista.insert(9,'x')
# print(lista)

# lista = ['a','b','c','d','c']
# lista.insert(-9,'x')
# print(lista)

# ordenar

# lista = ['e','b','c','d','f']
# lista.sort()
# print(lista)

# lista = ['e','b','c','d','f']
# lista.sort(reverse = True)
# print(lista)

# lista = ['e','b','c','d',2,'z'] # elementos del mismo tipo
# lista.sort()
# print(lista)

# invertir los elementos de una lista

# lista = ['e','b','c','d',2,'z']
# lista.reverse()
# print(lista)

# eliminar todos los elementos de una lista

# lista = ['e','b','c','d',2,'z']
# lista.clear()
# print(lista)

# copia de una lista

# recordamos
# a = [2,3]
# b = a
# print(a,b)
# a[0] = 9
# print(a,b)

# uso de copy
# a = [2,3]
# b = a.copy()
# print(a,b)
# a[0] = 9
# print(a,b)

# pero en este ejemplo la copia falla

# a = [ [2], [3] ]
# b = a.copy()
# print(a,b)
# a[0][0] = 9
# print(a,b)

# para solucionar este problema se usa deepcopy()
# deepcopy() pertenece a la librería copy

# from copy import deepcopy
# a = [ [2], [3] ]
# b = deepcopy(a)
# print(a,b)
# a[0][0] = 9
# print(a,b)

# lista = [1,2,3,4,5]
# print(f'el menor valor en la lista {min(lista)}')
# print(f'el menor valor en la lista {max(lista)}')
# print(f'el menor valor en la lista {sum(lista)}')

# lista = [10,2,30,4,25]
# lista2 = sorted(lista)
# print(lista2)
# lista3 = list(reversed(lista))
# print(lista3)

# lista1 = [1,2,3,4,5]
# lista2 = ['a','b','c','d','e']
# lista3 = ['+', '*', '@', '%', '#']
# lista_tuplas = zip(lista1, lista2, lista3)
# for tupla in lista_tuplas:    
#     print(tupla)

# se generan tantas tuplas como el tamaño de la menor lista
# lista1 = [1,2,3,4]
# lista2 = ['a','b','c','d','e']
# lista3 = ['+', '*', '@', '%', '#']
# lista_tuplas = zip(lista1, lista2, lista3)
# for tupla in lista_tuplas:    
#     print(tupla)

# las funciones filter y map cuando veamos las funciones