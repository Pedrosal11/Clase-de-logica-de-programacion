import random
# Opciones disponibles
opciones = ("piedra", "papel", "tijeras")

# Puntos de jugador y máquina
puntos_jugador = 0
puntos_maquina = 0

print("¡Bienvenido al juego Piedra, Papel o Tijeras!")
print("Primero en ganar 3 rondas es el campeón.")

while puntos_jugador < 3 and puntos_maquina < 3:
    jugador = input("Elige piedra, papel o tijeras: ").lower()

    # Validación de entrada
    if jugador not in opciones:
        print("Opción inválida. Intenta de nuevo.")
        continue

    maquina = random.choice(opciones)
    print(f"La máquina eligió: {maquina}")

    # Lógica del juego
    if jugador == maquina:
        print("Empate.")
    elif (jugador == "piedra" and maquina == "tijeras") or \
         (jugador == "papel" and maquina == "piedra") or \
         (jugador == "tijeras" and maquina == "papel"):
        print("¡Ganaste esta ronda!")
        puntos_jugador += 1
    else:
        print("Perdiste esta ronda.")
        puntos_maquina += 1

    # Mostrar marcador
    print(f"Puntos -> Tú: {puntos_jugador} | Máquina: {puntos_maquina}")
    print("-" * 40)

# Resultado final
if puntos_jugador == 3:
    print(" ¡Felicidades! Ganaste el juego.")
else:
    print("La máquina ganó el juego. ¡Suerte la próxima vez!")

