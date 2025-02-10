import math


salir = True
while salir:
    x = float(input("Ingrese un radio para calcular su area (Escribe 'escape' para salir) :"))
    if x ==    "escape" :
        print("Saliendo...")
        salir = False
    else:
        area = math.pi * (x**2)
    print("El area del circulo con radio", x, "es", area)




















