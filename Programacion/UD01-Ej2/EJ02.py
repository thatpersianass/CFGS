    # Un número de N dígitos es un número de Armstrong si es igual a la suma de las nésimas potencias de sus dígitos. Por ejemplo, 371, 8208 y 4210818 son números de Armstrong ya que
    #  371 = 3^3 + 7^3 + 1^3 y
    #  8208 = 8^4 + 2^4 + 0^4 + 8^4
    #  4210818 = 4^7 + 2^7 + 1^7 + 0^7 + 8^7 + 1^7 + 8^7
    # Escriba un programa en Python que muestre los 20 primeros números de Armstrong

    # x = sum(i(digito) ** n for y in z)

numeros_armstrong = []                                          # Crea una lista vacía
num = 0                                                         # Se define el número que se va a convertir en número de Armstrong

while len(numeros_armstrong) < 20:                              # Contador para imprimir los 20 primeros números
    n = len(str(num))                                           # Calcula el número de dígitos del número actual
    suma = sum(int(d)**n for d in str(num))                     # Fórmula para calcular el siguiente número
    
    if num == suma:
        numeros_armstrong.append(num)                           # Añade el número actual al final de la lista
    
    num += 1                                                    # Después de verificar si num es un número de Armstrong, se incrementa num para probar el siguiente número en la siguiente iteración del bucle.

print(numeros_armstrong)
