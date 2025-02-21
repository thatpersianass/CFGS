# Crear una clase de nombre Electrodomestico con las siguientes características:

# Sus atributos son precio base, color, consumo energético (letras entre ‘A’ y ‘F’) y peso.
# Por defecto, el color será blanco, el consumo energético será F, el precio base es de 100 € y el peso de 5 kg.

#     Los colores disponibles son blanco, negro, rojo, azul y gris.

#     El constructor de la clase debe cumplir las siguientes características:

#     Si se crea un objeto de la clase de la forma Electrodomestico(), se crea un objeto con todos los valores por defecto.

#     Si por el contrario el objeto se crea con la llamada Electrodomestico(precio=valor, peso=valor), 
#     entonces el objeto se crea con los atributos precio y peso con los valores asignados y el resto por defecto.

class Electrodomestico:
    def __init__(self, precio_base=100.0, peso=5.0, color='blanco', consumo_energetico='F'):
        self.precio_base = precio_base if precio_base > 0 else 100.0
        self.peso = peso if peso > 0 else 5.0

        colores_validos = ['blanco', 'negro', 'rojo', 'azul', 'gris']
        self.color = color if color in colores_validos else 'blanco'

        consumos_validos = ['A', 'B', 'C', 'D', 'E', 'F']
        self.consumo_energetico = consumo_energetico if consumo_energetico in consumos_validos else 'F'

    def __str__(self) -> str:
        return f'Precio base = {self.precio_base}, Color = {self.color}, Consumo = {self.consumo_energetico}, Peso = {self.peso}\n Precio de venta: {self.precioVenta()}'

    def precioVenta(self) -> float:
        precios_energia = {
            'A': 100, 'B': 80, 'C': 60, 'D': 50, 'E': 30, 'F': 10
        }
        if 0 <= self.peso <= 19:
            precio_peso = 10
        elif 20 <= self.peso <= 49:
            precio_peso = 50
        elif 50 <= self.peso <= 79:
            precio_peso = 80
        else:
            precio_peso = 100

        return self.precio_base + precios_energia[self.consumo_energetico] + precio_peso


if __name__ == '__main__':
    electro1 = Electrodomestico()  # Valores por defecto
    electro2 = Electrodomestico(precio_base=200, peso=55, consumo_energetico='B')

    print(electro1)
    # print(f'Precio de venta: {electro1.precioVenta()} €\n')

    print(electro2)
    # print(f'Precio de venta: {electro2.precioVenta()} €\n')
