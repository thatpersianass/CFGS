import pytest
from primos import es_primo

def test_primo():
    assert es_primo(2) == True  # Caso base, el primer número primo
    assert es_primo(3) == True  # Otro primo pequeño
    assert es_primo(17) == True # Número primo mayor

def test_no_primo():
    assert es_primo(1) == False  # Menor que 2
    assert es_primo(4) == False  # Número compuesto
    assert es_primo(15) == False # Otro número compuesto

def test_limites():
    assert es_primo(0) == False  # Límite inferior
    assert es_primo(2) == True   # Mínimo número primo
    assert es_primo(100) == False # Número compuesto grande
