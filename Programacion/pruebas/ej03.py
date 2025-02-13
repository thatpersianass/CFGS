# Escribe una función recursiva en Python llamada invertir_lista(lst) que reciba una lista y devuelva una nueva lista con los elementos en orden inverso.

def invertir_lista(lst) -> int:
    if not lst or len(lst) == 1:
        return lst
    
    else:
        return invertir_lista(lst[1:]) + [lst[0]]

lista = [1,2,3]

print(f'La lista {lista} invertida es {invertir_lista(lista)}')