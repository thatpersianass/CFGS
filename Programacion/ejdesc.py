# import matplotlib.pyplot as plt

# class Rectangulo:
#     def __init__(self, x1, x2, y1, y2):
#         self.A = (x1, y1)
#         self.B = (x1, y2)
#         self.C = (x2, y2)
#         self.D = (x2, y1)
    
#     def __str__(self):
#         return f'A={self.A} B={self.B} C={self.C} D={self.D}'
    
#     def movHorizontal(self, dist):
#         self.A = (self.A[0] + dist, self.A[1])
#         self.B = (self.B[0] + dist, self.B[1])
#         self.C = (self.C[0] + dist, self.C[1])
#         self.D = (self.D[0] + dist, self.D[1])
    
#     def movVertical(self, dist):
#         self.A = (self.A[0], self.A[1] + dist)
#         self.B = (self.B[0], self.B[1] + dist)
#         self.C = (self.C[0], self.C[1] + dist)
#         self.D = (self.D[0], self.D[1] + dist)
    
#     def dibujar(self, titulo="Posición del Rectángulo"):
#         plt.figure(figsize=(6, 6))
#         x = [self.A[0], self.B[0], self.C[0], self.D[0], self.A[0]]
#         y = [self.A[1], self.B[1], self.C[1], self.D[1], self.A[1]]
#         plt.plot(x, y, 'bo-', label='Rectángulo')
        
#         plt.xlim(-10, 10)
#         plt.ylim(-5, 10)
#         plt.axhline(0, color='black', linewidth=0.5)
#         plt.axvline(0, color='black', linewidth=0.5)
#         plt.grid(True, linestyle='--', linewidth=0.5)
#         plt.legend()
#         plt.title(titulo)
#         plt.show()

# # Crear el rectángulo
# rect01 = Rectangulo(2, 6, 2, 4)
# rect01.dibujar("Rectángulo en la posición inicial")

# # Mover el rectángulo y mostrar cambios
# rect01.movHorizontal(3)
# rect01.movVertical(1)
# rect01.dibujar("Rectángulo después de moverse")


# # class Usuario:
# #     def __init__(self, dni, nombre, apellido1, apellido2 = "") -> None:
# #         self.nombre = nombre
# #         self.apellido1 = apellido1
# #         self.apellido2 = apellido2
# #         self.dni = dni
        
    
# #     def __str__(self) -> str:
# #         return f'{self.nombre} {self.apellido1} {self.apellido2}\n DNI: {self.dni}'

# # user1 = Usuario('12345678F', 'Pepe','García')

# # print(user1)

class Persona:
    def __init__(self, nombre: str, edad: int, nif: str):
        self.nombre = nombre
        self.edad = edad
        self.nif = nif

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("La edad debe ser un número entero positivo")
        self._edad = valor

    @property
    def nif(self):
        return self._nif

    @nif.setter
    def nif(self, valor):
        if not (isinstance(valor, str) and len(valor) == 8 and valor.isdigit()):
            raise ValueError("El DNI debe tener exactamente 8 caracteres y contener solo números")
        self._nif = valor

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, NIF: {self.nif}"

    
# Ejemplo de uso
persona = Persona("Juan Pérez", 25, "12345678")
print(persona)  # Salida: Nombre: Juan Pérez, Edad: 25, NIF: 12345678
