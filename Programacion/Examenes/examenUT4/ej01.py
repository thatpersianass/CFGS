# Desarrolle un sistema de inventario para una tienda de videojuegos utilizando programación orientada a objetos. El sistema debe implementar una jerarquía de
# clases con la siguiente jerarquía:
#   Constructor
#   Uso de getter y setter para los atributos precio_base y clasificación_por_edades
#   Un método calcularPrecioFinal() que devuelva el precio base
#   Un método mostrarInformacion() que muestre los detalles del videojuego

class Videojuego():
    '''
    Clase Videojuego que heredará a los Fisicos, Digitales y Coleccionistas
    '''
    
    PEGI = ['PEGI 3', 'PEGI 4', 'PEGI 6', 'PEGI 7', 'PEGI 12', 'PEGI 16', 'PEGI 18']
    
    def __init__(self, titulo:str, desarrollador:str, precio_base:float, anio_de_lanzamiento:int, clasificacion_por_edades:str):
        self.titulo = titulo
        self.desarrollador = desarrollador
        self.precio_base = precio_base if precio_base > 0 else 0.1
        self.anio_de_lanzamiento = anio_de_lanzamiento
        self.clasificacion_por_edades = clasificacion_por_edades
    
    def __str__(self):
        return self.mostrarInformacion()
    
    def calcularPrecioFinal(self):
        return self.precio_base
    
    def mostrarInformacion(self):
        return f"Titulo: {self.titulo}, Desarrollador: {self.desarrollador}, Clasificacion: {self.clasificacion_por_edades}, Precio: {self.precio_base}"
    
    @property
    def precio_base(self):
        return self._precio_base
    
    @precio_base.setter
    def precio_base(self, precio):
        if precio > 0:
            self._precio_base = precio
    
    @property
    def clasificacion_por_edades(self):
        return self._clasificacion_por_edades
    
    @clasificacion_por_edades.setter
    def clasificacion_por_edades(self, clasificacion):
        if clasificacion in self.PEGI:
            self._clasificacion_por_edades = clasificacion        
        else:
            raise ValueError(f"Clasificación inválida, tiene que ser uno de los siguientes:\n  {self.PEGI}")    

class JuegoFisico(Videojuego):
    '''
    Juegos Fisicos que heredan datos de la clase padre Videojuegos
    '''
    def __init__(self, titulo:str, desarrollador:str, precio_base:float, anio_de_lanzamiento:int, clasificacion_por_edades:str, plataforma:str, stock_disponible:int, costo_de_produccion:float):
        super().__init__(titulo, desarrollador, precio_base, anio_de_lanzamiento, clasificacion_por_edades)
        self.plataforma = plataforma
        self.stock_disponible = stock_disponible
        self.costo_de_produccion = costo_de_produccion
    
    def calcular_precio_final(self):
        return self.costo_de_produccion + (self.precio_base * 1.4)

    def mostrarInformacion(self):
        return f"Titulo: {self.titulo}, Desarrollador: {self.desarrollador}, Clasificacion: {self.clasificacion_por_edades}, Precio: {self.precio_base}, Plataforma: {self.plataforma.upper()}"
    
    def actualizarStock(self, cantidad):
        if self.stock_disponible + cantidad >= 0:
            self.stock_disponible += cantidad

class JuegoDigital(Videojuego):
    '''
    Juegos Digitales que heredan datos de la clase padre Videojuegos
    '''
    def __init__(self, titulo:str, desarrollador:str, precio_base:float, anio_de_lanzamiento:int, clasificacion_por_edades:str, tamanio_en_GB:int, descuento_promocional:float):
        super().__init__(titulo, desarrollador, precio_base, anio_de_lanzamiento, clasificacion_por_edades)
        self.tamanio_en_GB = tamanio_en_GB
        self.descuento_promocional = descuento_promocional
        
    def calcular_precio_final(self):
        return self.precio_base / self.descuento_promocional
    
    def mostrarInformacion(self):
        return f"Titulo: {self.titulo}, Desarrollador: {self.desarrollador}, Clasificacion: {self.clasificacion_por_edades}, Precio: {self.precio_base}, Tamaño: {self.tamanio_en_GB} GB"
        
    def actualizarDescuento(self,descuento_nuevo:float):
        if descuento_nuevo >= 0:
            self.descuento_promocional = descuento_nuevo
            
        else:
            raise ValueError('El descuento no puede ser menor de cero...')

