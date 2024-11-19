# Escribir un programa en Python que permita encontrar la/las claves que tengan el máximo valor. El resultado se debe mostrar como una tupla, en la que el primer
# elemento es/son las claves en la que se consigue el máximo y el segundo elemento de la tupla es el máximo valor encontrado.

d1 = {
    7: 95,
    2: 85,
    9: 100,
    4: 100,
    3: 70,
    10: 100,
    5: 90,
    1: 40,
    8: 55,
    6: 80
}

clave_max = ()                                                                  # Aquí se van a guardar las claves del valor máximo

clave_encontrada = []                                                           # Donde se agregaran las claves para luego agregarlos a la tupla                       

valor_max = max(d1.values())                                                    # Se encuentra el valor máximo

for i in d1:                                                                    # Se itera el diccionario para encontrar las claves que contengan el valor máximo
    if d1[i] == valor_max:
        clave_encontrada.append(i)

clave_max = clave_max + tuple(clave_encontrada)                                 # Se añade la clave máxima a la tupla

print(f'Las claves {clave_max} tienen el valor más alto ({valor_max})')