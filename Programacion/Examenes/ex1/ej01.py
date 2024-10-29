# Escribir un programa que lea un string en pantalla que represente la dirección de un correo electrónico y diga si es válida o no. Lo que se pide es que se revise el
# formato.

# Una dirección de correo debe tener el siguiente formato:

# aaaaaaaaaaaaaaaa@aaaaaaaaa.aaaa

# Es decir, antes del arroba debe existir al menos dos caracteres y un máximo de 16 y no debe empezar por número, a continuación el carácter ‘@‘, seguido de
# cualquier número de caracteres o dígitos, (que no comienza por dígito), para finalizar debe estar el ‘.’ seguido de al menos 2 y hasta 4 caracteres, ninguno de
# los cuales puede ser un dígito.

opt = input('Introduce tu correo electrónico -->   ')

parte1 = opt.split('@')
parte2 = parte1[1].split('.')

arroba = False
punto = False
con1 = True
con2 = True
cond3 = True

# print(parte1)
# print(parte2)

if len(parte1[0]) <= 16 and len(parte1[0]) >= 2 and len(parte2[1]) <= 4 and len(parte2[1]) >= 2: # Verifica si cada uno tiene sus respectivos caracteres minimos y maximos
    if opt[0].isdigit():                                                    # Va verificando si cada uno de los campos del correo empiezan por numero
        print('El correo no puede empezar un número...')
        con1 = False

    
    if parte1[1][0].isdigit():
        print('El dominio no puede empezar un número...')
        con2 = False

    if parte2[1][0].isdigit():
        cond3 = False

    else:
        for i in opt:
            if i == '@':                            # Verifica si tiene @
                arroba = True
                
            if i == '.':                            # Verifica si tiene .
                punto = True


if arroba and punto and con1 and con2:
    print('Correo Válido')

else:
    print('Correo Inválido...')