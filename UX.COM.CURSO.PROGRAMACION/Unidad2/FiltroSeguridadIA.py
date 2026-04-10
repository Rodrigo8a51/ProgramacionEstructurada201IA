

def filtro_seguridad():
    LIMITE_SUPERIROR = 100
    LIMITE_INFERIROR = 0

    lectura = float(input("Ingrese la lectura del sensor térmico: "))

    if lectura >= LIMITE_INFERIROR and lectura <= LIMITE_SUPERIROR:
        dato_normalizado = lectura / LIMITE_SUPERIROR
        print("Señal aceptada. Valor normalizado para el modelo:", dato_normalizado)

    else:
        print( "Error: Lectura fuera de rango. La señal se considera ruido.") 
        
    print("Fin del proceso de filtrado de datos.")