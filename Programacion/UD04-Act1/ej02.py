import json
import os

class Producto:
    def __init__(self, id_producto, nombre, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Precio: {self.precio}"

class Inventariable:
    def __init__(self):
        self.stock = 0

    def agregar_stock(self, cantidad):
        self.stock += cantidad

    def vender(self, cantidad):
        if cantidad > self.stock:
            print(f"No hay suficiente stock. Disponible: {self.stock}")
        else:
            self.stock -= cantidad

    def __str__(self):
        return f"Stock: {self.stock}"

class Electronico(Producto, Inventariable):
    def __init__(self, id_producto, nombre, precio, garantia):
        Producto.__init__(self, id_producto, nombre, precio)
        Inventariable.__init__(self)
        self.garantia = garantia

    def __str__(self):
        return super().__str__() + f", Garantía: {self.garantia} meses"

class Ropa(Producto, Inventariable):
    def __init__(self, id_producto, nombre, precio, talla, material):
        Producto.__init__(self, id_producto, nombre, precio)
        Inventariable.__init__(self)
        self.talla = talla
        self.material = material

    def __str__(self):
        return super().__str__() + f", Talla: {self.talla}, Material: {self.material}"

class Alimento(Producto, Inventariable):
    def __init__(self, id_producto, nombre, precio, fecha_expiracion):
        Producto.__init__(self, id_producto, nombre, precio)
        Inventariable.__init__(self)
        self.fecha_expiracion = fecha_expiracion

    def __str__(self):
        return super().__str__() + f", Fecha de Expiración: {self.fecha_expiracion}"

class Inventario:
    def __init__(self, archivo):
        self.productos = []
        self.archivo = archivo
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga productos desde un archivo JSON."""
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r', encoding='utf8') as f:
                    productos_data = json.load(f)
                    for data in productos_data:
                        if 'garantia' in data:  # Electronico
                            producto = Electronico(data['id_producto'], data['nombre'], data['precio'], data['garantia'])
                        elif 'talla' in data:  # Ropa
                            producto = Ropa(data['id_producto'], data['nombre'], data['precio'], data['talla'], data['material'])
                        elif 'fecha_expiracion' in data:  # Alimento
                            producto = Alimento(data['id_producto'], data['nombre'], data['precio'], data['fecha_expiracion'])
                        else:
                            continue
                        producto.stock = data.get('stock', 0)  # Cargar stock
                        self.agregar_producto(producto)
                print("Inventario cargado desde", self.archivo)
            except json.JSONDecodeError:
                print("Error al decodificar el archivo JSON.")
        else:
            print("El archivo no existe. Se creará uno nuevo.")

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_inventario(self):
        if not self.productos:
            print("No hay productos en el inventario.")
            return

        print("\nLista de Productos:")
        print(f"{'ID Producto':<15} {'Nombre':<20} {'Precio':<10} {'Stock':<10} {'Tipo':<15}")
        print("=" * 70)
        for producto in self.productos:
            tipo = type(producto).__name__
            print(f"{producto.id_producto:<15} {producto.nombre:<20} {producto.precio:<10} {producto.stock:<10} {tipo:<15}")
        print("=" * 70)

    def actualizar_stock(self, id_producto, cantidad):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                producto.agregar_stock(cantidad)
                print(f"Stock actualizado para {producto.nombre}. Nuevo stock: {producto.stock}")
                return
        print("Producto no encontrado.")

    def realizar_venta(self, id_producto, cantidad):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                producto.vender(cantidad)
                if producto.stock == 0:
                    self.productos.remove(producto)
                    print(f"Producto {producto.nombre} eliminado del inventario por falta de stock.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre=None, tipo=None):
        found = False
        for producto in self.productos:
            if (nombre and nombre.lower() in producto.nombre.lower()):
                print(producto)
                found = True
            elif tipo:
                if tipo == 'Electronico' and isinstance(producto, Electronico):
                    print(producto)
                    found = True
                elif tipo == 'Ropa' and isinstance(producto, Ropa):
                    print(producto)
                    found = True
                elif tipo == 'Alimento' and isinstance(producto, Alimento):
                    print(producto)
                    found = True
        if not found:
            print("No se encontraron productos que coincidan con la búsqueda.")

    def guardar_inventario(self):
        """Guarda productos en un archivo JSON."""
        try:
            with open(self.archivo, 'w', encoding='utf8') as f:
                json.dump([vars(p) for p in self.productos], f, indent=4)
                print("Inventario guardado en", self.archivo)
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")

# Funciones del menú
def menu():
    directorio_actual = os.getcwd()
    archivo_json = os.path.join(directorio_actual, 'inventario.json')  # Ruta del archivo JSON
    inventario = Inventario(archivo_json)
    
    while True:
        print("""
            --- Menú de Inventario ---
            1. Agregar producto
            2. Mostrar inventario
            3. Actualizar stock
            4. Realizar venta
            5. Buscar producto
            6. Guardar inventario
            0. Salir
        """)
        
        opcion = input("    Seleccione una opción: ")

        if opcion == '1':
            tipo = input("Ingrese el tipo de producto (Electronico/Ropa/Alimento): ").strip().lower()
            id_producto = int(input("Ingrese el ID del producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            
            if tipo == 'electronico':
                garantia = int(input("Ingrese la garantía en meses: "))
                producto = Electronico(id_producto, nombre, precio, garantia)
            elif tipo == 'ropa':
                talla = input("Ingrese la talla: ")
                material = input("Ingrese el material: ")
                producto = Ropa(id_producto, nombre, precio, talla, material)
            elif tipo == 'alimento':
                fecha_expiracion = input("Ingrese la fecha de expiración (YYYY-MM-DD): ")
                producto = Alimento(id_producto, nombre, precio, fecha_expiracion)
            else:
                print("Tipo de producto no válido.")
                continue
            
            inventario.agregar_producto(producto)
            print(f"Producto {nombre} agregado al inventario.")

        elif opcion == '2':
            inventario.mostrar_inventario()

        elif opcion == '3':
            id_producto = int(input("Ingrese el ID del producto a actualizar: "))
            cantidad = int(input("Ingrese la cantidad a agregar: "))
            inventario.actualizar_stock(id_producto, cantidad)

        elif opcion == '4':
            id_producto = int(input("Ingrese el ID del producto a vender: "))
            cantidad = int(input("Ingrese la cantidad a vender: "))
            inventario.realizar_venta(id_producto, cantidad)

        elif opcion == '5':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            tipo = input("Ingrese el tipo de producto a buscar (Electronico/Ropa/Alimento) o dejar en blanco: ").strip().lower()
            if tipo == '':
                tipo = None
            inventario.buscar_producto(nombre, tipo)

        elif opcion == '6':
            inventario.guardar_inventario()

        elif opcion == '0':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()