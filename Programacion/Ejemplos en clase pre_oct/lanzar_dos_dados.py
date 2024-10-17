# mostrar los valores posibles al Lanzar dos dados

for dado1 in range(1,7):
    for dado2 in range(1, dado1 +1):
        print(f'({dado1},{dado2})', end=' ')
    print()