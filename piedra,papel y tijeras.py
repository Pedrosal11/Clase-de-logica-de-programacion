
#PIEDRA, PAPEL O TIJERAS

import random
opciones=("papel", "piedra", "tijeras")

player = input("Elige papel, piedra o tijeras:")
maquina = random.choice (opciones)

print("maquina selecciono",maquina)

if maquina == player:
    print("empate")
elif (player== "piedra" and maquina== "tijeras") or \
    (player== "papel" and maquina== "piedra") or \
    (player)== ("tijeras" and maquina== "papel"):
    print("Ganaste")
else:
    print("Lo siento, perdiste")