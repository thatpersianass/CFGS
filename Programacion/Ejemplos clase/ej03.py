# Dada una lista generar otra lista eliminando los elementos duplicados consecutivos.

lista = [0,0,1,2,3,4,4,5,6,6,6,7,8,9,4,4]

# lista = ['a','b','b','b','c','d']

# # lista_limpia = []

# elto = None

# for i in lista:
#     if i != elto:
#         lista_limpia.append(i)
#         elto = i
        
# print(lista_limpia)

lista_limpia = [0]

elto = 0

for i in lista[1:]:
    if i != elto:
        lista_limpia.append(i)
        elto = i
        
print(lista_limpia)