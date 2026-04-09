
def asistente_ia():
    UMBRAL_ALTO = 80.0
    UMBRAL_MINIMO = 40.0

    instrucción_detectada = input("Instrucción recibida: ")
    nivel_confianza = float(input("Nivel de confianza calculado (%): "))

    if nivel_confianza >= UMBRAL_ALTO:
        print("Ejecutando la acción:" + instrucción_detectada + "... (Éxito)")

def main():
    asistente_ia()
    
if __name__ == "__main__":    
    main()
