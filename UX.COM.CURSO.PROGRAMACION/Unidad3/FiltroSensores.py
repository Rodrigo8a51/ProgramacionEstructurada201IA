def captura_de_datos():
    temperatura = []
    contador = 0
    while contador < 8:

        temperatura.append(float(input(f"Lectura {contador + 1}: ")))
        contador += 1

    return temperatura

def deteccion(temperatura):
    contador_errores = 0

    for i in range(len(temperatura)): 
        if temperatura[i] < 0 or temperatura[i] > 100:
            temperatura[i] = 35.0
            contador_errores += 1

    return contador_errores

def promedio(temperatura):
    suma = 0
    contador = 0

    for i in temperatura:
        suma += i
        contador += 1

    prom = suma / contador
    return prom

def main():
    print("--- SISTEMA DE FILTRADO DE DATOS (SENSOR GPU) ---")

    temperatura = captura_de_datos()

    errores = deteccion(temperatura)

    print(f"\nSe detectaron {errores} lecturas erróneas y fueron corregidas a 35.0")
    print(f"Datos limpios: {temperatura}")

    prom = promedio(temperatura)
    print(f"\nPromedio de operación: {prom:.2f}°C")

    if prom > 75:
        print("ALERTA: Activando sistema de enfriamiento líquido")
    else:
        print("Estado: Operación normal")



if __name__ == "__main__":    
    main()

    
