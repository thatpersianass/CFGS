# Estructura de datos

# productos = {tipo_producto1 : { código : [desc, ctdad, precio]},
#              tipo_producto2 : { código : [desc, ctdad, precio]} ... }

# descripción_del_producto, cantidad_exist_producto y el precio_venta_producto.

# Los tipos de productos permitidos son los siguientes: frío, verduras, carnes, panadería, bazar, despensa, wines y lácteos.

# El código del producto es un string de 5 caracteres donde el primero de ellos indica el tipo de producto al que pertenece. Este primer caracter del código se
# obtiene del primer caracter del tipo de producto al que pertenece.

# desc es un string que representa la descripción del producto, ctdad es número flotante o entero que representa la existencia actual del producto,
# precio es un número float que representa el precio de venta del producto

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

while True:
    print('\nBienvenido, introduce el dato solicitado o presiona ENTER para salir del programa.')
    
    tip_producto = input(f'Introduce el tipo de producto\nTipos disponibles: {", ".join(productos_validos)}\n-->   ').lower()
    
    if tip_producto == '':
        print("Saliste del programa...\n")
        break

    if tip_producto not in productos_validos:
        print(f"El tipo de producto no es válido. Tipos válidos son: {', '.join(productos_validos)}\n")
        continue

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
                    print(f"Cantidad actualizada. Nueva cantidad: {productos[tip_producto][codigo][1]}")

                elif opcion == '2':
                    precio_nuevo = float(input(f"Ingrese el nuevo precio para el producto '{productos[tip_producto][codigo][0]}': "))
                    precio_nuevo = round(precio_nuevo, 2)
                    productos[tip_producto][codigo][2] = precio_nuevo
                    print(f"Precio actualizado. Nuevo precio: {productos[tip_producto][codigo][2]}")

                elif opcion == '3':
                    print("No se realizaron cambios.")
                break
        else:
            print("El código debe tener exactamente 4 dígitos.")

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
                precio = round(precio, 2)
                break
            except ValueError:
                print("El precio debe ser un número decimal.")

        productos[tip_producto][codigo] = [descripcion, cantidad, round(precio, 2)]
        print(f"Producto '{descripcion}' añadido con el código {codigo}.")

    print("\nProductos almacenados:")
    for categoria, productos_categoria in productos.items():
        print(f"\n{categoria.capitalize()}:")
        for codigo, (descripcion, cantidad, precio) in productos_categoria.items():
            print(f"  {codigo}: {descripcion} - {cantidad} unidades - {precio}€")

    print("\nProductos de la empresa 01:")
    for categoria, descripcion, cantidad, precio in empresa01:
        print(f"{categoria.capitalize()}: {descripcion} - {cantidad} unidades - {precio}€")

    print("\nProductos de la empresa 02:")
    for descripcion, cantidad, precio in empresa02:
        print(f"{descripcion} - {cantidad} unidades - {precio}€")