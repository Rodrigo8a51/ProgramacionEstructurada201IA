umbral_pequeño = 5
umbral_grande = 20

def clasificador():
    dimension = float(input("Ingrese el tamaño del objeto detectado (cm): "))
    
    if dimension <= 0:
        print("Error: Lectura inválida. Verifique el sensor.")

    elif dimension > 0 and dimension <= umbral_pequeño:
        print("Clasificación: Micro-componente (Grado A)")

    elif dimension > umbral_pequeño and dimension <= umbral_grande:
        print("Clasificación: Componente Estándar (Grado B)")

    elif dimension > umbral_grande:
        print("Clasificación: Componente Industrial (Grado C)")

        volumen = dimension ** 3
        print("Espacio requerido en contenedor:", volumen, "cm3")

    print("Registro de inspección completado.")

def main():
    clasificador()

if __name__ == "__main__":
    main()