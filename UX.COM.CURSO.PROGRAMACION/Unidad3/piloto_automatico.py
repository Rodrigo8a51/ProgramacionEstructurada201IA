def piloto_automatico():
    distancia = float(input("¿A qué distancia está el objeto más cercano (en metros)?: "))
    color_semaforo = input("¿De qué color está el semáforo? (verde/amarillo/rojo): ").lower()
    peaton = input("¿Hay un peatón cruzando? (si/no): ").lower()

    if distancia < 5 or peaton == "si":
        print("¡FRENO DE EMERGENCIA ACTIVADO! Deteniendo el vehículo inmediatamente.")



def main():
    piloto_automatico()


if __name__ == "__main__":
    main()
    