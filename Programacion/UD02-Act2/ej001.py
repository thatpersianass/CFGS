# Escribir un programa en Python para eliminar claves con los mismos valores en un diccionario.

# Ejemplo:

# d1 = {"one":"eleven", "2":2, "three":3, "11":"eleven", "four":44, "two":2}

# La solución es {'three': 3, 'four': 44}

d1 = {"one":"eleven", "2":2, "three":3, "11":"eleven", "four":44, "two":2}

l1 = list(d1.keys())                                                                            # Se guardan en una lista SOLO las claves de el diccionario
l2 = list(d1.values())                                                                          # Se guardan en una lista SOLO los valores de el diccionario

elim = []                                                                                       # Lista de claves a eliminar

for i in l1:
    if l2.count(d1[i]) > 1:                                                                     # Si el valor aparece más de una vez se añade a la lista elim
        elim.append(i)

for clave in elim:                                                                              # Se iteran las claves de eliminación del diccionario
    del d1[clave]

print(d1)