from colorama import Fore
from preguntas import preguntas
import os

# Función principal para hacer las preguntas al usuario
def hacer_preguntas(lista_preguntas):
    puntaje = 0                          # Inicializa el puntaje en 0
    correctas = []                       # Lista para guardar preguntas respondidas correctamente
    incorrectas = []                     # Lista para guardar preguntas incorrectas

    # Recorre cada pregunta de la lista
    for p in lista_preguntas:
        print(f"\n {p['pregunta']}")     # Muestra la pregunta

        # Muestra las opciones de respuesta numeradas
        for i, opcion in enumerate(p['opciones'], 1):
            print(f"  {i}. {opcion}")

        # Pide al usuario que elija una opción válida
        while True:
            respuesta = input("👉 Ingresá el número de tu respuesta: ")
            if respuesta.isdigit() and 1 <= int(respuesta) <= len(p['opciones']):
                break
            else:
                print("⚠️ Opción inválida. Intentá de nuevo.")

        # Traduce la respuesta del usuario al texto de la opción elegida
        seleccion = p['opciones'][int(respuesta) - 1]

        # Verifica si la respuesta es correcta (comparación sin distinguir mayúsculas)
        if seleccion.lower() == p['respuesta'].lower():
            print(f"{Fore.GREEN}✅ ¡Correcto!\n")
            puntaje += 10                   # Suma 10 puntos si es correcta
            correctas.append(p['pregunta']) # Guarda la pregunta en la lista de correctas
        else:
            print(f"{Fore.RED}❌ Incorrecto. La respuesta correcta era: {p['respuesta']}")
            if "mensaje" in p:              # Muestra un mensaje educativo si hay
                print(f"{Fore.YELLOW}{p['mensaje']}\n")
            else:
                print()
            incorrectas.append(p['pregunta'])  # Guarda la pregunta en la lista de incorrectas

        # Pregunta si el jugador quiere seguir jugando
        while True:
            continuar = input("¿Deseás seguir jugando? (S/N): ").strip().upper()
            if continuar in ["S", "N"]:
                break
            else:
                print("⚠️ Opción inválida. Ingresá S para seguir o N para salir.")

        # Si elige no continuar, se termina el juego
        if continuar == "N":
            print(f"{Fore.CYAN}👋 ¡Gracias por jugar!")
            break
        else:
            os.system("cls")  # Limpia la pantalla si se sigue jugando

    # Retorna el puntaje final y las listas de correctas e incorrectas
    return puntaje, correctas, incorrectas


# Esta función muestra un resumen final con los resultados del jugador al terminar el juego
def resumen_final(nombre, puntaje, correctas, incorrectas):
    # Calcula el total de preguntas respondidas (correctas + incorrectas)
    total_preguntas = len(correctas) + len(incorrectas)

    # Título del resumen
    print(f"\n🧾 {Fore.MAGENTA}Resumen Final del Juego")
    
    # Muestra los datos principales del jugador
    print(f"{Fore.CYAN}👤 Nombre del jugador: {nombre}")
    print(f"{Fore.YELLOW}🏆 Puntaje obtenido: {puntaje} puntos")
    print(f"✅ Preguntas respondidas correctamente: {len(correctas)} de {total_preguntas}")
    print(f"❌ Preguntas respondidas incorrectamente: {len(incorrectas)}")

    # Si hay preguntas correctas, las muestra en pantalla
    if correctas:
        print(f"\n{Fore.GREEN}✔️ Preguntas correctas:")
        for preg in correctas:
            print(f" - {preg}")

    # Si hay preguntas incorrectas, también las muestra
    if incorrectas:
        print(f"\n{Fore.RED}❌ Preguntas incorrectas:")
        for preg in incorrectas:
            print(f" - {preg}")

    # Mensaje final de despedida personalizado con nombre y dedicatoria
    print(f"\n{Fore.BLUE}🎉 ¡Gracias por participar y jugar, {nombre}!\n")
    print(f"{Fore.MAGENTA}Este juego fue desarrollado con mucho entusiasmo y dedicación")
    print(f"por Sheyla Astorga, para que aprender sea divertido y motivador.")
    print("¡Espero que hayas disfrutado la experiencia y vuelvas pronto a desafiar tus conocimientos! 🚀\n")


# Esta función controla el desarrollo del juego según la categoría elegida y evalúa si se desbloquea el Nivel 2
def jugar(nombre, categoria):
    puntaje_total = 0                # Acumula el puntaje total del jugador
    correctas_totales = []           # Guarda todas las preguntas correctas del jugador
    incorrectas_totales = []         # Guarda todas las preguntas incorrectas del jugador

    # Muestra el título del primer nivel
    print(f"\n{Fore.CYAN}Nivel 1 - Básico: {categoria}")

    # Obtiene las preguntas fáciles según la categoría elegida
    nivel1 = preguntas[categoria]["facil"]
    
    # Llama a la función que hace las preguntas y guarda resultados del Nivel 1
    puntaje, correctas, incorrectas = hacer_preguntas(nivel1)

    # Suma el puntaje y acumula preguntas correctas/incorrectas
    puntaje_total += puntaje
    correctas_totales.extend(correctas)
    incorrectas_totales.extend(incorrectas)

    # Si el jugador consigue 50 puntos o más, accede al Nivel 2
    if puntaje_total >= 50:
        print(f"\n{Fore.GREEN}🎉 ¡Felicidades {nombre}! Desbloqueaste el Nivel 2 - Avanzado.")

        # Obtiene las preguntas difíciles de la misma categoría
        nivel2 = preguntas[categoria]["dificil"]
        
        # Llama a la función para hacer las preguntas del Nivel 2
        puntaje, correctas, incorrectas = hacer_preguntas(nivel2)

        # Suma resultados del segundo nivel
        puntaje_total += puntaje
        correctas_totales.extend(correctas)
        incorrectas_totales.extend(incorrectas)
    else:
        # Si no llega a 50 puntos, no puede jugar el Nivel 2
        print(f"\n{Fore.YELLOW}🔒 No alcanzaste los 50 puntos. Nivel 2 bloqueado.")

    # Llama a la función que muestra el resumen final del juego
    resumen_final(nombre, puntaje_total, correctas_totales, incorrectas_totales)
