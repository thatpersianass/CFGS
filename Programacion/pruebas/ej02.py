# Escribe una función recursiva en Python llamada sumar_lista(lst) que reciba una lista de números enteros y devuelva la suma de todos sus elementos. 
# No puedes usar bucles (como for o while), solo recursividad.

def sumar_lista(lst) -> int:
    if lst:
        return lst[0] + sumar_lista(lst [1:])   
    
    else:
        return 0

lista = []

while True:
    i = input('Ingrese un numero para agregar a la lista, ponga @ para salir del bucle \n  ->    ')
    
    if i == "@":
        break
    
    try:
        i = int(i)
    
    except:
        print('Dato no valido...')
    
    else:
        lista.append(i)

print(f'La suma de todos los digitos de la lista es {sumar_lista(lista)}')