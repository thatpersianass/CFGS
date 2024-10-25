#  Generar una lista aplanada desde una lista con anidamientos

# lista = ['a',1,2,'b',['c',3],4]

# lista_plana = []

# #  lista = ['a',1,2,'b','c',3,4]

# for i in lista:
#     if type(i) != list:
#         lista_plana.append(i)
#     else:
#         for k in range(len(i)):
#             lista_plana.append(i[k])

# print(lista_plana)

# lista = ['a',1,2,'b',['c',3],4]

# lista_plana = []

# for i in lista:
#     if type(i) != list:
#         lista_plana.append(i)
#     else:
#         for k in i:
#             lista_plana.append(k)

# print(lista_plana)


lista = ['a',1,2,'b',['c',3],4]

lista_plana = []

for i in lista:
    if type(i) != list:
        lista_plana.append(i)
    else:
        lista_plana.extend(i)

print(lista_plana)