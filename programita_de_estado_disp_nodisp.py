
def estados(numero):
    return "Disponible" if numero > 10 else "No disponible"

while True:
    numero = int(input("Ingrese un numero (-1 para salir): "))
    if numero == -1:
        print("Saliendo del programa")
        break
    print("Estado:",estados(numero))