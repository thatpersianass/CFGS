# Se sabe que al lanzar dos dados normales (valores de 1 al 6) se pueden tener valores de suma obtenida que van
# desde el 2 hasta el 12.

# Se pide que diseñe un programa en Python con las dos funciones siguientes:

# calculo_combinaciones()

# esta función se encarga de calcular el número de maneras distintas en obtener cada uno de los valores de la suma
# de los dos dados.

# Por ejemplo, el valor 2, sólo se obtiene de sacar 1 en los dos dados, el valor 4 se puede obtener de 3 maneras
# distintas:

# Dado1: 1 Dado2: 3,
# Dado1: 2 Dado2: 2,
# Dado1: 3 Dado2: 1.

# Esta función debe retornar un diccionario donde la clave representa la suma de los puntos de los dos dados (2 al
# 12) y el valor el número de maneras distintas en que se puede obtener esa puntuación.

combinaciones = {}

def calculo_combinaciones( dic_nro_veces: dict ) -> dict:
    nro_total_casos = sum(dic_nro_veces.values())
    dict_prob = {}
    for clave,valor in dic_nro_veces.items():
        dict_prob[clave] = 0
        
    for dado1 in range(1,7):
        for dado2 in range (1,7):
            dict_prob[dado1+dado2] += 1

    return dict_prob

if __name__ == '__main__':
    dict_posibilidades = calculo_combinaciones()
    
    print(dict_posibilidades)