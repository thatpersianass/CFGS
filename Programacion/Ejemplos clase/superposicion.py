# Definir una función superposicion(lista1, lista2) que tome dos listas y devuelva True si tienen al menos 1 miembro
# en común o devuelva False en caso contrario. Escribir la función usando un bucle for anidado.

# Deberá definir también una función leer_datos() que permita leer los datos y guardarlos en una lista. La función
# debe retornar la lista creada.

# El programa principal debe realizar la lectura de los datos y ejecutar la función superposición. 
lista01 = None

def leer_datos() -> list:
    '''funcion que crea una lista de numeros enteros leidos por teclado.
    Se para la lectura con @.
    Retorna la lista de elementos'''
    lista = []
    if lista01 == None:
        print('Empieza la lectura de la lista01')
    else:
        print('Empieza la lectura de la lista02')
    while True:
        opt = input('\nIntroduce numeros enteros pisha\n->    ')
        
        if opt != '@':
            try:
                lista.append(int(opt))
            except:
                print('Tu suspendiste lengua no?...')
        else:
            break
    
    return lista

def superposicion(lista01: list, lista02:list) -> bool:
    '''Busca un elemento común entre las dos lista
    Retorna True si lo hay, False en caso contrario'''
    set01 = set(lista01)
    set02 = set(lista02)
    comunes = set01.intersection(set02)
    
    return list(comunes)

if __name__ == '__main__':
    lista01 = leer_datos()
    lista02 = leer_datos()
    comunes = superposicion(lista01,lista02)
#     print(f'Están las listas superpuestas: \
# {'SI' if superposicion(lista01,lista02) else 'NO'}')
    print(f'Los elementos comunes son: \
{comunes if comunes else "No hay elementos compuestos"}')