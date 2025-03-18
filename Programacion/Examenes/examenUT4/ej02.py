import random

class Carta:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor

    def __str__(self):
        return f"{self.valor} de {self.palo}"
    
    def __eq__(self, otra):
        return self.palo == otra.palo and self.valor == otra.valor
    
    def __lt__(self, otra):
        valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        valor_self = valores.index(self.valor)
        valor_otro = valores.index(otra.valor)
        return valor_self < valor_otro

class Mazo:
    def __init__(self):
        palos = ['trébol', 'picas', 'corazones', 'diamantes']
        valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        
        self.cartas = [Carta(palo, valor) for palo in palos for valor in valores]
        self.barajar()

    def __len__(self):
        return len(self.cartas)
    
    def __iter__(self):
        return iter(self.cartas)
    
    def __getitem__(self, indice):
        return self.cartas[indice]
    
    def repartir(self, n):
        cartas_repartidas = self.cartas[:n]
        self.cartas = self.cartas[n:]
        return cartas_repartidas
    
    def barajar(self):
        random.shuffle(self.cartas)

# Cree un programa principal que genere un mazo de cartas de poker y permita demostrar el uso de todas las funcionalidades programadas 

def main():
    # Crear un mazo de cartas
    mazo = Mazo()
    print("Mazo creado y barajado.")
    
    # Ver el número de cartas en el mazo
    print(f"Cartas en el mazo: {len(mazo)}")
    
    # Repartir 5 cartas
    cartas_repartidas = mazo.repartir(5)
    print("\n5 cartas repartidas:")
    for carta in cartas_repartidas:
        print(carta)
    
    # Ver el número de cartas restantes
    print(f"\nCartas restantes en el mazo: {len(mazo)}")
    
    # Iterar sobre el mazo
    print("\nCartas restantes en el mazo:")
    for carta in mazo:
        print(carta)
    
    # Comparar dos cartas
    carta1 = mazo[0]
    carta2 = mazo[1]
    print(f"\nComparando las cartas {carta1} y {carta2}:")
    if carta1 == carta2:
        print("Las cartas son iguales.")
    elif carta1 < carta2:
        print(f"{carta1} es menor que {carta2}.")
    else:
        print(f"{carta1} es mayor que {carta2}.")
    
    # Ver el número de cartas restantes tras repartir y comparar
    print(f"\nCartas restantes en el mazo: {len(mazo)}")

if __name__ == "__main__":
    main()