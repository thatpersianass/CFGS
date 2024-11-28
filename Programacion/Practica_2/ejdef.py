# Diccionario inicial que almacena los productos organizados por tipo
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

# Datos de la empresa 01: lista de tuplas que incluyen tipo de producto, descripción, cantidad y precio
empresa01 = [
    ('verduras', 'tomates', 20, 2.15),
    ('frio', 'muslos pollo', 30, 8.65),
    ('lacteos', 'leche semidesnatada', 20, 1.4),
    ('wines', 'vino tinto monje', 10, 13.75),
    ('wines', 'vino dulce', 5, 12.15)
]

# Datos de la empresa 02: lista de tuplas que incluyen descripción, cantidad y precio
empresa02 = [
    ('pepinos', 20, 1.95),
    ('pala basura', 5, 3.80),
    ('leche entera', 10, 1.90),
    ('pan mediano', 20, 0.5),
    ('vino blanco', 5, 14.25)
]

# Lista de tipos de productos válidos
productos_validos = ['frio', 'verduras', 'carnes', 'panadería', 'bazar', 'despensa', 'wines', 'lacteos']

# Integración de datos de la empresa 01
for tipo_producto, descripcion, cantidad, precio in empresa01:
    tipo_producto = tipo_producto.lower()  # Asegura que el tipo sea en minúsculas
    precio = round(precio, 2)  # Redondea el precio a dos decimales

    # Verifica si el tipo de producto es válido
    if tipo_producto not in productos_validos:
        print(f"Tipo de producto '{tipo_producto}' no es válido. Producto ignorado.")
        continue

    # Si el tipo no existe en productos, se inicializa como un diccionario vacío
    if tipo_producto not in productos:
        productos[tipo_producto] = {}

    # Busca si ya existe un producto con la misma descripción
    codigo_existente = None
    for codigo, (desc, ctdad, prc) in productos[tipo_producto].items():
        if desc == descripcion:
            codigo_existente = codigo
            break

    if codigo_existente:
        # Si existe, actualiza cantidad y precio
        productos[tipo_producto][codigo_existente][1] += cantidad
        productos[tipo_producto][codigo_existente][2] = max(precio, productos[tipo_producto][codigo_existente][2])
    else:
        # Si no existe, solicita un nuevo código al usuario y agrega el producto
        while True:
            num_codigo = input(f"Nuevo producto '{descripcion}' en categoría '{tipo_producto}'. Ingresa un número de código (4 dígitos): ")
            if len(num_codigo) == 4 and num_codigo.isdigit():
                nuevo_codigo = f"{tipo_producto[0]}{num_codigo}"
                if nuevo_codigo not in productos[tipo_producto]:
                    productos[tipo_producto][nuevo_codigo] = [descripcion, cantidad, precio]
                    break
                else:
                    print("El código ya existe. Intenta con otro.")
            else:
                print("El código debe ser de 4 dígitos.")

# Integración de datos de la empresa 02
for descripcion, cantidad, precio in empresa02:
    precio = round(precio, 2)  # Redondea el precio a dos decimales

    # Busca si ya existe un producto con la misma descripción en cualquier tipo de producto
    descripcion_encontrada = False
    for tipo_producto, productos_tipo in productos.items():
        for codigo, (desc, ctdad, prc) in productos_tipo.items():
            if desc == descripcion:
                productos[tipo_producto][codigo][1] += cantidad
                productos[tipo_producto][codigo][2] = max(precio, productos[tipo_producto][codigo][2])
                descripcion_encontrada = True
                break
        if descripcion_encontrada:
            break

    if not descripcion_encontrada:
        # Si no existe, solicita el tipo y el código del producto al usuario para crearlo
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
                            break
                        else:
                            print("El código ya existe. Intenta con otro.")
                    else:
                        print("El código debe ser de 4 dígitos.")
                break
            else:
                print(f"Tipo de producto inválido. Tipos válidos: {', '.join(productos_validos)}")

# Ciclo principal para gestionar manualmente productos
while True:
    print('\nBienvenido, introduce el dato solicitado o presiona ENTER para salir del programa.')

    # Solicita el tipo de producto
    tip_producto = input(f'Introduce el tipo de producto\nTipos disponibles: {", ".join(productos_validos)}\n-->   ').lower()

    if tip_producto == '':
        print("Saliste del programa...\n")
        break

    if tip_producto not in productos_validos:
        print(f"El tipo de producto no es válido. Tipos válidos son: {', '.join(productos_validos)}\n")
        continue

    # Solicita el código del producto
    while True:
        num_codigo = input(f"Introduce el código del producto (4 dígitos): ")
        if len(num_codigo) == 4 and num_codigo.isdigit():
            codigo = f"{tip_producto[0]}{num_codigo}"
            if codigo not in productos[tip_producto]:
                break
            else:
                print(f"El código {codigo} ya existe. ¿Quieres modificarlo?")
                opcion = input("1. Modificar cantidad\n2. Modificar precio\n3. No hacer cambios\n--> ")

                if opcion == '1':
                    cantidad_nueva = int(input(f"Ingrese la cantidad adicional para el producto '{productos[tip_producto][codigo][0]}': "))
                    productos[tip_producto][codigo][1] += cantidad_nueva

                elif opcion == '2':
                    precio_nuevo = float(input(f"Ingrese el nuevo precio para el producto '{productos[tip_producto][codigo][0]}': "))
                    productos[tip_producto][codigo][2] = round(precio_nuevo, 2)

                elif opcion == '3':
                    print("No se realizaron cambios.")
                break
        else:
            print("El código debe tener exactamente 4 dígitos.")

    # Si el código no existe, solicita los datos para crear un nuevo producto
    if codigo not in productos[tip_producto]:
        descripcion = input(f"Introduce la descripción del producto: ").lower()
        while True:
            try:
                cantidad = int(input(f"Introduce la cantidad del producto (solo número entero): "))
                break
            except ValueError:
                print("La cantidad debe ser un número entero.")
        while True:
            try:
                precio = float(input(f"Introduce el precio del producto: "))
                break
            except ValueError:
                print("El precio debe ser un número decimal.")
        productos[tip_producto][codigo] = [descripcion, cantidad, round(precio, 2)]

    # Muestra todos los productos almacenados
    print("\nProductos almacenados:")
    for categoria, productos_categoria in productos.items():
        print(f"\n{categoria.capitalize()}:")
        for codigo, (descripcion, cantidad, precio) in productos_categoria.items():
            print(f"  {codigo}: {descripcion} - {cantidad} unidades - {precio}€")