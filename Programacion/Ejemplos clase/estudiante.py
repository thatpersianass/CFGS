class Estudiante:
    def __init__(self, cial: str, nombre: str, estudios: str, curso: int):
        self.cial = cial
        self.nombre = nombre
        self.estudios = estudios
        self.curso = curso
        self.materias_actuales = []
        self.expediente_academico = {}
    
    def matricular(self, materia: str):
        if materia not in self.materias_actuales:
            self.materias_actuales.append(materia)
            print(f"{self.nombre} ha sido matriculado en {materia}.")
        else:
            print(f"{self.nombre} ya está matriculado en {materia}.")
    
    def dar_baja(self, materia: str):
        if materia in self.materias_actuales:
            self.materias_actuales.remove(materia)
            print(f"{self.nombre} ha sido dado de baja en {materia}.")
        else:
            print(f"{self.nombre} no está matriculado en {materia}.")
    
    def traspasar_a_expediente(self):
        self.expediente_academico[self.curso] = self.materias_actuales[:]
        self.materias_actuales.clear()
        print(f"Materias del curso {self.curso} trasladadas al expediente de {self.nombre}.")
    
    def obtener_promedio_curso(self):
        print(f"Promedio del curso actual para {self.nombre}: 0.00")
    
    def obtener_promedio_ciclo(self):
        print(f"Promedio del ciclo completo para {self.nombre}: 0.00")
    
    def actualizar_curso(self):
        self.curso += 1
        print(f"{self.nombre} ha sido promovido al curso {self.curso}.")

estudiante = Estudiante("12345678", "Juan Pérez", "Ingeniería", 1)

while True:
    print("\nMenú de Gestión Académica")
    print("1. Matricular")
    print("2. Dar Baja")
    print("3. Traspasar A Expediente")
    print("4. Obtener Promedio Curso")
    print("5. Obtener Promedio Ciclo")
    print("6. Actualizar Curso")
    print("7. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        materia = input("Ingrese la materia a matricular: ")
        estudiante.matricular(materia)
    elif opcion == "2":
        materia = input("Ingrese la materia a dar de baja: ")
        estudiante.dar_baja(materia)
    elif opcion == "3":
        estudiante.traspasar_a_expediente()
    elif opcion == "4":
        estudiante.obtener_promedio_curso()
    elif opcion == "5":
        estudiante.obtener_promedio_ciclo()
    elif opcion == "6":
        estudiante.actualizar_curso()
    elif opcion == "7":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
