def piloto_automatico():
    distancia = float(input("¿A qué distancia está el objeto más cercano (en metros)?: "))
    color_semaforo = input("¿De qué color está el semáforo? (verde/amarillo/rojo): ").lower()
    peaton = input("¿Hay un peatón cruzando? (si/no): ").lower()

    if distancia < 5 or peaton == "si":
        print("¡FRENO DE EMERGENCIA ACTIVADO! Deteniendo el vehículo inmediatamente.")

    elif color_semaforo == "rojo":
        print("Estado: Detenido. Esperando luz verde.")
    
    elif color_semaforo == "amarillo":
        print("Estado: Precaución. Preparándose para detenerse.")
    
    elif color_semaforo == "verde" and distancia >= 5:
        print("Estado: En movimiento. Todo despejado para avanzar.")
    
    else:
        print("Error de lectura en sensores: Color de semáforo no reconocido.")

   

def main():
    piloto_automatico()


if __name__ == "__main__":
    main()
    