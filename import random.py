
import random

numero_secreto = random.randint(0, 100)
adivinado = False
intentos = 0
intentosmax = 15
puntos = 0
puntosganados = 20
puntosperdidos = -10

print("Bienvenido al Juego del Número Secreto")

while not adivinado and intentos < intentosmax:
    numero = int(input("Introduce un número del 1 al 99: "))
    
    if numero == numero_secreto:
        puntos += puntosganados
        print("¡Felicidades! Has adivinado el número secreto y ganas {puntosganados} puntos.")
        adivinado = True
    else:
        puntos -= puntosperdidos
        if intentos < intentosmax - 1:
            if numero < numero_secreto:
                print("El número es mayor al ingresado.")
            else:
                print("El número es menor al ingresado.")
    
    intentos += 1

if not adivinado:
    print("Perdiste, el número era", numero_secreto)
else:
    print("Tu puntuacion final es", puntos)
