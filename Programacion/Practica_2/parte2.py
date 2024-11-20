# Estructura de datos

# productos = {tipo_producto1 : { código : [desc, ctdad, precio]},
#              tipo_producto2 : { código : [desc, ctdad, precio]} ... }

# descripción_del_producto, cantidad_exist_producto y el precio_venta_producto.

# Los tipos de productos permitidos son los siguientes: frío, verduras, carnes, panadería, bazar, despensa, vinos y lácteos.

# El código del producto es un string de 5 caracteres donde el primero de ellos indica el tipo de producto al que pertenece. Este primer caracter del código se
# obtiene del primer caracter del tipo de producto al que pertenece.

# desc es un string que representa la descripción del producto, ctdad es número flotante o entero que representa la existencia actual del producto,
# precio es un número float que representa el precio de venta del producto

productos = {}
