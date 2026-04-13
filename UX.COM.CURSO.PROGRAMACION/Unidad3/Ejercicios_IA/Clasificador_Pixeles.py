#Limpiieza de datos, normalizacion

UMBRAL_ALTO = 0.7
UMBRAL_BAJO = 0.3

def clasificador_pixeles():
    intensidad = float(input("Ingrese la intensidad del pixel (0.0 a 1.0): "))

    if intensidad < 0.0 or intensidad > 1.0:
        print("ERROR: Valor de pixel invalido")
        return
    
    if 0.0 <= intensidad < UMBRAL_BAJO:
        print("Clasificacion (Fondo Oscuro)")
        return
    
    if UMBRAL_BAJO < intensidad < UMBRAL_ALTO:
        print("Clasificacion (Fondo Gris)")
        return

    if intensidad >= UMBRAL_ALTO:
        print("Clasificacion (Objeto Brillante)")
        return
    
    print("Analisis de imagen finalizado")

def main():
    clasificador_pixeles()

if __name__ == "__main__":  
    main()