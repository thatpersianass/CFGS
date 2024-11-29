# Estructura de datos

# productos = {tipo_producto1 : { código : [desc, ctdad, precio]},
#              tipo_producto2 : { código : [desc, ctdad, precio]} ... }

# descripción_del_producto, cantidad_exist_producto y el precio_venta_producto.

# Los tipos de productos permitidos son los siguientes: frío, verduras, carnes, panadería, bazar, despensa, vinos y lácteos.

# El código del producto es un string de 5 caracteres donde el primero de ellos indica el tipo de producto al que pertenece. Este primer caracter del código se
# obtiene del primer caracter del tipo de producto al que pertenece.

# desc es un string que representa la descripción del producto, ctdad es número flotante o entero que representa la existencia actual del producto,
# precio es un número float que representa el precio de venta del producto

# Fusión de datos de empresa01
productos = {
    'frio': {
        'f0001': ['muslos pollo', 20, 8.5],
        'f0002': ['carne cerdo', 20, 5.6]
    },
    'verduras': {
        'v0001': ['tomates', 30, 2.5],
        'v0002': ['cebollas', 20, 2.2]
    },
    'bazar': {
        'b0001': ['pala basura', 10, 3.75],
        'b0002': ['lejia', 10, 1.85]
    },
    'lacteos': {
        'l0001': ['leche entera', 50, 1.15],
        'l0002': ['leche sin lactosa', 20, 1.5]
    }
}

empresa01 = [
    ('verduras', 'tomates', 20, 2.15),
    ('frío', 'muslos pollo', 30, 8.65),
    ('lacteos', 'leche semidesnatada', 20, 1.4),
    ('wino', 'vino tinto monje', 10, 13.75),
    ('wino', 'vino dulce', 5, 12.15)
]

empresa02 = [
    ('pepinos', 20, 1.95),
    ('pala', 5, 3.80),
    ('leche entera', 10, 1.90),
    ('pan mediano', 20, 0.5),
    ('vino blanco', 5, 14.25)
]

productos_validos = ['frio', 'verduras', 'carnes', 'panadería', 'bazar', 'despensa', 'wines', 'lacteos']

# Fusión de datos de empresa01
for tipo_producto, descripcion, cantidad, precio in empresa01:
    tipo_producto = tipo_producto.lower()
    precio = round(precio, 2)

    if tipo_producto not in productos_validos:
        print(f"Tipo de producto '{tipo_producto}' no es válido. Producto ignorado.")
        continue

    if tipo_producto not in productos:
        productos[tipo_producto] = {}

    codigo_existente = None
    for codigo, (desc, ctdad, prc) in productos[tipo_producto].items():
        if desc == descripcion:
            codigo_existente = codigo
            break

    if codigo_existente:
        productos[tipo_producto][codigo_existente][1] += cantidad
        productos[tipo_producto][codigo_existente][2] = max(precio, productos[tipo_producto][codigo_existente][2])
        print(f"Producto '{descripcion}' actualizado: {productos[tipo_producto][codigo_existente]}")
    else:
        while True:
            num_codigo = input(f"Nuevo producto '{descripcion}' en categoría '{tipo_producto}'. Ingresa un número de código (4 dígitos): ")
            if len(num_codigo) == 4 and num_codigo.isdigit():
                nuevo_codigo = f"{tipo_producto[0]}{num_codigo}"
                if nuevo_codigo not in productos[tipo_producto]:
                    productos[tipo_producto][nuevo_codigo] = [descripcion, cantidad, precio]
                    print(f"Producto '{descripcion}' añadido con el código '{nuevo_codigo}'.")
                    break
                else:
                    print("El código ya existe. Intenta con otro.")
            else:
                print("El código debe ser de 4 dígitos.")

# Fusión de datos de empresa02
for descripcion, cantidad, precio in empresa02:
    precio = round(precio, 2)

    descripcion_encontrada = False
    for tipo_producto, productos_tipo in productos.items():
        for codigo, (desc, ctdad, prc) in productos_tipo.items():
            if desc == descripcion:
                productos[tipo_producto][codigo][1] += cantidad
                productos[tipo_producto][codigo][2] = max(precio, productos[tipo_producto][codigo][2])
                print(f"Producto '{descripcion}' actualizado: {productos[tipo_producto][codigo]}")
                descripcion_encontrada = True
                break
        if descripcion_encontrada:
            break

    if not descripcion_encontrada:
        while True:
            tipo_producto = input(f"Nuevo producto '{descripcion}'. Ingresa el tipo de producto: ").lower()
            if tipo_producto in productos_validos:
                if tipo_producto not in productos:
                    productos[tipo_producto] = {}

                while True:
                    num_codigo = input(f"Ingresa un número de código para '{descripcion}' (4 dígitos): ")
                    if len(num_codigo) == 4 and num_codigo.isdigit():
                        nuevo_codigo = f"{tipo_producto[0]}{num_codigo}"
                        if nuevo_codigo not in productos[tipo_producto]:
                            productos[tipo_producto][nuevo_codigo] = [descripcion, cantidad, precio]
                            print(f"Producto '{descripcion}' añadido con el código '{nuevo_codigo}'.")
                            break
                        else:
                            print("El código ya existe. Intenta con otro.")
                    else:
                        print("El código debe ser de 4 dígitos.")
                break
            else:
                print(f"Tipo de producto inválido. Tipos válidos: {', '.join(productos_validos)}")

# Mostrar productos actualizados
print("\nProductos después de la fusión con empresa01 y empresa02:")
for tipo, productos_tipo in productos.items():
    print(f"\n{tipo.capitalize()}:")
    for codigo, (descripcion, cantidad, precio) in productos_tipo.items():
        print(f"  {codigo}: {descripcion} - {cantidad} unidades - {precio:.2f}€")
