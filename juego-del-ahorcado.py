import random

def obtener_palabra_secreta() -> str:
    palabra = ['python', 'javascript','java','angular','django', 'react','typescript','git','flask']
    return random.choice(palabra)

def mostrar_progreso(plabra_secreta, letras_adivindas):
    adivinadas = ''

    for letra in plabra_secreta:
        if letra in letras_adivindas:
            adivinadas += letra
        else:
             adivinadas +="_"    

    return adivinadas

def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 10
    juego_termanado = False

    print("¡Bienvenido al juego del ahorcado")
    print(f"Tenes {intentos} intentos para adivinar la palabra secreta")
    print(mostrar_progreso(palabra_secreta, letras_adivinadas), "La cantidad de letras de la palabra es:", len(palabra_secreta ))

    while not juego_termanado and intentos > 0:
        adivinanza = input("Introdusca una letra:").lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
             print("Por favor introdusca una letra valida(solo escribir una letra) ")
        elif adivinanza in letras_adivinadas:
            print("Ya has utilizado esa letra, prueba con otra")
        else:
            letras_adivinadas.append(adivinanza)

            if adivinanza in palabra_secreta:
                print(f"¡Muy bien has acertado, la letra '{adivinanza}'esta presente en la palabra")
            else:
                intentos -= 1
                print(f"Lo siento mucho la letra '{adivinanza}' no esta presente en la plabra secreta")
                print(f"Te quedan {intentos} intentos")

        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)

        if "_" not in progreso_actual:
           juego_termanado = True
           palabra_secreta = palabra_secreta.capitalize()
           print(f"¡Felicitaciones has ganado la palbra completa es: {palabra_secreta}")
    if intentos == 0: 
         palabra_secreta = palabra_secreta.capitalize()
         print(f"Lo siento mucho se te han acabado los intentos, la palabra secreta era {palabra_secreta}")
        
juego_ahorcado()   