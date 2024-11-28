# Dicccionario que contiene autores y palabras utilizadas en sus textos

# Identifique las palabras que son únicas para cada autor.
# Las palabras compartidas entre los autores

# La respuesta es:

# Palabras únicas por autor:

# Autor1: {'programar'}
# Autor2: {'software'}
# Autor3: {'algoritmos'}

# Palabras compartidas por todos: {'Python'}

textos = {
    "Autor1": {"Python", "programar", "avanzado", "diseño"},
    "Autor2": {"Python", "diseño", "software", "ingeniería"},
    "Autor3": {"Python", "ingeniería", "algoritmos", "avanzado"}
}

dif01 = textos["Autor1"].difference(textos["Autor2"]).difference(textos["Autor3"])

dif02 = textos["Autor2"].difference(textos["Autor3"]).difference(textos["Autor1"])

dif03 = textos["Autor3"].difference(textos["Autor1"]).difference(textos["Autor2"])

comun = textos["Autor1"].symmetric_difference(textos["Autor2"]).symmetric_difference(textos["Autor3"])

print(f"Autor1: {dif01}")
print(f"Autor2: {dif02}")
print(f"Autor3: {dif03}")

print(f'Palabra compartida por todos:{comun}')