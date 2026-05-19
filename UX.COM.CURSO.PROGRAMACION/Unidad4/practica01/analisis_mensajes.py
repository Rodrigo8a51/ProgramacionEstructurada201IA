# 1. IMPORTACIÓN
# Importamos la biblioteca externa y le asignamos un alias 'np' para facilitar su uso
import numpy as np
def procesar_estadisticas(lista_mensajes):
    """
    Función que recibe datos y utiliza funciones externas de
    la biblioteca NumPy para procesarlos.
    """
    # Invocación de función externa para el promedio
    promedio = np.mean(lista_mensajes)

    # Invocación de función externa para encontrar el valor máximo
    pico_maximo = np.max(lista_mensajes)

    # Invocación de función externa para la desviación estándar
    desviacion = np.std(lista_mensajes)
    
    mediana = np.median(lista_mensajes)

    return promedio, pico_maximo, desviacion, mediana

# --- Programa Principal ---

def main():
    # Datos: Mensajes enviados cada hora durante un turno de 8 horas
    datos_servidor = [15, 42, 88, 30, 120, 55, 72, 20]

    # Llamada a nuestra función enviando los parámetros de entrada
    prom, maximo, ds, mediana = procesar_estadisticas(datos_servidor)

    print("=== REPORTE DE ACTIVIDAD DEL SERVIDOR ===")
    print(f"Promedio de mensajes por hora: {prom:.2f}")
    print(f"Pico de actividad registrado: {maximo} mensajes")
    print(f"Variabilidad del tráfico (Desviación): {np.round(ds, 2)} ")
    print(f"Mediana de mensajes por hora: {mediana:.2f}")

if __name__ == "__main__":
    main()

"""
Si no importamos la biblioteca externa NumPy y ejecutamos el programa,
va a mandar error porque las funciones de la libreria no estan definidas.
"""