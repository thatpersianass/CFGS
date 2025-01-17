def leer_archivo(i):
    try:
        fichero = open(i,'r')
    except FileNotFoundError:
        print('El fichero no existe')
        return None
    else:
        texto = fichero.read()
        return texto

if __name__ == "__main__":
    while True:
        opt = input('¿Desea buscar palabras completas o parciales? \n (1)Completas\n (2)Parciales\n (0)Salir\n-->    ')
        if opt != '0':
            nombre_archivo = input('Inserte el nombre y la ruta del archivo\n-->   ')

        elif opt == '1':
            palabra = input('Inserte la palabra a buscar\n-->   ')
            texto = leer_archivo(nombre_archivo)
            if palabra in texto:
                print(f'La palabra "{palabra}" se encuentra en el archivo.\n')
            else:
                print(f'La palabra "{palabra}" no se encuentra en el archivo.\n')
    
        elif opt == '2':
            pass
        
        elif opt == '0':
            print('Saliendo...')
            break