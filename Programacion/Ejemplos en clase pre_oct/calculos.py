# ejercicio 04

i = input("Escriba un valor entre 0 y 6: ")
try:
    digit = int(i)

except:
    print("Error...")

else:
    if digit < 6 or digit <0:
        print("Error... Numero fuera de rango")
    else:
        pass

finally:
    print("Saliendo....")