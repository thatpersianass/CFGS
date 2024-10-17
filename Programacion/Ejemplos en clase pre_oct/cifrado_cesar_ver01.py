# cifrado de cesar

ALFABETO = "abcdefghijklmnñopqrstuvwxyz"
mensaje = input("Introduzca un mensaje: ")
clave = int(input("Introduzca la clave: "))
operacion = input("(C)ifrar o (D)escifrar: ").upper()
if operacion == "C":
    mje_cifrado = ''
    iteracion = 0
    while iteracion < len(mensaje):
        posicion = ALFABETO.find(mensaje[iteracion])
        nva_posicion = posicion + clave
        mje_cifrado += ALFABETO[nva_posicion % len(ALFABETO)]
        
elif operacion == "D":
    pass
else:
    print("Error...Opción inválida")