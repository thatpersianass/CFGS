# Escribe un programa en Python que genere una lista de nombre
# comprado_por_todos en la que aparecen los productos que han sido comprado
# por todo los clientes.

# Escribe un programa en Python que genere un diccionario de nombre
# clientes_exlusivos en la que se guardará los clientes que tienen productos en
# exclusividad. En exclusividad significa que sólo lo vende ese cliente.

# La clave del diccionario es el nombre del cliente
# El valor una lista de productos que vende en exclusividad.

compras = {
    "Juan": ["manzanas", "plátanos", "café"],
    "Ana": ["café", "leche", "pan"],
    "Luis": ["manzanas", "café", "pan"]
}

clientes = []  # Guardar los clientes para luego iterarlos

productos = {} # Guardar los productos y las veces que aparecen en el diccionario

productos_exclusivos = [] # Guarda los productos que aparecen solo una vez

comprado_por_todos = []

clientes_exclusivos = {}

for i in compras: # Guarda los clientes
    clientes.append(i)

for i in range(len(compras)):   # itera por el numero de claves del diccionario
    for k in compras[clientes[i]]:  # itera los clientes para guardar los productos en k
        if k not in productos:  # si el producto no está en productos, entonces se agrega con 1 aparicion
            productos[k] = 1
        else:                   # si está, se le suma 1 a sus apariciones
            productos[k] += 1

for i in productos:
    if productos[i] == len(clientes): # Si el numero de apariciones es igual a los clientes que hay, significa que ha sido comprado por todos
        comprado_por_todos.append(i)
    elif productos[i] == 1: # SI aparecen solo una vez, significa que son exclusivos, y se guardan para buscarlos en el diccionario
        productos_exclusivos.append(i)

for i in range(len(compras)):
    for h in clientes:
        for k in compras[h]:
            for f in productos_exclusivos: # SI se encuentra en el diccionario el producto exclusivo, se guarda quien lo compró, junto a él
                if f == k:
                    clientes_exclusivos[h] = f

if comprado_por_todos:
    print(f'Los productos comprados por todos son:\n{comprado_por_todos}')
else:
    print('No hay productos que hayan sido comprados por todos')
    
if clientes_exclusivos:
    print(f'Los productos exclusivos son:\n{clientes_exclusivos}')
else:
    print('No hay productos exclusivos')