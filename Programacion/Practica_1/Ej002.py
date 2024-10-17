# Un número está posicionalmente bien estructurado, si ocurre que:

# 1. Las posiciones impares las ocupan dígitos impares
# 2. Las posiciones pares las ocupan dígitos pares
# 3. En cualquier otro situación el número NO ESTÁ posicionalmente bien estructurado.

# Tenga en cuenta que las posiciones se miran de derecha a izquierda y que el primer dígito corresponde a posición impar.

try:
    opt = int(input('Ingresa un numero ---->   '))

except:
    print('Ingrese un número entero...')

else:
    def es_valido(opt):                                                             # Funcion def, para devolver un valor booleano (no se usó una declaraciónd de variable para practicar el def)
        string_opt = str(opt)                                                       # Convertir el numero introducido por el usuario en un string, ya que los enteros no se pueden revertir

        for i,digito in enumerate(reversed(string_opt), start = 1):                 # Este bucle recorre los dígitos de la cadena numero_str en orden inverso (de derecha a izquierda), asignando a i la posición (comenzando desde 1) y a digito el valor correspondiente de cada dígito.
            digito = int(digito)                                                    # Convertir digito en un entero

            if i % 2 != 0 and digito % 2 == 0:                                      # Verificar la posición impar (posiciones 1, 3, 5, ...) debe tener dígito impar
                return False
    
            if i % 2 == 0 and digito % 2 != 0:                                      # Verificar la posición par (posiciones 2, 4, 6, ...) debe tener dígito par
                return False
        
        return True                                                                 # Si pasa todas las verificaciones, el número está bien estructurado
    
    if es_valido(opt):
        print(f'El número {opt} es un número válido')
    
    else:
        print(f'El número {opt} NO es un número válido')