class edicionColeccionista(Videojuego):
    '''
    Juegos de Edicion Coleccionista que heredan datos de la clase padre Videojuegos
    '''
    def __init__(self, titulo:str, desarrollador:str, precio_base:float, anio_de_lanzamiento:int, clasificacion_por_edades:str, contenidos_adicionales:list, cantidad_limitada:int):
        super().__init__(titulo, desarrollador, precio_base, anio_de_lanzamiento, clasificacion_por_edades)
        self.contenidos_adicionales = contenidos_adicionales
        self.cantidad_limitada = cantidad_limitada
    
    def calcular_precio_final(self):
        precio = self.precio_base * (1 + (0.1 * len(self.contenidos_adicionales)))
        if self.cantidad_limitada < 50:
            precio *= 1.2
        return precio
        
    def mostrarInformacion(self):
        return f"Titulo: {self.titulo}, Desarrollador: {self.desarrollador}, Clasificacion: {self.clasificacion_por_edades}, Precio: {self.precio_base}, Contenido adicional: {self.contenidos_adicionales}, Cantidad: {self.cantidad_limitada}"
    
    def agregarContenido(self, contenido):
        self.contenidos_adicionales.append(contenido)

class Tienda:
    def __init__(self):
        self.inventario = []
    
    def aniadir_videojuego(self, videojuego):
        self.inventario.append(videojuego)
    
    def eliminar_videojuego(self, titulo):
        self.inventario = [v for v in self.inventario if v.titulo != titulo]
    
    def buscar_videojuego(self, plataforma):
        juegos_encontrados = [v for v in self.inventario if isinstance(v, JuegoFisico) and v.plataforma == plataforma]
        return juegos_encontrados

    def actualizar_descuento(self, titulo, nuevo_descuento):
        for videojuego in self.inventario:
            if isinstance(videojuego, JuegoDigital) and videojuego.titulo == titulo:
                videojuego.actualizarDescuento(nuevo_descuento)
                print(f"Descuento actualizado para {titulo}. Nuevo descuento: {nuevo_descuento}")
                return
        print(f"El juego {titulo} no es un Juego Digital o no se encontró.")
    
    def agregar_contenido_a_coleccionista(self, titulo, contenido):
        for videojuego in self.inventario:
            if isinstance(videojuego, edicionColeccionista) and videojuego.titulo == titulo:
                videojuego.agregarContenido(contenido)
                print(f"Contenido '{contenido}' agregado a la edición coleccionista de {titulo}.")
                return
        print(f"El juego {titulo} no es de Edición Coleccionista o no se encontró.")


