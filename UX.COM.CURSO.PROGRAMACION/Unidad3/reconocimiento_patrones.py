def reconocer_patron():
    contador = 0
    concidencia = 0
    patron_maestro = [1, 0, 1, 1, 0]
    lectura_sensor = []

    while len(lectura_sensor) < 5:
        contador += 1
        lectura_sensor.append(int(input(f"Ingrese bit {contador} (0 o 1): ")))
        
    for i in range(len(patron_maestro)):
        if patron_maestro[i] == lectura_sensor[i]:
            concidencia += 1
    
    return concidencia,patron_maestro,lectura_sensor

def porcentaje_similitud(concidencia):
    
    similitud = (concidencia / 5) * 100
    if similitud == 100:
        print("\nESTADO: ACCESO TOTAL: Identidad Verificada.")
    elif similitud >= 60 and similitud < 100:
        print("\nESTADO: ADVERTENCIA: Similitud parcial. Se requiere verificación manual.")
    elif similitud < 60:
        print("\nESTADO: ALERTA: Intruso detectado. Sistema bloqueado.")

    return similitud

def main():
    print("--- ESCÁNER BIOMÉTRICO DE IA ---\n")
    concidencia, patron_maestro, lectura_sensor = reconocer_patron()
    print("\n> Comparando lectura con base de datos...")
    print(f"> Coincidencias encontradas: {concidencia}")

    similitud = porcentaje_similitud(concidencia)
    print(f"> Porcentaje de Similitud: {similitud:.2f}%")   

    print("--- Errores de coincidencia ---")
    print(f"Patrón Maestro: {patron_maestro}")
    print(f"Lectura Sensor: {lectura_sensor}")

if __name__ == "__main__":
    main()
            
