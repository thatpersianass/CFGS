# Escriba un programa en Python que permita escribir por pantalla el siguiente
# patrón. Se lee como dato un número entero impar que representa el número de
# filas que contiene el patrón. El programa debe verificar que el número leído es
# impar y mayor o igual a 3.
# * * *
#   * *             n = 3
#  *  *

# * * * * *
#       * *
#     *   * n = 5
#   *     *
# *       *


# * * * * * * *
#           * *
#         *   *
#       *     * n = 7
#     *       *
#   *         *
# *           *

try:
    hell = int(input('Introduce un número -->   '))

except:
    print('Tiene que ser un numero entero')

else:
    if hell >= 3:
        for i in range(hell):                               # Se usará para imprimir asteriscos en toda la primera fila       
            for k in range(hell):                           # Se usará para imprimir asteriscos en toda la primera columna


                if i == 0 or k == 0 or i == k:              # La comparación 'i == k' sirve para dibujar la linea diagonal
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

    else: 
        print('Tiene que ser mayor que 3...')