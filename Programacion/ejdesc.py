# polizas = lista de diccionarios
#     nro polizas
#     DNI tomador
#     Matricula
#     DatosVehiculo=(Tipo,marca,modelo,etc)
#     Cobertura(RC,RL,RB,INC,TR)
#     Estado = (Cobrado,Pendiente cobro, Baja)
#     Fecha emision
#     Forma de pago

# fichero = open('dir_trab/fichero01.txt')
# print(f'El fichero ha sido abierto en modo: {fichero.mode}')
# fichero.close()

try:
    fichero = open('dir_trab/fichero02.txt','r')
    textoaux = fichero.readlines()
    for linea in textoaux[:-1]:
        print(linea[:-1])
    print(textoaux[-1])
except:
    print('Error al abrir el fichero')

else:
    print('Fin de la ejecicion')