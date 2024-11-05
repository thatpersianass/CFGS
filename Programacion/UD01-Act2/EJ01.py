    # Escribir un programa en Python que comienza pidiendo una frase o palabra al usuario. Una vez leída la frase o palabra el programa deberá generar un nuevo
    # string a partir de las letras que contengan.

    # En el string construído deben aparecer todas las letras (sin repetir) que estén dentro de la frase o palabra leída ordenadas de forma decreciente. Los espacios
    # en blanco en la frase se deben omitir. El string generado debe estar en minúsculas.

    # Ejemplos:
    # abecedario -> abcdeior
    # zapatero a tus zapatos -> aeoprstuz

i = input('Inserte una palabra: ')                                      # Pedir al usuario la palabra

palbra_limpia = i.replace(' ', '').upper()                              # Quitar los espacios y convertilo a mayúsculas
dupe = set(palbra_limpia)                                               # Quitar las letras duplicadas
ordenado = sorted(dupe)                                                 # Ordenarlo en orden descendiente

print(''.join(ordenado))                                                # Unir todo e imprimir el resultado