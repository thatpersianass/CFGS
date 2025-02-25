class Fraccion:
    def __init__(self, num, den):
        if den == 0:
            raise ValueError("El denominador no puede ser cero.")
        self.num = num
        self.den = den
        self.simplifica()

    def __str__(self):
        return f"{self.num} / {self.den}"

    def mcd(self, a, b):
        """Calcula el máximo común divisor usando el algoritmo de Euclides."""
        while b:
            a, b = b, a % b
        return abs(a)

    def simplifica(self):
        divisor = self.mcd(self.num, self.den)
        self.num //= divisor
        self.den //= divisor
        if self.den < 0:  # Aseguramos que el denominador sea positivo
            self.num = -self.num
            self.den = -self.den

    @staticmethod
    def suma(a, b):
        num = a.num * b.den + b.num * a.den
        den = a.den * b.den
        return Fraccion(num, den)

    @staticmethod
    def resta(a, b):
        num = a.num * b.den - b.num * a.den
        den = a.den * b.den
        return Fraccion(num, den)

    @staticmethod
    def multiplicacion(a, b):
        num = a.num * b.num
        den = a.den * b.den
        return Fraccion(num, den)

    @staticmethod
    def division(a, b):
        if b.num == 0:
            raise ValueError("No se puede dividir por cero.")
        num = a.num * b.den
        den = a.den * b.num
        return Fraccion(num, den)

    @staticmethod
    def multpornumero(frac, num):
        return Fraccion(frac.num * num, frac.den)

    @staticmethod
    def cambiarsigno(fracc):
        return Fraccion(-fracc.num, fracc.den)

    @staticmethod
    def potencia(fracc, exponente):
        return Fraccion(fracc.num ** exponente, fracc.den ** exponente)

# Programa principal para probar la clase Fracción
if __name__ == "__main__":
    f1 = Fraccion(1, 2)
    f2 = Fraccion(3, 4)

    print("Fracción 1:", f1)
    print("Fracción 2:", f2)

    print("Suma:", Fraccion.suma(f1, f2))
    print("Resta:", Fraccion.resta(f1, f2))
    print("Multiplicación:", Fraccion.multiplicacion(f1, f2))
    print("División:", Fraccion.division(f1, f2))
    print("Multiplicar por número:", Fraccion.multpornumero(f1, 3))
    print("Cambiar signo:", Fraccion.cambiarsigno(f1))
    print("Potencia:", Fraccion.potencia(f1, 2))
    
    
