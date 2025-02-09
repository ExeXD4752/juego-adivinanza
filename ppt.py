while True:
    nombre1 = input("Elige el nombre de tu personaje: ")
    nombre2 = input("Elige el nombre de tu personaje: ")

    jugador1 = input("Hola " + nombre1 + ", ¿qué eliges? Piedra, Papel o Tijeras: ")
    jugador2 = input("Hola " + nombre2 + ", ¿qué eliges? Piedra, Papel o Tijeras: ")

    condicion1  = jugador1 == "piedra" and jugador2 == "tijeras"
    condicion2  = jugador1 == "papel" and jugador2 == "piedra"
    condicion3  = jugador1 == "tijeras" and jugador2 == "papel"

    if jugador1 == jugador2:
        print("Empate")
    elif condicion1 or condicion2 or condicion3:
        print("Ha ganado", nombre1)
    else:
        print("Ha ganado", nombre2)

    jugar_de_nuevo = input("¿Quieres jugar otra vez? (si/no): ").lower()
    if jugar_de_nuevo != "si":
        print("Gracias por jugar. ¡Hasta la próxima!")
        break





