# El programa debe contener un menú que permita dar respuesta a todas las
# preguntas que se plantean a continuación:
# 1. Películas vistas por todos los usuarios (1,00 punto)
# Se trata de encontrar las películas que se han sido vistas por todos los usuarios

# 2. Películas vista en exclusivas por un usuario (1,00 punto)
# Se trata de encontrar las películas que ha visto en exclusiva un usuario. En este caso se pide y valida el nombre del usuario.

# 3. Conteo del número de visionado (1,00 punto)
# En este caso se intenta contar el número de veces que se ha visto cada película. La información se debe almacenar en un lista de nombre visionado en la que cada
# elemento es una tupla con los siguientes valores (película, nro_veces_vista). Esta lista debe tener ordenada sus tuplas por el número de visionado de cada película.

# 4. Encontrar las películas más populares (1,00 punto)
# En este caso se pide que encuentre la/las películas que más se han visto (por número de visionado)

# 5. Recomendar películas a un usuario (1,00 punto)
# Dado el nombre de un usuario que se pide por pantalla y se valida, se debe crear una lista con las películas que se le recomiendan ver.

peliculas_vistas = {
    "Ana": ["Inception", "Avatar", "Titanic", "Matrix"],
        "Luis": ["Matrix", "Inception", "El Señor de los Anillos"],
            "Sofía": ["Titanic", "Avatar", "Matrix", "El Rey León"],
                "Carlos": ["Matrix", "Avatar", "El Señor de los Anillos"],
}

clientes = []

peliculas_todos = []

peliculas_exclusivas = []

peliculas_exclusivas_def = {}

visionado = {}

vistas = {}

peliculas_populares = [] # Se hace en un top 3

for i in peliculas_vistas:
    clientes.append(i)

for i in range(len(peliculas_vistas)):   # itera por el numero de claves del diccionario
    for k in peliculas_vistas[clientes[i]]:  # itera los clientes para guardar las peliculas en k
        if k not in vistas:  # si la pelicula no está en vistas, entonces se agrega con 1 aparicion
            vistas[k] = 1
        else:                   # si está, se le suma 1 a sus apariciones   
            vistas[k] += 1

for i in vistas:
    if vistas[i] == len(clientes): # Si el numero de apariciones es igual a los clientes que hay, significa que ha sido vista por todos
        peliculas_todos.append(i)
    elif vistas[i] == 1: # SI aparecen solo una vez, significa que son exclusivos, y se guardan para buscarlos en el diccionario
        peliculas_exclusivas.append(i)


for i in range(len(peliculas_vistas)):
    for h in clientes:
        for k in peliculas_vistas[h]:
            for f in peliculas_exclusivas: # SI se encuentra en el diccionario la película exclusivo, se guarda quien la vió, junto a él
                if f == k:
                    peliculas_exclusivas_def[h] = f

visionado = (sorted(vistas.items(), key=lambda item: item[1], reverse=True)) # Se guarda en visionado las películas en tuplas junto sus vistas, este se guarda en formato de lista, que dentro tiene las películas en tuplas en formato ((película, nro_veces_vista)

iter = 1
for i in visionado: # Se guardan las 3 películas más populares
    if iter <= 3:
        peliculas_populares.append(i)
        iter += 1


if peliculas_todos: # Si peliculas_todos no está vacío, se imprime las películas que han visto todos
    iter = 1
    for i in peliculas_todos:
        print(f'las película/s vista/s por todos son: \n   {iter}. {i}\n')
        iter += 1
else:
    print('No hay películas vistas por todos...')

if peliculas_exclusivas_def:
    iter = 1
    for i,k in peliculas_exclusivas_def.items():
        print(f'La/s película/s exclusiva/s son: \n   {iter}. {k}, vista por {i}\n')
        iter += 1
else:
    print('No hay películas exclusivas...')

print(f'Visitas en cada pelíicula:\n{visionado}\n')

iter = 1
print('Las películas más populares son:')
for i in peliculas_populares:
    if iter <= iter:
        for k in vistas:
            if k in i:
                print(f'   {iter}. {k} : {vistas[k]} Vistas')
                iter += 1

while True:
    nombre = input('\nIntroduce tu nombre para poder recomendarte películas que ver\n-->     ')
    iter = 1
    if nombre:
        if nombre in clientes:
            print('Te recomendamos:')
            for i in peliculas_vistas[nombre]:
                print(f'   {iter}. {i}')
                iter += 1
                
            
        else: # Si no existe el nombre en el diccionario, le recomienda las 3 más populares
            print('Te recomendamos:')
            for i in peliculas_populares:
                for k in vistas:
                    if k in i:
                        print(f'   {iter}. {k}')
                        iter += 1
        break

    else:
        print('Introduce tu nombre....')