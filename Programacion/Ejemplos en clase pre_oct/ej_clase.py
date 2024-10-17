# Una palabra se considera creciente si sus letras van de manera creciente

# alfabeto = 'abcdefghijklmnñopqrstuvwxyz'

                    # char = input('Introduzca una palabra:  ').lower()
                    # ant = char[0]

                    # for letra in char:
                    #     if letra < ant:
                    #         print('Decreciente')
                    #         break

                    #     ant = letra

                    # else:
                    #     print("Creciente")

#  UNA CONTRASEÑA SE CONSIDERA SEGURA SI CUMPLE CON LAS SIGUIENTES CONDICIONES: TIENE UNA LETRA MATÚSCULA, AL MENOS UNA LETRA MINÚSCULA, AL MENOS UN DIGITO, 1 CARACTER ESPECIAL DE'@,#,%,[,],{,}...
#  ESCRIBIR UN PROGRAMA QUE LEA UNA CONTRASEÑA Y DIGA SI ES SEGURA....

minus = 'abcdefghijklmnopqrstuvwxyz'
mayus = minus.upper()
digit = '0123456789'
simbol = '!"#$%&*,@[]()~'

hay_min = False
hay_may = False
hay_dig = False
hay_sim = False

i = input('Introduzca una contraseña:  ')

if len(i) >= 8:
    for letra in i:
        if letra in minus:
            hay_min = True
            continue
        if letra in mayus:
            hay_may = True
            continue
        if letra in digit:
            hay_dig = True
            continue
        if letra in simbol:
            hay_sim = True
            continue

    if hay_min and hay_may and hay_dig and hay_sim:
        print('Contraseña segura')
    else:
        print('Contraseña NO segura')
else:
    print('Debe contener más de 8 caracteres...')