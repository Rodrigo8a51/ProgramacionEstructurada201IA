import math

def calculo_esfera():
    radio = float(input("Ingrese el radio de la esfera: "))
    volumen = (4/3) * math.pi * math.pow(radio, 3)
    print("El volumen de la esfera es:", volumen)


def main():
    calculo_esfera()

if __name__ == "__main__":
    main()
