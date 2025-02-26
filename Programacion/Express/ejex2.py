# Se define una clase llamada Lista, la cual contiene como atributo una lista de números enteros.

# Métodos de la clase:
# - insertarFinalLista(num): Inserta el número 'num' al final de la lista.
# - insertarComienzoLista(num): Inserta el número 'num' al comienzo de la lista.
# - sacarFinalLista(): Retorna el último valor de la lista si existe, en caso contrario retorna False.
# - sacarInicioLista(): Retorna el primer valor de la lista si existe, en caso contrario retorna False.
# - vaciarLista(): Elimina todos los elementos de la lista.
# - compararListas(): Redefine el método __eq__ para comparar si dos listas son iguales.
#   Dos listas son consideradas iguales si tienen la misma longitud y contienen los mismos elementos,
#   sin importar el orden.

# Métodos mágicos redefinidos para operaciones matemáticas:
# - Suma (__add__): Suma un número 'num' a todos los elementos de la lista.
# - Resta (__sub__): Resta un número 'num' a todos los elementos de la lista.
# - Multiplicación (__mul__): Multiplica un número 'num' a todos los elementos de la lista.
# - División entera (__floordiv__): Divide cada elemento de la lista por 'num' mediante división entera.

# Programa principal:
# - Crear varios objetos de la clase Lista.
# - Probar todos los métodos definidos en la clase.

# Colores
error = "\033[38;5;196m"
gud = "\033[32m"
reset_color = "\033[0m"

#   Clase lista
class Lista:
    # Se define la lista vacía
    def __init__(self):
        self.lista = []
    
    # Devuelve la lista en forma de String para que los colores se apliquen correctamente
    def __str__(self):
        return str(self.lista)
    
    # Insertar al final de la lista
    def insertarFinalLista(self,num):
        self.lista.append(num)

    # Insertar al inicio de la lista
    def insertarComienzoLista(self,num):
        self.lista.insert(0, num)
    
    # Devolver el último caracter de la lista
    def sacarFinalLista(self):
        if self.lista:
            return self.lista[0]
        return False
    
    # Devolver el primer caracter de la lista
    def sacarComienzoLista(self):
        if self.lista:
            return self.lista[-1]
    
    # Se explica solo, vacía la lista
    def vaciarLista(self):
        self.lista.clear()
    
    # Función para los métodos mágicos, verificar si el valor introducido es un entero
    def verificarInt(self, num):
        if isinstance(num, int):
            return True
        return False

    # Sumar
    def __add__(self,num):
        nueva_lista = Lista()
        if self.verificarInt(num):
            nueva_lista.lista = [x + num for x in self.lista]
            return nueva_lista
        print( error + f'El valor {num} no es un número entero.' + reset_color)
        return nueva_lista
    
    # Restar
    def __sub__(self,num):
        nueva_lista = Lista()
        if self.verificarInt(num):
            nueva_lista.lista = [x - num for x in self.lista]
            return nueva_lista
        print( error + f'El valor {num} no es un número entero.' + reset_color)
        return nueva_lista
    
    # Multiplicar
    def __mul__(self,num):
        nueva_lista = Lista()
        if self.verificarInt(num):
            nueva_lista.lista = [x * num for x in self.lista]
            return nueva_lista
        print( error + f'El valor {num} no es un número entero.' + reset_color)
        return nueva_lista

    # División
    def __floordiv__(self,num):
        nueva_lista = Lista()
        if self.verificarInt(num):
            nueva_lista.lista = [x // num for x in self.lista]
            return nueva_lista
        print( error + f'El valor {num} no es un número entero.' + reset_color)
        return nueva_lista
    
    # Comparación
    def __eq__(self, otra_lista):
        return sorted(self.lista) == sorted(otra_lista.lista)

# Ejecución de los métodos de la clase
if __name__ == "__main__":
    # Se crean dos listas, que estarán vacías
    lista1 = Lista()
    lista2 = Lista()
    
    # Se insertan datos en las listas
    lista1.insertarFinalLista(5)
    lista1.insertarFinalLista(10)
    lista1.insertarComienzoLista(3)

    lista2.insertarFinalLista(10)
    lista2.insertarComienzoLista(3)
    lista2.insertarFinalLista(5)
    
    # Se imprimen las listas con sus datos
    print("\nLista 1: " + gud + str(lista1) + reset_color)
    print("Lista 2: " + gud + str(lista2) + reset_color)
    
    # Verificación para comprobar si las listas son iguales
    if lista1 == lista2:
        print(gud + "\nLas listas son iguales.\n" + reset_color)
    else:
        print(error + "\nLas listas no son iguales.\n" + reset_color)
    
    # Operaciones, dos son correctas y dos retornan ValueError
    lista3 = lista1 + "a"
    lista4 = lista1 - 2
    lista5 = lista1 * "H"
    lista6 = lista1 // 2
    
    print("\nSuma de 2 a cada elemento de lista1: " + gud + str(lista3.lista) + reset_color)
    print("Resta de 2 a cada elemento de lista1: "+ gud + str(lista4.lista) + reset_color)
    print("Multiplicación de lista1 por 2: " + gud + str(lista5.lista) + reset_color)
    print("División entera de lista1 por 2: " + gud + str(lista6.lista) + reset_color)
    
    # Sacar los datos especificados de la lista
    print("\nElemento al inicio de lista1: " + gud + str(lista1.sacarComienzoLista()) + reset_color)
    print("Elemento al final de lista1: "+ gud + str(lista1.sacarFinalLista()) + reset_color)
    
    # Vaciar la lista
    lista1.vaciarLista()
    print(gud + "\nLista 1 vaciada correctamente.\n" +  reset_color)
