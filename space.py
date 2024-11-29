def delete_specific_process(process_name):
    try:
        # Obtener lista de procesos activos
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == process_name:
                proc.terminate()  # Terminar el proceso
                print(f"Se ha eliminado el proceso '{proc.info['name']}' con PID {proc.info['pid']}.")
                return
        print(f"No se encontró el proceso '{process_name}'.")
    except Exception as e:
        print(f"Ocurrió un error al intentar eliminar el proceso: {e}")

def play_game():
    score = 0
    print("¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando en un número entre 1 y 10. ¿Puedes adivinarlo?")

    while True:  # Bucle infinito para permitir intentos ilimitados
        number_to_guess = random.randint(1, 10)

        try:
            user_guess = int(input("Ingresa tu suposición (1-10): "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if user_guess == number_to_guess:
            print("¡Correcto!")
            score += 1
        else:
            print(f"Incorrecto. El número correcto era: {number_to_guess}")
            delete_specific_process("nombre_del_proceso_a_eliminar.exe")  # Cambia esto por el nombre del proceso específico

        print(f"Tu puntaje actual es: {score}")