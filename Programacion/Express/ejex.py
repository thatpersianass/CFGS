class Empleado():
    def __init__(self,id:str,nombre:str):
        self.id = id
        self.nombre = nombre
    
    def calcular_nomina(self):
        pass
    
    def __str__(self):
        return f'ID: {self.id} Nombre: {self.nombre}'
    
class EmpleadoCobroSemanal(Empleado):
    def __init__(self,id:str,nombre:str,salario_semanal:float):
        super().__init__(id,nombre)
        self.salario_semanal = salario_semanal
    
    def modificar_salario(self,nuevo_salario:float):
        self.salario_semanal = nuevo_salario
    
    def calcular_nomina(self):
        return self.salario_semanal
    
    def __str__(self):
        return super().__str__() + f' Salario Semanal: {self.salario_semanal} Tipo: Cobro Semanal'

class EmpleadoCobroHoras(Empleado):
    def __init__(self,id:str, nombre:str, horas:float, salario_hora:float):
        super().__init__(id,nombre)
        self.horas = horas
        self.salario_hora = salario_hora
    
    def modificar_nro_horas(self, nuevas_horas:float):
        self.horas = nuevas_horas
    
    def modificar_tarifa_hora(self,nuevo_salario:float):
        self.salario_hora = nuevo_salario
    
    def calcular_nomina(self):
        return self.horas * self.salario_hora
    
    def __str__(self):
        return super().__str__() + f' Horas: {self.horas} Salario por Hora: {self.salario_hora} Tipo: Cobro por Hora'

class EmpleadoAsociado(Empleado):
    def __init__(self,id:str, nombre:str, salario_semanal:float, importe_venta:float, comision_venta:float):
        super().__init__(id,nombre)
        self.salario_semanal = salario_semanal
        self.importe_venta = importe_venta
        self.comision_venta = comision_venta
    
    def modificar_salario(self, nuevo_salario:float):
        self.salario_semanal = nuevo_salario
        
    def modificar_importe_venta_semanal(self, nuevo_importe):
        self.importe_venta = nuevo_importe
        
    def modificar_comision_venta(self, nueva_comision):
        self.comision_venta = nueva_comision
    
    def calcular_nomina(self):
        return self.salario_semanal + self.importe_venta * self.comision_venta
    
    def __str__(self):
        return super().__str__() + f' Salario Semanal: {self.salario_semanal} Importe Venta Semanal: {self.importe_venta} Comision Venta: {self.comision_venta} Tipo: Asociado'

def mostrar_empleados(empleados):
    if not empleados:
        print("No hay empleados en la lista.")
        return

    print("\nLista de Empleados:")
    print(f"{'ID':<15} {'Nombre':<20} {'Tipo':<20} {'Salario Semanal':<15} {'Horas':<10} {'Salario por Hora':<15} {'Importe Venta':<15} {'Comisión':<15} {'Nómina':<10}")
    print("=" * 140)
    
    for empleado in empleados:
        tipo = type(empleado).__name__
        nomina = empleado.calcular_nomina()

        salario_semanal = "N/A"
        horas = "N/A"
        salario_por_hora = "N/A"
        importe_venta = "N/A"
        comision = "N/A"
        
        if isinstance(empleado, EmpleadoCobroSemanal):
            salario_semanal = empleado.salario_semanal
        elif isinstance(empleado, EmpleadoCobroHoras):
            horas = empleado.horas
            salario_por_hora = empleado.salario_hora
        elif isinstance(empleado, EmpleadoAsociado):
            salario_semanal = empleado.salario_semanal
            importe_venta = empleado.importe_venta
            comision = empleado.comision_venta
        
        print(f"{empleado.id:<15} {empleado.nombre:<20} {tipo:<20} {salario_semanal:<15} {horas:<10} {salario_por_hora:<15} {importe_venta:<15} {comision:<15} {nomina:<10.2f}")
    
    print("=" * 140)

empleados = [
    EmpleadoCobroSemanal(1, "Juan Pérez", 500),
    EmpleadoCobroSemanal(2, "Ana Gómez", 600),
    EmpleadoCobroHoras(3, "Carlos López", 40, 15),
    EmpleadoCobroHoras(4, "Laura Martínez", 35, 20),
    EmpleadoAsociado(5, "Pedro Sánchez", 400, 2000, 10),
    EmpleadoAsociado(6, "María Fernández", 450, 3000, 12)
]

mostrar_empleados(empleados)    