def main():
    tienda = Tienda()
    tienda = Tienda()
    juego1 = JuegoFisico("God of War", "Santa Monica", 50, 2018, "PEGI 18", "xbox", 10, 10)
    juego2 = JuegoDigital("Cyberpunk 2077", "CD Projekt", 60, 2020, "PEGI 18", 70, 0.2)
    juego3 = edicionColeccionista("Elden Ring", "FromSoftware", 80, 2022, "PEGI 18", ["Figura", "Mapa"], 30)
    
    tienda.aniadir_videojuego(juego1)
    tienda.aniadir_videojuego(juego2)
    tienda.aniadir_videojuego(juego3)
    
    while True:
        
        print(
            """
            --- Menú Tienda de Videojuegos ---
                1. Añadir Videojuego
                2. Eliminar Videojuego
                3. Buscar Videojuego físico por Plataforma
                4. Mostar Inventario
                5. Actualizar descuento de Juego Digital
                6. Agregar contenido a Edicion coleccionista
                0. Salir
            """
        )
        eleccion = input(" -->    ")
        
        if eleccion == "1":
            while True:
                eleccion = input('\n¿Qué tipo de videojuego deseas añadir?(Fisico, Digital, Coleccionista), o presiona Enter para salir.  --> ').lower()
                if eleccion == "fisico":
                    titulo = input('Introduzca el titulo del videojuego.  --> ')
                    desarrollador = input('Introduzca el desarrollador del videojuego.  --> ')
                    precio_base = float(input('Introduzca el precio base del videojuego.  --> '))
                    anio = int(input('Introduzca el año de lanzamiento del videojuego.  --> '))
                    clasificacion = input('Introduzca la clasificacion del videojuego (PEGI 18, 16, 12, 7, 6, 4, 3).  --> ')
                    plataforma = input('Introduzca la plataforma del videojuego.  --> ').lower()
                    stock = int(input('Introduzca el stock del videojuego.  --> '))
                    costo_produccion = float(input('Introduzca el costo de producción del videojuego.  --> '))
                    
                    nuevo_juego = JuegoFisico(titulo, desarrollador, precio_base, anio, clasificacion, plataforma, stock, costo_produccion)
                    tienda.aniadir_videojuego(nuevo_juego)
                    
                elif eleccion == "digital":
                    titulo = input('Introduzca el titulo del videojuego.  --> ')
                    desarrollador = input('Introduzca el desarrollador del videojuego.  --> ')
                    precio_base = float(input('Introduzca el precio base del videojuego.  --> '))
                    anio = int(input('Introduzca el año de lanzamiento del videojuego.  --> '))
                    clasificacion = input('Introduzca la clasificacion del videojuego (PEGI 18, 16, 12, 7, 6, 4, 3).  --> ')
                    tamanio = int(input('Introduzca el tamaño en GB del videojuego.  --> '))
                    descuento = float(input('Introduzca el descuento promocional del videojuego.  --> '))
                    
                    nuevo_juego = JuegoDigital(titulo, desarrollador, precio_base, anio, clasificacion, tamanio, descuento)
                    tienda.aniadir_videojuego(nuevo_juego)
                
                elif eleccion == "coleccionista":
                    titulo = input('Introduzca el titulo del videojuego.  --> ')
                    desarrollador = input('Introduzca el desarrollador del videojuego.  --> ')
                    precio_base = float(input('Introduzca el precio base del videojuego.  --> '))
                    anio = int(input('Introduzca el año de lanzamiento del videojuego.  --> '))
                    clasificacion = input('Introduzca la clasificacion del videojuego (PEGI 18, 16, 12, 7, 6, 4, 3).  --> ')
                    cantidad = int(input('Introduzca la cantidad de existencias del videojuego.  --> '))
                    while True:
                        lista_contenido = []
                        contenido = input('Introduzca el descuento promocional del videojuego. O presione Enter para salir.  --> ')
                        if contenido == "":
                            break
                        else:
                            lista_contenido.append(contenido)
                    
                    nuevo_juego = JuegoDigital(titulo, desarrollador, precio_base, anio, clasificacion, lista_contenido,cantidad)
                    tienda.aniadir_videojuego(nuevo_juego)

                elif eleccion == "5":
                    titulo = input('Introduzca el título del Juego Digital para actualizar el descuento.  --> ')
                    nuevo_descuento = float(input('Introduzca el nuevo descuento promocional (por ejemplo, 0.2 para 20%).  --> '))
                    tienda.actualizar_descuento(titulo, nuevo_descuento)
                
                elif eleccion == "6":
                    titulo = input('Introduzca el título del videojuego de Edición Coleccionista.  --> ')
                    contenido = input('Introduzca el contenido adicional a agregar.  --> ')
                    tienda.agregar_contenido_a_coleccionista(titulo, contenido)
        
                
                elif eleccion == "":
                    break
                
                else:
                    print('Elección inválida, seleccione una de las opciones que se muestran por pantalla...')
        
        elif eleccion == "2":
            while True:
                eleccion = input('Introduzca el titulo del videojuego que desea eliminar. O presione Enter para salir.  --> ')
                if eleccion == "":
                    break
                else:
                    tienda.eliminar_videojuego(eleccion)
        
        elif eleccion == "3":
            while True:
                plataforma = input('Introduzca la plataforma del videojuego. O presione Enter para salir.  --> ').lower()
                if plataforma == "":
                    break
                else:
                    juegos_encontrados = tienda.buscar_videojuego(plataforma)
                    if juegos_encontrados:
                        for juego in juegos_encontrados:
                            print(juego.mostrarInformacion(), "Precio Final:", juego.calcular_precio_final())
                    else:
                        print(f"No se encontraron juegos para la plataforma: {plataforma}")
        
        elif eleccion == "4":
            for juego in tienda.inventario:
                print(juego.mostrarInformacion(), "Precio Final:", juego.calcular_precio_final())

        elif eleccion == "5":
            titulo = input('Introduzca el título del Juego Digital para actualizar el descuento.  --> ')
            nuevo_descuento = float(input('Introduzca el nuevo descuento promocional (por ejemplo, 0.2 para 20%).  --> '))
            tienda.actualizar_descuento(titulo, nuevo_descuento)
        
        elif eleccion == "6":
            titulo = input('Introduzca el título del videojuego de Edición Coleccionista.  --> ')
            contenido = input('Introduzca el contenido adicional a agregar.  --> ')
            tienda.agregar_contenido_a_coleccionista(titulo, contenido)
        
        elif eleccion == "0":
            print('Saliendo del programa...')
            break
        
        else:
            print('Elección inválida, seleccione una de las opciones que se muestran por pantalla...')

if __name__ == "__main__":    
    main()