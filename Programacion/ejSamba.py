# //ip/carpetas/x
# //nomvre_servidor/x/y

ruta = input("Escriba la ruta: ")

if ruta[0] == '/' and ruta[1] == '/':
    desglose = ruta[2:].partition('/')
    print(f"Nombre equipo IP: {desglose[0]}")
    print(f"Ruta compartida: {desglose[2]}")

else:
    print("Error, la ruta es inválida...")