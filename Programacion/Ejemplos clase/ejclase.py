class Libro():
    def __init__(self, titulo:str , autor:str, genero:str, enprestamo:bool = False, nro_prestado:int = 0, nro_ejemplares:int = 1):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.enprestamo = enprestamo
        self.nro_prestado = nro_prestado
        self.nro_ejemplares = nro_ejemplares
    
    def __str__(self) -> str:
        return f"   Titulo del libro: {self.titulo}\n   Autor: {self.autor}\n   Genero literario: {self.genero}\n   Estado: {'En préstamo' if self.enprestamo else 'En biblioteca'}\n   Ejemplares: {self.nro_ejemplares}"
    
    def consultaGeneroLibro(self):
        return f"El genero del libro es: {self.genero}\n"
    
    def consultarSituaciónActual(self):
        return f"El libro {self.titulo} está {'en préstamo' if self.enprestamo else 'en biblioteca'}"
    
    def realizarPrestamo(self):
        if self.nro_ejemplares > 0 and not self.enprestamo:
            self.enprestamo = True
            self.nro_prestado += 1
            self.nro_ejemplares -= 1
            return f"El libro {self.titulo} ha sido prestado con éxito"
        else:
            return "El libro está prestado o no hay ejemplares disponibles"
        
    def procesarDevolucion(self):
        if self.enprestamo and self.nro_prestado > 0:
            self.nro_prestado -= 1
            self.nro_ejemplares += 1
            self.enprestamo = False
            return f"La devolución del libro {self.titulo} ha sido procesada con éxito"
        else:
            return "El libro no se encuentra en préstamo o ya ha sido devuelto"

libro1 = Libro("Quijote", "No sé", "Masculino", False, 3)

libro2 = Libro("Rubio", "Un rubio", "Masculino", False, 4)

while True:
    print("""
        MENU PRESTAMOS:
        1. Crea un Libro
        2. Realizar Prestamo de un libro
        3. Realizar devolucion de un libro
        4. Mostrar los datos de un libro
        5. Mostrar informe de prestamo de libros
        0. Salir
        """)
    opcion = int(input("Ingrese una opción: "))
    
    if opcion == 1:
        pass
    
    elif opcion == 2:
        pass
    
    elif opcion == 3:
        pass
    
    elif opcion == 4:
        pass
    
    elif opcion == 5:
        pass
    
    elif opcion == 0:
        break
