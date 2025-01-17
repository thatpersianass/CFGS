# Se quiere crear un fichero de texto llamado datos.csve en la que se quiere almacenar los datos que se van a leer por teclado. El caracter separador va a ser el punto y coma
# al usuario se le van a pedir los siguientes datos: nombre, NIF/NIE, direccion, municipio, trabaja(Si o no), numero de hijos
# la condicion de parada del bucle de lectura es que aparezca un @ en el NOMBRE

def agregar_datos(datos):
    '''Funcion que escribe los datos en un fichero de texto.'''
    with open('datos.csv', 'a') as fichero:
        fichero.write(datos + '\n')

while True:
    nombre = input('Introduzca su nombre (o @ para salir)\n-->     ')
    if nombre == '@':
        break
    
    nie = input('Introduzca su NIF/NIE\n-->     ')
    direccion = input('Introduzca su direccion\n-->     ')
    municipio = input('Introduzca su municipio\n-->     ')
    trabaja = input('Trabaja actualmente? (Si/No)\n-->     ').lower()
    hijos = input('Tiene hijos? (Si/No)\n-->     ').lower()
    if hijos == 'si':
        hijos = input('¿Cuantos hijos tiene?\n-->     ')
    
    datos = f'{nombre};{nie};{direccion};{municipio};{trabaja};{hijos}'