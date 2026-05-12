
def monitor_ia():
    temperatura_GPU = float(input("Temperatura actual (°C): "))
    
    while True:
        memoria_VRAM = int(input("Uso de Memoria VRAM (%): "))
        if memoria_VRAM < 0 or memoria_VRAM > 100:
            print("Error: Lectura de memoria fuera de rango (0-100)")
        else:
            break
    
    enfriamiento_activo = input("¿Enfriamiento activo? (si/no): ").strip().lower()

    if temperatura_GPU > 90 or memoria_VRAM == 100:
        return("¡ALERTA CRÍTICA! Apagando servidores para evitar daños físicos.")
    
    elif 75 <= temperatura_GPU <= 90:
        if enfriamiento_activo == "no":
            return("Peligro: Temperatura alta y enfriamiento desactivado. Pausando entrenamiento.")
        else:
            return("Temperatura elevada. Reduciendo velocidad de procesamiento (Throttling).")
    
    elif 75 > temperatura_GPU and memoria_VRAM < 80:
        memoria_libre = 100 - memoria_VRAM
        return(f"Sistema Estable: Temperatura normal. Memoria VRAM libre: {memoria_libre}%")
        

def main():
    print("--- TELEMETRÍA DE CLUSTER IA ---")
    resultado = monitor_ia()
    print("\n> Diagnóstico:", resultado)

if __name__ == "__main__":
    main()