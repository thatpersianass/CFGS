import random  # Importar la librería random para generar números aleatorios

# Lista extendida de campeones y emparejamientos con Malphite
campeones = {
    "Aatrox": "le gana a Malphite",
    "Jax": "le gana a Malphite",
    "Nasus": "le gana a Malphite",
    "Teemo": "le gana a Malphite",
    "Ryze": "pierde contra Malphite",
    "Sion": "pierde contra Malphite",
    "Ziggs": "pierde contra Malphite",
    "Yasuo": "le gana a Malphite",
    "Garen": "le gana a Malphite",
    "Ashe": "pierde contra Malphite",
    "Lux": "pierde contra Malphite",
    "Zed": "le gana a Malphite",
    "Darius": "le gana a Malphite",
    "Vayne": "pierde contra Malphite",
    "Ahri": "pierde contra Malphite",
    "Caitlyn": "le gana a Malphite",
    "Ezreal": "le gana a Malphite",
    "Syndra": "pierde contra Malphite",
    "Katarina": "le gana a Malphite",
    "Karthus": "pierde contra Malphite",
    "Fiora": "le gana a Malphite",
    "Riven": "le gana a Malphite",
    "Morgana": "pierde contra Malphite",
    "Jhin": "pierde contra Malphite",
    "Draven": "le gana a Malphite",
    "Miss Fortune": "le gana a Malphite",
    # Agregar aquí más campeones si es necesario
}

# Definir las cargas necesarias para cada campeón
cargas_necesarias = {
    "Zed": 10,
    "Yasuo": 15,
    "Ryze": 5,
    "Sion": 5,
    "Ziggs": 5,
    "Garen": 10,
    "Darius": 10,
    "Vayne": 5,
    "Ahri": 5,
    "Caitlyn": 10,
    "Ezreal": 10,
    "Syndra": 5,
    "Katarina": 10,
    "Karthus": 5,
    "Fiora": 10,
    "Riven": 10,
    "Morgana": 5,
    "Jhin": 5,
    "Draven": 10,
    "Miss Fortune": 10,
    # Agregar aquí más campeones si es necesario
}

# Listas de campeones según el resultado contra Malphite
pierde_contra_malphite = [campeon for campeon, resultado in campeones.items() if resultado == "pierde contra Malphite"]
gana_contra_malphite = [campeon for campeon, resultado in campeones.items() if resultado == "le gana a Malphite"]

rock_solid = "Tlinkn't!" # Tiene Heartsteel?
fumo = 1 # Contador de bucle
action = 0 # Input del usuario
money = 0  # Inicializar money en 0
kills = 0  # Contador de asesinatos
cargas_heartsteel = 0  # Contador de cargas de Heartsteel
muertes = 0  # Contador de muertes

# Códigos ANSI para colores
amarillo = "\033[93m"
rojo = "\033[91m"
verde = "\033[92m"
reset_color = "\033[0m"

def mensaje_kill(count, campeon, cargas_ganadas):
    if count == 1:
        return f"{verde}You have slain {amarillo}{campeon}{reset_color}! +{cargas_ganadas} Heartsteel charges. Total: {cargas_heartsteel}."
    elif count == 2:
        return f"{verde}Double kill! {amarillo}{campeon}{reset_color}! +{cargas_ganadas} Heartsteel charges. Total: {cargas_heartsteel}."
    elif count == 3:
        return f"{verde}Triple kill! {amarillo}{campeon}{reset_color}! +{cargas_ganadas} Heartsteel charges. Total: {cargas_heartsteel}."
    elif count == 4:
        return f"{verde}Quadra kill! {amarillo}{campeon}{reset_color}! +{cargas_ganadas} Heartsteel charges. Total: {cargas_heartsteel}."
    elif count >= 5:
        return f"{verde}Penta kill! {amarillo}{campeon}{reset_color}! +{cargas_ganadas} Heartsteel charges. Total: {cargas_heartsteel}."
    return ""

def obtener_heartsteel():
    global rock_solid, cargas_heartsteel
    rock_solid = "Tlink!"
    cargas_heartsteel = 0  # Reiniciar las cargas para que comiences desde cero
    print(f"{verde}You have received Heartsteel with the secret code!{reset_color} {rojo}You are a cheater!{reset_color}")

