import datetime

# Clase base para los recursos de la biblioteca
class Recurso:
    def __init__(self, identificador, descripcion, nro_ejemplares):
        self.identificador = identificador
        self.descripcion = descripcion
        self.nro_ejemplares = nro_ejemplares

# Clase para los libros
class Libro(Recurso):
    def __init__(self, identificador, autor, titulo, editorial, nro_ejemplares):
        super().__init__(identificador, f"{titulo} de {autor}", nro_ejemplares)
        self.autor = autor
        self.titulo = titulo
        self.editorial = editorial
        self.ejem_prestamo = 0  # Ejemplares prestados

# Clase para las revistas
class Revista(Recurso):
    def __init__(self, identificador, nombre, fecha_publicacion, editorial):
        super().__init__(identificador, nombre, 1)  # Solo un ejemplar
        self.nombre = nombre
        self.fecha_publicacion = fecha_publicacion
        self.editorial = editorial

# Clase para las películas
class Pelicula(Recurso):
    def __init__(self, identificador, titulo, actores_principales, actores_secundarios, fecha_publicacion):
        super().__init__(identificador, titulo, 2)  # Dos ejemplares
        self.actores_principales = actores_principales
        self.actores_secundarios = actores_secundarios
        self.fecha_publicacion = fecha_publicacion
        self.estado_prestamo = True  # Indica si está disponible para préstamo
        self.titulo = titulo  # Agregar el atributo titulo

# Clase base para las personas
class Persona:
    def __init__(self, nif, nombre, telefono, direccion):
        self.nif = nif
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

# Clase para los usuarios ocasionales
class UsuarioOcasional(Persona):
    def __init__(self, nif, nombre, telefono, direccion):
        super().__init__(nif, nombre, telefono, direccion)
        self.recurso_solicitado = None
        self.fecha_hora_solicitud = None

# Clase para los socios
class Socio(Persona):
    def __init__(self, nif, nombre, telefono, direccion, nro_socio):
        super().__init__(nif, nombre, telefono, direccion)
        self.nro_socio = nro_socio
        self.nro_ejemplares_prestados = 0
        self.recursos_en_poder = []  # Lista de identificadores de recursos prestados

# Clase para los préstamos
class Prestamo:
    def __init__(self, recurso, usuario, fecha_solicitud):
        self.recurso = recurso
        self.usuario = usuario
        self.fecha_solicitud = fecha_solicitud
        self.fecha_max_devolucion = fecha_solicitud + datetime.timedelta(days=7)  # 7 días de préstamo
        self.fecha_devuelto = None

