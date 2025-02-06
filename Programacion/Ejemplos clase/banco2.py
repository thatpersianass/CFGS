class CuentaBancaria:
    def __init__(self, titular: str, nif: str, saldo: float, limite_retiro: float):
        self._titular = None
        self._nif = None
        self._saldo = None
        self._limite_retiro = None
        
        self.titular = titular
        self.nif = nif
        self.saldo = saldo
        self.limite_retiro = limite_retiro
    
    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El titular no puede estar vacío.")
        self._titular = valor.strip()
    
    @property
    def nif(self):
        return self._nif

    @nif.setter
    def nif(self, valor):
        if len(valor) != 9 or not valor[:8].isdigit() or not valor[8].isalpha():
            raise ValueError("El NIF debe tener 8 dígitos seguidos de una letra.")
        self._nif = valor.upper()
    
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo.")
        self._saldo = valor
    
    @property
    def limite_retiro(self):
        return self._limite_retiro

    @limite_retiro.setter
    def limite_retiro(self, valor):
        if valor <= 0:
            raise ValueError("El límite de retiro debe ser un número positivo.")
        self._limite_retiro = valor
    
    def depositar(self, monto: float):
        if monto > 0:
            self.saldo += monto
            print(f"Se ha depositado {monto} en la cuenta. Nuevo saldo: {self.saldo}")
        else:
            raise ValueError("El monto a depositar debe ser positivo.")
    
    def retirar(self, cantidad: float):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        if cantidad > self.limite_retiro:
            raise ValueError(f"La cantidad excede el límite de retiro de {self.limite_retiro}")
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            print(f"Se ha retirado {cantidad} de la cuenta. Nuevo saldo: {self.saldo}")
        else:
            raise ValueError("No tienes suficiente saldo en tu cuenta.")
    
    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}")
    
    def mostrar_informacion(self):
        print("Información de la cuenta:")
        print(f"Titular: {self.titular}")
        print(f"NIF: {self.nif[:3]}*****{self.nif[-2:]}")
        print(f"Saldo: {self.saldo}")
        print(f"Límite de retiro: {self.limite_retiro}")

while True:
    print("\nSeleccione una opción con los números indicados abajo:")
    print("1. Crear cuenta")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Mostrar saldo")
    print("5. Mostrar información de la cuenta")
    print("0. Salir")
    
    try:
        opt = int(input("-->   "))
        
        if opt == 0:
            break
        
        if opt == 1:
            titular = input("Ingrese el titular: ")
            nif = input("Ingrese el NIF (8 dígitos seguidos de una letra): ")
            saldo = float(input("Ingrese el saldo inicial: "))
            limite_retiro = float(input("Ingrese el límite de retiro: "))
    
            cuenta = CuentaBancaria(titular, nif, saldo, limite_retiro)
            print("Cuenta creada correctamente.")
    
        elif opt == 2:
            monto = float(input("Ingrese el monto a depositar: "))
            cuenta.depositar(monto)
        
        elif opt == 3:
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cuenta.retirar(cantidad)
        
        elif opt == 4:
            cuenta.mostrar_saldo()
        
        elif opt == 5:
            cuenta.mostrar_informacion()
        
    except ValueError as e:
        print(f"Error: {str(e)}")
        continue
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
    
    print()