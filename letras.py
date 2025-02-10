

salir = True
while salir:
    cantletras = 0
    x = input("Ingrese una palabra para contabilizarla (Escribe 'escape' para salir) :")
    if x ==    "escape" :
        print("Saliendo...")
        salir = False
    else:
        for letras in x:
    
            cantletras += 1
        print(cantletras)























