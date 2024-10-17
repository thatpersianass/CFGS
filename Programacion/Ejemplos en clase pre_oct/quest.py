# Crear un código que solicite el Nombre y Apellido, seguidamente, invierta el orden de estos, separandolos por una coma.

            # nom = input("Indique su nombre:  ")
            # ape = input("Indique su apellido:  ")

            # print(f"{ape}, {nom}")

# Crear un código que solicite el Nombre y Apellido, seguidamente, invierta el orden de estos, separandolos por una coma (CON SOLO UN INPUT).

                                        # i = int(input("Cuantos nombre tienes?:  "))
                                        # nom = i - 1

                                        # i = int(input("Cuantos apellidos tienes?:  "))
                                        # ape = i

                                        # i = input("Introduce tu nombre completo:  ")


                                        # print(f"{i.split()[ape]}, {i.split()[nom]}")


ape = int(input("¿Cuántos apellidos tienes?(Cuentan palabras como DE o LA):  "))
nom = input("Introduce tu nombre completo:  ")
i = nom.split()

print(f"{' '.join(i[-ape:])}, {' '.join(i[:-ape])}")
