# En este ejercicio se quiere realizar un programa de Python que implemente la variante del Código de César que se describe a continuación:

# Para este algoritmo de cifrado se necesita una clave numérica cuyo valor debe ser menor o igual que un tercio de la longitud del mensaje a encriptar y tener un valor
# que sea mayor a 3. Esto garantiza que el cifrado obtenido no sea tan fácil de descifrar.

# Una vez que se tiene el mensaje y la clave de cifrado se debe proceder de la siguiente forma. Lo veremos mejor con un ejemplo.


# Supongamos que el mensaje a cifrar es el siguiente:

# en un lugar de la mancha de cuyo nombre no quiero recordar

# Suponiendo que la clave de cifrado es el 5. El mensaje de encriptado se crea de la siguiente forma:

# Comenzamos a escribir los primeros 5 caracteres del mensaje en la primera línea, los segundos 5 caracteres en la segunda línea, el tercer bloque de 5 caracteres en
# la tercera línea y así sucesivamente hasta terminar con todos los caracteres del mensaje a cifrar. El número 5 es el correspondiente al valor de la clave.

# en un
#  luga
# r de
# la ma
# ncha

# Como resultado obtenemos el texto anterior con líneas de 5 caracteres cada una. El mensaje encriptado se obtiene leyendo por columnas el mensaje construido
# anteriormente.

# El resultado del encriptado es el siguiente: e rlnnl ac ud hugemana a

opt = input('Introduce una frase -->   ')

