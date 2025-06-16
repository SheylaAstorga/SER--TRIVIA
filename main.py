import time
from colorama import init, Fore, Style
from menu import menu_categorias
from juego import jugar

import os

init(autoreset=True)

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def portada(nombre_usuario=None):
    limpiar_pantalla()

    titulo = f"""
{Fore.CYAN}{Style.BRIGHT}

                            ███████╗███████╗██████╗  █████╗ ██████╗ 
                            ██╔════╝██╔════╝██╔══██╗██╔══██╗╚════██╗
                            ███████╗█████╗  ██████╔╝███████║  ▄███╔╝
                            ╚════██║██╔══╝  ██╔══██╗██╔══██║  ▀▀══╝ 
                            ███████║███████╗██║  ██║██║  ██║  ██╗   
                            ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═╝   
                                        
    """

    subtitulo = f"{Fore.YELLOW}{Style.BRIGHT}\n\n  ¡Poné a prueba tu conocimiento en este juego de preguntas al estilo Preguntados!\n"
    bienvenida = f"{Fore.GREEN}\n  Cargando..."
    
    print(titulo)
    if nombre_usuario:
        print(f"{Fore.MAGENTA}  Bienvenid@, {nombre_usuario}!\n")
    time.sleep(1.5)
    print(subtitulo)
    time.sleep(1)
    print(bienvenida)
    time.sleep(2)

    print(f"\n{Fore.MAGENTA}  Categorías: Ciencia | Historia | Entretenimiento")
    print(f"{Fore.CYAN}  Dificultad: Fácil / Difícil\n")
    print(f"{Fore.YELLOW}  🎮 ¡Preparate para demostrar cuánto sabés!\n")
    input(f"{Fore.LIGHTWHITE_EX}  Presioná Enter para comenzar...")
    print()
    limpiar_pantalla()

def login():
    contraseña_correcta = "123456"
    intentos = 3

    while intentos > 0:
        print(f"{Fore.YELLOW}BIENVENIDO A ¿SERÁ? ")
        print(f"{Fore.CYAN}🔐 Iniciá sesión para jugar")
        nombre_usuario = input("👤 Ingresá tu nombre: ")
        contraseña = input("🔑 Contraseña: ")

        if contraseña == contraseña_correcta:
            print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Contraseña correcta. ¡Bienvenid@, {nombre_usuario}!\n")
            time.sleep(1)
            return nombre_usuario
        else:
            intentos -= 1
            print(f"{Fore.RED}❌ Contraseña incorrecta. Te quedan {intentos} intento(s).\n")
            time.sleep(1)

    print(f"{Fore.RED}{Style.BRIGHT}🚫 Acceso denegado. Cerrando el juego...")
    time.sleep(2)
    return None

def main():
    nombre = login()
    if nombre:
        portada(nombre)
        categoria = menu_categorias()
        print(f"Arrancando el juego con categoría: {categoria}")
        jugar(nombre, categoria)
    else:
        print("Juego cerrado.")
        exit()
        
if __name__ == "__main__":
    main()