def tienda():
    global rock_solid, money
    print("\n--- Store ---")
    print("1. Heartsteel - 3200 Money")
    print("0. Exit the shop")
    eleccion = input("Choose an item to buy: ")

    if eleccion == "1":
        if money >= 3200:
            rock_solid = "Tlink!"
            money -= 3200
            print(f"{verde}You bought Heartsteel!{reset_color}")
        else:
            print(f"{rojo}You don't have enough money!{reset_color}")
    elif eleccion == "0":
        print("Leaving the store.")
    else:
        print(f"{rojo}Invalid choice. Please enter '1' to buy or '0' to exit.{reset_color}")

def terminar_partida(mensaje):
    global fumo
    fumo = 0
    print(mensaje)

while fumo == 1:
    action = input("What do you want to do? (W: Fight, Q: Collect money, T: Store, C: Code) ").upper()
    
    if action == "C":
        codigo = input("Enter the secret code: ")
        if codigo == "NOKIA":
            obtener_heartsteel()
        else:
            print(f"{rojo}Invalid code.{reset_color}")
    
    elif action == "W":
        if rock_solid == "Tlink!":
            # Elegir 5 campeones al azar de la lista
            campeones_elegibles = random.sample(list(campeones.keys()), 5)
            
            print("Choose a champion to attack from the following list:")
            for i, campeon in enumerate(campeones_elegibles, 1):
                print(f"{i}. {amarillo}{campeon}{reset_color}")
            
            try:
                eleccion = int(input("Enter the number of your choice: "))
                if 1 <= eleccion <= 5:
                    campeon_elegido = campeones_elegibles[eleccion - 1]
                    
                    # Determinar si puedes atacar al campeón
                    if campeones[campeon_elegido] == "le gana a Malphite":
                        # Si el campeón gana a Malphite, verifica si tienes suficientes cargas
                        if rock_solid == "Tlink!" and cargas_heartsteel >= cargas_necesarias.get(campeon_elegido, 20):
                            kills += 1
                            cargas_ganadas = 2  # Cada asesinato da 2 cargas
                            cargas_heartsteel += cargas_ganadas  # Incrementar las cargas de Heartsteel
                            print(mensaje_kill(kills, campeon_elegido, cargas_ganadas))  # Mostrar el mensaje correspondiente
                            
                            # Verificar si ganaste
                            if cargas_heartsteel >= 30:
                                terminar_partida(f"{verde}Congratulations! You've reached 30 Heartsteel charges and won the game!{reset_color}")
                        elif rock_solid == "Tlink!":
                            print(f"{rojo}You have been slain by {amarillo}{campeon_elegido}{reset_color}!")
                            print(f"{rojo}You have {cargas_heartsteel} Heartsteel charges. {cargas_necesarias.get(campeon_elegido, 20)} needed to kill this champion.{reset_color}")
                            muertes += 1
                            if muertes >= 10:
                                terminar_partida(f"{rojo}You have died 10 times. Game over!{reset_color}")
                        else:
                            # Si no tienes Heartsteel, no puedes matar a campeones que ganan a Malphite
                            print(f"{rojo}You cannot slay {amarillo}{campeon_elegido}{reset_color} without Heartsteel.")
                            muertes += 1
                            if muertes >= 10:
                                terminar_partida(f"{rojo}You have died 10 times. Game over!{reset_color}")
                    else:
                        # Si el campeón no gana a Malphite
                        print(f"{verde}You have slain {amarillo}{campeon_elegido}{reset_color}! +2 Heartsteel charges. Total: {cargas_heartsteel}.")
                        kills += 1
                        cargas_ganadas = 2  # Cada asesinato da 2 cargas
                        cargas_heartsteel += cargas_ganadas  # Incrementar las cargas de Heartsteel
                        
                        # Verificar si ganaste
                        if cargas_heartsteel >= 30:
                            terminar_partida(f"{verde}Congratulations! You destroyed the Nexus!{reset_color}")
                else:
                    print(f"{rojo}Invalid choice. Please choose a number between 1 and 5.{reset_color}")
            except ValueError:
                print(f"{rojo}Invalid input. Please enter a number.{reset_color}")
        else:
            print(f"{rojo}You need Heartsteel to fight!{reset_color}")

    elif action == "Q":
        money += 100  # Sumar 100 a money
        print(f"+100 Money: {money}")
        
        # 5% de probabilidad de ser cegado por Teemo
        if random.randint(1, 100) <= 5:
            money -= 200
            print(f"{rojo}Teemo blinded you and stole 200 money!{reset_color}")
        
    elif action == "T":
        tienda()

    else:
        print(f"{rojo}Invalid action. Please enter 'W', 'Q', 'T', or 'C'.{reset_color}")
