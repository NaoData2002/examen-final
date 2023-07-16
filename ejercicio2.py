import random
import datetime

class AdivinaNumero:
    def __init__(self):
        self.numero_secreto = self.genera_numero()
        self.intentos = 0

    @staticmethod
    def genera_numero():
        return random.randint(1, 40)

    def verifica_numero(self, entrada):
        try:
            entrada = int(entrada)
            if entrada > 0 and entrada < 100:
                self.intentos += 1
                if entrada == self.numero_secreto:
                    return True
                elif entrada > self.numero_secreto:
                    print("El número es más pequeño. Intenta nuevamente.")
                    return False
                else:
                    print("El número es más grande. Intenta nuevamente.")
                    return False
            else:
                print("Por favor, ingresa un número entre 1 y 100.")
                return False
        except ValueError:
            print("Por favor, ingresa un número válido.")
            return False

    def jugar(self):
        print("¡Bienvenido al juego Adivina el Número!")
        acierto = False
        while not acierto:
            entrada = input("Ingresa un número: ")
            acierto = self.verifica_numero(entrada)
        print(f"¡Has ganado! El número era {self.numero_secreto}. Lo adivinaste después de {self.intentos} intentos.")
        ahora = datetime.datetime.now()
        print(f"Ganaste el {ahora.day}/{ahora.month}/{ahora.year} a las {ahora.hour}:{ahora.minute}")

if __name__ == "__main__":
    juego = AdivinaNumero()
    juego.jugar()
