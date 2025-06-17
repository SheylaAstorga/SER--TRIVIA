from colorama import Fore

# Esta función muestra al usuario las categorías disponibles y le permite elegir una
def menu_categorias():
    # Lista de categorías disponibles en el juego
    categorias = ["Ciencia", "Historia", "Entretenimiento"]

    # Muestra el título del menú de categorías en color magenta
    print(f"{Fore.MAGENTA}Seleccioná una categoría:\n")

    # Recorre e imprime cada categoría con su número correspondiente
    for i, categoria in enumerate(categorias, 1):
        print(f"{Fore.CYAN}{i}. {categoria}")

    # Bucle que se repite hasta que el usuario elige una opción válida
    while True:
        # Pide al usuario que ingrese el número de la categoría
        opcion = input(f"\n{Fore.YELLOW}Ingresá el número de la categoría: ")

        # Verifica que la entrada sea un número válido y dentro del rango de la lista
        if opcion.isdigit() and 1 <= int(opcion) <= len(categorias):
            seleccion = categorias[int(opcion) - 1]  # Traduce el número a la categoría correspondiente
            print(f"{Fore.GREEN}\nHas elegido la categoría: {seleccion}\n")  # Confirma la selección
            return seleccion  # Devuelve la categoría elegida al programa principal
        else:
            # Mensaje de error si la opción es inválida
            print(f"{Fore.RED}Opción inválida. Por favor, ingresá un número válido.")