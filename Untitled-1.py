# Diccionario para almacenar el estado de los productos
productos = {
    "manzana": 0,
    "banana": 0,
    "tomate": 0
}

servicio_on = True

while servicio_on:
    x = input("Disponibilidad (o 'salir' para terminar): ").strip().lower()

    # Opción para salir del programa
    if x == "salir":
        print("\nCerrando el sistema de disponibilidad...")
        break  # Sale del while

    # Verificar si el usuario ingresó disponibilidad o no disponibilidad
    palabras = x.split()  # Divide la entrada en palabras
    if len(palabras) == 2:  # Deben ser dos palabras (ej: "manzana disponible")
        producto, estado = palabras  # Separa en "manzana" y "disponible"

        if producto in productos:  # Verifica si el producto es válido
            if estado == "disponible":
                productos[producto] = 1
            elif estado == "no":
                productos[producto] = 0

    # Mostrar estado actualizado
    print("\n📌 Estado actual de los productos:")
    for producto, estado in productos.items():
        print(f"🍏 {producto.capitalize()}: {'✅ Disponible' if estado == 1 else '❌ No disponible'}")
    print()  # Espacio para mayor claridad
