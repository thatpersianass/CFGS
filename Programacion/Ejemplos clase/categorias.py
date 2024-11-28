# Diccionario donde las claves son categorías y los valores son listas de elementos. Devuelve un nuevo diccionario donde las claves son los elementos
# y los valores son conjuntos con las categorías a las que pertenecen

# La salida debe ser:
# {
#  "Camisa": {"Ropa"},
#  "Pantalón": {"Ropa", "Electrónica"},
#  "Zapatos": {"Ropa", "Hogar"},
#  "Laptop": {"Electrónica"},
#  "Teléfono": {"Electrónica"},
#  "Silla": {"Hogar"},
#  "Mesa": {"Hogar"}
# }

categorias = {
    "Ropa": ["Camisa", "Pantalón", "Zapatos"],
    "Electrónica": ["Laptop", "Teléfono", "Pantalón"],
    "Hogar": ["Silla", "Mesa", "Zapatos"]
}

dick = {}

for clave, valor, in categorias.items():
    for valores in valor:
        if valores not in dick:
            dick[valores] = set()
        dick[valores].add(clave)
    
for elto in dick:
    print(f'{elto}:{dick[elto]}')