class Persona:
    def __init__(self, nombre: str, edad: int, nif: str):        
        self.nombre = nombre
        self.edad = edad
        self.nif = nif

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad: int):
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
        self._edad = edad

    @property
    def nif(self):
        return self._nif

    @nif.setter
    def nif(self, nif: str):
        if len(nif) != 9 or not nif[:8].isdigit() or not nif[8].isalpha():
            raise ValueError("El NIF debe tener 8 dígitos seguidos de una letra")
        self._nif = nif.upper()

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, NIF: {self.nif[:3]}***{self.nif[-2:]}"

while True:
    try:
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        nif = input("Ingrese su NIF (8 números y 1 letra): ")
        persona = Persona(nombre, edad, nif)
        print("\nDatos de la persona:")
        print(persona)
        break
    except ValueError as e:
        print(f"Error: {e}. Intente nuevamente.\n")