# Clase para la biblioteca
class Biblioteca:
    def __init__(self):
        self.recursos = []
        self.socios = []
        self.usuarios_ocasionales = []
        self.prestamos = []
        self.contador_prestamos = 1
        self.contador_consultas = 1

    def agregar_recurso(self, recurso):
        '''
        Primero verifica si el recurso ya existe. Si no, lo agrega a la lista. Si ya está, solo suma más ejemplares.
        '''
        for r in self.recursos:
            if isinstance(recurso, Libro) and isinstance(r, Libro) and r.titulo == recurso.titulo and r.autor == recurso.autor:
                if r.nro_ejemplares + recurso.nro_ejemplares <= 100:
                    r.nro_ejemplares += recurso.nro_ejemplares
                    print(f"Se han añadido {recurso.nro_ejemplares} ejemplares al libro '{r.titulo}' (ID: {r.identificador}).")
                else:
                    print("No se puede añadir más ejemplares, se ha alcanzado el límite.")
                return

            elif isinstance(recurso, Pelicula) and isinstance(r, Pelicula) and r.titulo == recurso.titulo:
                if r.nro_ejemplares < 2:
                    r.nro_ejemplares += 1
                    print(f"Se ha añadido un ejemplar a la película '{r.titulo}' (ID: {r.identificador}).")
                else:
                    print("No se puede añadir más ejemplares, ya hay 2 disponibles.")
                return
                
        self.recursos.append(recurso)
        print(f"Recurso '{recurso.descripcion}' (ID: {recurso.identificador}) añadido a la biblioteca.")

    def eliminar_recurso(self, identificador):
        '''
        Elimina un recurso de la biblioteca si no está en préstamo y maneja la reducción de ejemplares para libros.
        '''
        recurso_a_eliminar = None
        
        for recurso in self.recursos:
            if recurso.identificador == identificador:
                recurso_a_eliminar = recurso
                break
        
        if recurso_a_eliminar is None:
            print("Recurso no encontrado.")
            return
        
        for prestamo in self.prestamos:
            if prestamo.recurso == recurso_a_eliminar:
                print("No se puede eliminar el recurso, está en préstamo.")
                return
        
        if isinstance(recurso_a_eliminar, Libro):
            if recurso_a_eliminar.nro_ejemplares > 1:
                recurso_a_eliminar.nro_ejemplares -= 1
                print(f"Se ha reducido el número de ejemplares del libro '{recurso_a_eliminar.titulo}'.")
                return
            else:
                self.recursos.remove(recurso_a_eliminar)
                print(f"El libro '{recurso_a_eliminar.titulo}' ha sido eliminado de la biblioteca.")
                return
        
        if isinstance(recurso_a_eliminar, Revista):
            self.recursos.remove(recurso_a_eliminar)
            print(f"La revista '{recurso_a_eliminar.nombre}' ha sido eliminada de la biblioteca.")
            return
        
        if isinstance(recurso_a_eliminar, Pelicula):
            if recurso_a_eliminar.nro_ejemplares > 1:
                recurso_a_eliminar.nro_ejemplares -= 1
                print(f"Se ha reducido el número de ejemplares de la película '{recurso_a_eliminar.titulo}'.")
                return
            else:
                self.recursos.remove(recurso_a_eliminar)
                print(f"La película '{recurso_a_eliminar.titulo}' ha sido eliminada de la biblioteca.")
                return

    def consultar_estado_recurso(self, identificador):
        '''
        Verifica el estado de un recurso y muestra si está disponible o cuántos ejemplares están prestados
        '''
        recurso_encontrado = None
        
        for recurso in self.recursos:
            if recurso.identificador == identificador:
                recurso_encontrado = recurso
                break
        
        if recurso_encontrado is None:
            print("Recurso no encontrado.")
            return
        
        print(f"Estado del recurso '{recurso_encontrado.descripcion}':")
        print(f"  Identificador: {recurso_encontrado.identificador}")
        print(f"  Número de ejemplares: {recurso_encontrado.nro_ejemplares}")
        
        if isinstance(recurso_encontrado, Libro):
            print(f"  Autor: {recurso_encontrado.autor}")
            print(f"  Título: {recurso_encontrado.titulo}")
            print(f"  Editorial: {recurso_encontrado.editorial}")
            print(f"  Ejemplares prestados: {recurso_encontrado.ejem_prestamo}")
        
        elif isinstance(recurso_encontrado, Revista):
            print(f"  Nombre: {recurso_encontrado.nombre}")
            print(f"  Fecha de publicación: {recurso_encontrado.fecha_publicacion}")
            print(f"  Editorial: {recurso_encontrado.editorial}")
        
        elif isinstance(recurso_encontrado, Pelicula):
            print(f"  Título: {recurso_encontrado.titulo}")
            print(f"  Actores principales: {recurso_encontrado.actores_principales}")
            print(f"  Actores secundarios: {recurso_encontrado.actores_secundarios}")
            print(f"  Fecha de publicación: {recurso_encontrado.fecha_publicacion}")
            print(f"  Estado local: {'En uso' if recurso_encontrado.estado_local else 'Disponible'}")
            print(f"  Estado de préstamo: {'No disponible' if not recurso_encontrado.estado_prestamo else 'Disponible'}")


    def realizar_prestamo(self, recurso, socio):
        '''
        Permite a un socio tomar prestado un recurso si hay disponibilidad
        '''
        if socio.nro_ejemplares_prestados >= 3:
            print(f"El socio {socio.nombre} ya ha alcanzado el límite de préstamos.")
            return
        
        if isinstance(recurso, Libro):
            if recurso.ejem_prestamo < recurso.nro_ejemplares - 1:  # Al menos un ejemplar debe quedar en la biblioteca
                recurso.ejem_prestamo += 1
                socio.nro_ejemplares_prestados += 1
                socio.recursos_en_poder.append(recurso.identificador)
                print(f"Préstamo realizado: {socio.nombre} ha tomado prestado el libro '{recurso.titulo}'.")
            else:
                print(f"No hay ejemplares disponibles del libro '{recurso.titulo}' para préstamo.")
        
        elif isinstance(recurso, Pelicula):
            if recurso.estado_prestamo:
                recurso.estado_prestamo = False
                socio.nro_ejemplares_prestados += 1
                socio.recursos_en_poder.append(recurso.identificador)
                print(f"Préstamo realizado: {socio.nombre} ha tomado prestada la película '{recurso.titulo}'.")
            else:
                print(f"La película '{recurso.titulo}' no está disponible para préstamo.")
        
        elif isinstance(recurso, Revista):
            print("Las revistas no se pueden prestar, solo se pueden consultar en la biblioteca.")
            return
        
        fecha_solicitud = datetime.datetime.now()
        prestamo = Prestamo(recurso, socio, fecha_solicitud)
        self.prestamos.append(prestamo)

    def devolver_recurso(self, prestamo):
        '''
        Registra la devolución de un recurso y actualiza los números
        '''
        prestamo.fecha_devuelto = datetime.datetime.now()
        
        recurso = prestamo.recurso
        socio = prestamo.usuario
        
        if isinstance(recurso, Libro):
            recurso.ejem_prestamo -= 1
            print(f"El libro '{recurso.titulo}' ha sido devuelto.")
        elif isinstance(recurso, Pelicula):
            recurso.estado_prestamo = True
            print(f"La película '{recurso.titulo}' ha sido devuelta.")

        if isinstance(socio, Socio):
            socio.nro_ejemplares_prestados -= 1
            if recurso.identificador in socio.recursos_en_poder:
                socio.recursos_en_poder.remove(recurso.identificador)
        
        print(f"Recurso '{recurso.descripcion}' devuelto por {socio.nombre}.")

    def renovar_prestamo(self, prestamo):
        '''
        Renueva un préstamo si no ha sido devuelto y no se ha alcanzado el límite
        '''
        if prestamo.fecha_devuelto is not None:
            print("El préstamo ya ha sido devuelto y no se puede renovar.")
            return

        if hasattr(prestamo, 'renovaciones'):
            if prestamo.renovaciones >= 3:
                print("Se ha alcanzado el límite de renovaciones.")
                return
        else:
            prestamo.renovaciones = 0

        prestamo.renovaciones += 1

        prestamo.fecha_max_devolucion += datetime.timedelta(days=7)
        print(f"Préstamo renovado. Nueva fecha de devolución: {prestamo.fecha_max_devolucion}")

    def agregar_socio(self, socio):
        '''
        Agrega un nuevo socio si no está registrado
        '''
        for s in self.socios:
            if s.nif == socio.nif or s.nro_socio == socio.nro_socio:
                print("El socio ya está registrado.")
                return

        self.socios.append(socio)
        print(f"Socio '{socio.nombre}' agregado exitosamente.")

    def eliminar_socio(self, nro_socio):
        '''
        Elimina un socio si no tiene préstamos activos
        '''
        socio_a_eliminar = None

        for socio in self.socios:
            if socio.nro_socio == nro_socio:
                socio_a_eliminar = socio
                break
        
        if socio_a_eliminar is None:
            print("Socio no encontrado.")
            return

        if socio_a_eliminar.nro_ejemplares_prestados > 0:
            print("No se puede eliminar el socio, tiene recursos en préstamo.")
            return

        self.socios.remove(socio_a_eliminar)
        print(f"Socio '{socio_a_eliminar.nombre}' eliminado exitosamente.")
        
    def consultar_socios(self):
        '''
        Busca socios y muestra sus detalles
        '''
        if not self.socios:
            print("No hay socios registrados.")
            return

        print("Socios registrados:")
        for socio in self.socios:
            print(f"{socio.nro_socio}. {socio.nombre} - {socio.nif}")

        criterio = input("Introduce el ID del socio que deseas consultar: ")
        socio_encontrado = next((s for s in self.socios if s.nro_socio == criterio), None)

        if socio_encontrado:
            print(f"Detalles del socio: ID: {socio_encontrado.nro_socio}, Nombre: {socio_encontrado.nombre}, NIF: {socio_encontrado.nif}, Teléfono: {socio_encontrado.telefono}, Dirección: {socio_encontrado.direccion}, Ejemplares Prestados: {socio_encontrado.nro_ejemplares_prestados}")
        else:
            print("Socio no encontrado.")


