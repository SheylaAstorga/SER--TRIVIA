import time
from colorama import init, Fore, Style
from menu import menu_categorias
from juego import jugar
import os

# Inicializa Colorama para que los colores se reseteen automáticamente
init(autoreset=True)

 # Limpia la consola. Usa "cls" para Windows y "clear" para otros sistemas (Linux, Mac)
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

# Muestra la pantalla de bienvenida o portada del juego
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
     # Si se recibió el nombre del usuario, se le da la bienvenida personalizada
    if nombre_usuario:
        print(f"{Fore.MAGENTA}  Bienvenid@, {nombre_usuario}!\n")
    time.sleep(1.5) # Pausa para que el usuario pueda leer
    print(subtitulo)
    time.sleep(1)
    print(bienvenida)
    time.sleep(2)
    # Información extra sobre categorías y dificultad
    print(f"\n{Fore.MAGENTA}  Categorías: Ciencia | Historia | Entretenimiento")
    print(f"{Fore.CYAN}  Dificultad: Fácil / Difícil\n")
    print(f"{Fore.YELLOW}  🎮 ¡Preparate para demostrar cuánto sabés!\n")
    # Pausa para que el usuario presione Enter y comience
    input(f"{Fore.LIGHTWHITE_EX}  Presioná Enter para comenzar...")
    print()
    limpiar_pantalla()
    
# Función para pedir usuario y contraseña antes de empezar el juego
def login():
    contraseña_correcta = "123456"
    intentos = 3

    while intentos > 0:
        print(f"{Fore.YELLOW}BIENVENIDO A ¿SERÁ? ")
        print(f"{Fore.CYAN}🔐 Iniciá sesión para jugar")
        # Pido nombre y contraseña al usuario
        nombre_usuario = input("👤 Ingresá tu nombre: ")
        contraseña = input("🔑 Contraseña: ")
        # Verifico si la contraseña es correcta
        if contraseña == contraseña_correcta:
            print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Contraseña correcta. ¡Bienvenid@, {nombre_usuario}!\n")
            time.sleep(1)
            return nombre_usuario
        else:
            intentos -= 1
            print(f"{Fore.RED}❌ Contraseña incorrecta. Te quedan {intentos} intento(s).\n")
            time.sleep(1)
            
    # Si se acabaron los intentos, muestra mensaje y termina el juego
    print(f"{Fore.RED}{Style.BRIGHT}🚫 Acceso denegado. Cerrando el juego...")
    time.sleep(2)
    return None

def main():
    # Función principal que controla el flujo del programa
    nombre = login()  # Primero login
    
    if nombre:  # Si el login fue exitoso
        portada(nombre)  # Muestra portada personalizada
        categoria = menu_categorias()  # Muestra menú para elegir categoría
        print(f"Arrancando el juego con categoría: {categoria}")
        jugar(nombre, categoria)  # Inicia el juego con usuario y categoría elegida
    else:
        print("Juego cerrado.")
        exit()  # Sale del programa si login falla   
    
    input(f"{Fore.LIGHTWHITE_EX}\nPresioná Enter para salir del juego...")  
    
if __name__ == "__main__":
    main()
