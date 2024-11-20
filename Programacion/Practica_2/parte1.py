# Estructura de datos

# productos = {tipo_producto1 : { código : [desc, ctdad, precio]},
#              tipo_producto2 : { código : [desc, ctdad, precio]} ... }

# descripción_del_producto, cantidad_exist_producto y el precio_venta_producto.

# Los tipos de productos permitidos son los siguientes: frío, verduras, carnes, panadería, bazar, despensa, wines y lácteos.

# El código del producto es un string de 5 caracteres donde el primero de ellos indica el tipo de producto al que pertenece. Este primer caracter del código se
# obtiene del primer caracter del tipo de producto al que pertenece.

# desc es un string que representa la descripción del producto, ctdad es número flotante o entero que representa la existencia actual del producto,
# precio es un número float que representa el precio de venta del producto

productos = {}

productos_validos = ['frío','verduras','carnes','panadería','bazar','despensa','wines','lácteos']

while True:
    codigo = None
    modificar = False

    print('\nBienvenido, introduce el dato solicitado o presiona ENTER para salir del programa.')

    while True:
        tip_producto = input(f'Introduce el tipo de producto\nTipos disponibles: {', '.join(productos_validos)}\n-->   ')
        if tip_producto == '':
            print(f'Saliste del programa...\n')
            break

        if tip_producto not in productos_validos:
            print(f'El tipo de producto no es válido, los tipos válidos son:\n{productos_validos}\n')
        else:
            break

    if tip_producto == '':
        break

    while True:
        num_codigo = input('Introduce el numero del código de producto (Máxmimo 4 caracteres)\n-->   ')
        if 0 < len(num_codigo) <= 4 and num_codigo.isdigit():
            if productos:
                codigo = tip_producto[0].upper() + num_codigo
                if codigo not in productos[tip_producto]:
                    break
                else:
                    i = input('Código existente... Desea modificar los datos de este producto?\n(1)SI\n(2)NO\n-->   ')
                    if i == 1:
                        modificar = True
                        break
                    if i != 1 or i != 2:
                        print('Selección inválida, se toma como un NO...')

            else:
                codigo = tip_producto[0].upper() + num_codigo
                break
        else:
            print('El código introducido no es válido, tienen que ser números enteros y tener una longitud de máximo 4 digitos...\n')

    if modificar != True:
        while True:
            descripcion = input('Introduce la descripción del producto\n-->   ')
            if len(descripcion) == 0:
                print('Se debe introducir la descripcion obligatoriamente...\n')
            else:
                break

        while True:
            try:
                cantidad = float(input('Introduce la cantidad del producto\n-->   '))
            except ValueError:
                print('La cantidad tiene que ser un número decimal...\n')
            else:
                break

        while True:
            try:
                precio = float(input('Introduce el precio del producto\n-->   '))
            except ValueError:
                print('El precio tiene que ser un número decimal...\n')
            else:
                break

    if modificar:
        while True:
            try:
                cantidad = float(input(f'Introduzca cuanto le quiere SUMAR a la cantidad actual de producto ({productos[tip_producto][codigo][1]}) SUMAR 0 SI NO SE DESEA CAMBIAR'))
            except ValueError:
                print('Tiene que ser un número decimal....')
            else:
                if cantidad != 0:
                    productos[tip_producto][codigo][1] += cantidad
                    break
                else:
                    print('Saltando paso...\n')
                    break

        while True:
            try
    if tip_producto not in productos:
        productos[tip_producto] = {}

    productos[tip_producto][codigo] = [descripcion, cantidad, precio]

    print(f"\nEl producto {descripcion} ha sido añadido a la categoría {tip_producto}, con código {codigo}, con precio {precio}€ y {cantidad} existencias")

print(productos)