def main():
    biblioteca = Biblioteca()

    while True:
        print(
        """
        --- Menú de Biblioteca ---
            1. Agregar Recurso
            2. Agregar Socio
            3. Realizar Préstamo
            4. Devolver Recurso
            5. Renovar Préstamo
            6. Consultar Socios
            7. Eliminar Socio
            8. Eliminar Recurso
            9. Consultar Estado de Recurso
            0. Salir
        """
        )
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Agregar Recurso
            tipo = input("¿Qué tipo de recurso es? (libro/pelicula): ").strip().lower()
            if tipo == "libro":
                autor = input("Autor: ")
                titulo = input("Título: ")
                editorial = input("Editorial: ")
                nro_ejemplares = int(input("Número de ejemplares: "))
                libro = Libro(f"LIB-{titulo}", autor, titulo, editorial, nro_ejemplares)
                biblioteca.agregar_recurso(libro)
            elif tipo == "pelicula":
                titulo = input("Título: ")
                actores_principales = input("Actores principales (separados por comas): ").split(",")
                actores_secundarios = input("Actores secundarios (separados por comas): ").split(",")
                fecha_publicacion = input("Fecha de publicación (DD/MM/AAAA): ")
                pelicula = Pelicula(f"PEL-{titulo}", titulo, actores_principales, actores_secundarios, fecha_publicacion)
                biblioteca.agregar_recurso(pelicula)
            else:
                print("Tipo de recurso no válido.")

        elif opcion == "2":
            # Agregar Socio
            nif = input("NIF: ")
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            direccion = input("Dirección: ")
            nro_socio = input("Número de socio: ")
            socio = Socio(nif, nombre, telefono, direccion, nro_socio)
            biblioteca.agregar_socio(socio)

        elif opcion == "3":
            # Realizar Préstamo
            nro_socio = input("Número de socio: ")
            recurso_id = input("Identificador del recurso: ")
            socio = next((s for s in biblioteca.socios if s.nro_socio == nro_socio), None)
            recurso = next((r for r in biblioteca.recursos if r.identificador == recurso_id), None)
            if socio and recurso:
                biblioteca.realizar_prestamo(recurso, socio)
            else:
                print("Socio o recurso no encontrado.")

        elif opcion == "4":
            # Devolver Recurso
            prestamo_id = input("Identificador del préstamo: ")
            prestamo = next((p for p in biblioteca.prestamos if p.recurso.identificador == prestamo_id), None)
            if prestamo:
                biblioteca.devolver_recurso(prestamo)
            else:
                print("Préstamo no encontrado.")

        elif opcion == "5":
            # Renovar Préstamo
            prestamo_id = input("Identificador del préstamo: ")
            prestamo = next((p for p in biblioteca.prestamos if p.recurso.identificador == prestamo_id), None)
            if prestamo:
                biblioteca.renovar_prestamo(prestamo)
            else:
                print("Préstamo no encontrado.")

        elif opcion == "6":
            # Consultar Socios
            biblioteca.consultar_socios()

        elif opcion == "7":
            # Eliminar Socio
            nro_socio = input("Número de socio a eliminar: ")
            biblioteca.eliminar_socio(nro_socio)

        elif opcion == "8":
            # Eliminar Recurso
            recurso_id = input("Identificador del recurso a eliminar: ")
            biblioteca.eliminar_recurso(recurso_id)

        elif opcion == "9":
            # Consultar Estado de Recurso
            recurso_id = input("Identificador del recurso: ")
            recurso = next((r for r in biblioteca.recursos if r.identificador == recurso_id), None)
            if recurso:
                estado = "Disponible" if recurso.ejem_prestamo < recurso.nro_ejemplares else "No disponible"
                print(f"El recurso '{recurso.descripcion}' está {estado}.")
            else:
                print("Recurso no encontrado.")

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Por favor, selecciona otra.")

if __name__ == "__main__":
    main()