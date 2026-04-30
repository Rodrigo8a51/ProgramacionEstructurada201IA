def modulo_sensores():
    print("--- MÓDULO DE SENSORES (VECTORES) ---")

    sensores_distancia = []
    suma = 0

    for i in range(5):
        distancia = float(input(f"Ingrese distancia sensor {i+1}: "))
        sensores_distancia.append(distancia)
        suma += distancia

    promedio = suma / len(sensores_distancia)

    if promedio < 2.0:
        print(f"\nPromedio de proximidad: {promedio:.2f}m. Estado: Peligro.")
        print("Aviso: Reduciendo velocidad global")
    else:
        print(f"\nPromedio de proximidad: {promedio:.2f}m. Estado: Seguro.")


def modulo_camara():
    print("\n--- MÓDULO DE VISIÓN (MATRICES) ---")
    print("Llenando matriz de cámara 3x3:\n")

    camara_ia = []

    for fila in range(3):
        fila_actual = []
        for col in range(3):
            valor = int(input(f"Fila {fila}, Col {col} (Brillo 0-255): "))

            if valor > 255:
                valor = 255
            elif valor < 0:
                valor = 0

            fila_actual.append(valor)
        camara_ia.append(fila_actual)


    print("\nVisualización de la imagen capturada:\n")
    for fila in camara_ia:
        print("[ ", end="")
        for valor in fila:
            print(f"{valor:3}", end=" ")
        print("]")

    return camara_ia

def detectar_brillo(camara):
    contador = 0

    for fila in camara:
        for valor in fila:
            if valor > 200:
                contador += 1

    print("\nResultado de Análisis IA:")
    print(f"Se detectaron {contador} píxeles de alta intensidad.")


def main():
    modulo_sensores()
    camara = modulo_camara()
    detectar_brillo(camara)


if __name__ == "__main__":
    main()