from colorama import Fore

def menu_categorias():
    categorias = ["Ciencia", "Historia", "Entretenimiento"]

    print(f"{Fore.MAGENTA}Seleccioná una categoría:\n")
    for i, categoria in enumerate(categorias, 1):
        print(f"{Fore.CYAN}{i}. {categoria}")

    while True:
        opcion = input(f"\n{Fore.YELLOW}Ingresá el número de la categoría: ")
        if opcion.isdigit() and 1 <= int(opcion) <= len(categorias):
            seleccion = categorias[int(opcion) - 1]
            print(f"{Fore.GREEN}\nHas elegido la categoría: {seleccion}\n")
            return seleccion
        else:
            print(f"{Fore.RED}Opción inválida. Por favor, ingresá un número válido.")
