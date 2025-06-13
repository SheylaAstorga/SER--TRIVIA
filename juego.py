from colorama import Fore
from preguntas import preguntas

def hacer_preguntas(lista_preguntas):
    puntaje = 0
    correctas = []
    incorrectas = []

    for p in lista_preguntas:
        print(f"\n❓ {p['pregunta']}")
        for i, opcion in enumerate(p['opciones'], 1):
            print(f"  {i}. {opcion}")

        while True:
            respuesta = input("👉 Ingresá el número de tu respuesta: ")
            if respuesta.isdigit() and 1 <= int(respuesta) <= len(p['opciones']):
                break
            else:
                print("⚠️ Opción inválida. Intentá de nuevo.")

        seleccion = p['opciones'][int(respuesta) - 1]
        if seleccion.lower() == p['respuesta'].lower():
            print(f"{Fore.GREEN}✅ ¡Correcto!\n")
            puntaje += 10
            correctas.append(p['pregunta'])
        else:
            print(f"{Fore.RED}❌ Incorrecto. La respuesta correcta era: {p['respuesta']}\n")
            incorrectas.append(p['pregunta'])

    return puntaje, correctas, incorrectas

def resumen_final(nombre, puntaje, correctas, incorrectas):
    print(f"\n🧾 {Fore.MAGENTA}Resumen Final del Juego:")
    print(f"👤 Jugador: {nombre}")
    print(f"🏆 Puntaje total: {puntaje} puntos")
    print(f"✅ Respuestas correctas: {len(correctas)}")
    print(f"❌ Respuestas incorrectas: {len(incorrectas)}")

    if correctas:
        print(f"\n{Fore.GREEN}Preguntas correctas:")
        for preg in correctas:
            print(f" - {preg}")

    if incorrectas:
        print(f"\n{Fore.RED}Preguntas incorrectas:")
        for preg in incorrectas:
            print(f" - {preg}")

    print(f"\n🎉 ¡Gracias por jugar, {nombre}!\n")

def jugar(nombre, categoria):
    puntaje_total = 0
    correctas_totales = []
    incorrectas_totales = []

    print(f"\n{Fore.CYAN}Nivel 1 - Básico: {categoria}")
    nivel1 = preguntas[categoria]["facil"]
    puntaje, correctas, incorrectas = hacer_preguntas(nivel1)

    puntaje_total += puntaje
    correctas_totales.extend(correctas)
    incorrectas_totales.extend(incorrectas)

    if puntaje_total >= 50:
        print(f"\n{Fore.GREEN}🎉 ¡Felicidades {nombre}! Desbloqueaste el Nivel 2 - Avanzado.")
        nivel2 = preguntas[categoria]["dificil"]
        puntaje, correctas, incorrectas = hacer_preguntas(nivel2)

        puntaje_total += puntaje
        correctas_totales.extend(correctas)
        incorrectas_totales.extend(incorrectas)
    else:
        print(f"\n{Fore.YELLOW}🔒 No alcanzaste los 50 puntos. Nivel 2 bloqueado.")

    resumen_final(nombre, puntaje_total, correctas_totales, incorrectas_totales)
