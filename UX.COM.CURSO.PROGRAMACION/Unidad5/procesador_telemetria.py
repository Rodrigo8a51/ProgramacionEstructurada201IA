# ==========================================

# IMPORTACIÓN DE BIBLIOTECAS (Biblioteca Estándar)

# ==========================================

import sys

 

# ==========================================

# PEGA AQUÍ LAS 3 FUNCIONES GENERADAS POR IA

# ==========================================

def limpiar_lecturas(lecturas):
    """
    Filtra y retorna una lista de lecturas válidas del sensor LIDAR.
    
    Recibe una lista de números flotantes que representan distancias en metros
    detectadas por el sensor LIDAR de un robot autónomo. Retorna una nueva lista
    conteniendo solo los valores que están dentro del rango válido de 0.0 a 100.0
    metros, ambos inclusive.
    
    Args:
        lecturas (list): Lista de números flotantes representando distancias en metros.
    
    Returns:
        list: Nueva lista con solo los valores válidos (0.0 <= valor <= 100.0).
    """
    lecturas_validas = []
    
    for lectura in lecturas:
        if lectura >= 0.0 and lectura <= 100.0:
            lecturas_validas.append(lectura)
    
    return lecturas_validas

 
def calcular_alertas(lista_filtrada, umbral_critico):
    """
    Cuenta el número de lecturas que están por debajo del umbral crítico de seguridad.
    
    Recibe una lista de números flotantes representando distancias válidas del sensor
    LIDAR y un umbral crítico que indica la distancia mínima de seguridad. Retorna
    la cantidad de lecturas que están por debajo de este umbral, indicando riesgo
    de colisión inmediata.
    
    Args:
        lista_filtrada (list): Lista de números flotantes con distancias válidas en metros.
        umbral_critico (float): Distancia mínima de seguridad en metros.
    
    Returns:
        int: Cantidad de lecturas por debajo del umbral crítico.
    """
    contador_alertas = 0
    
    for lectura in lista_filtrada:
        if lectura < umbral_critico:
            contador_alertas = contador_alertas + 1
    
    return contador_alertas

import sys

def generar_log_sistema(total_alertas):
    """
    Genera un registro de log del sistema con información sobre alertas críticas detectadas.
    
    Esta función construye un mensaje de log que incluye el nombre del sistema operativo,
    la cantidad de alertas críticas encontradas y la acción correspondiente a ejecutar.
    
    Args:
        total_alertas (int): Número entero que representa la cantidad de alertas críticas detectadas.
    
    Returns:
        str: Cadena de texto con formato "[SO] Alertas críticas encontradas: X. Acción: [PERMITIDA o ABORTAR]"
    
    Ejemplos:
        >>> generar_log_sistema(2)
        '[Linux] Alertas críticas encontradas: 2. Acción: PERMITIDA'
        
        >>> generar_log_sistema(5)
        '[Windows] Alertas críticas encontradas: 5. Acción: ABORTAR'
    """
    
    if sys.platform == 'win32':
        nombre_so = 'Windows'
    else:
        if sys.platform == 'linux':
            nombre_so = 'Linux'
        else:
            if sys.platform == 'darwin':
                nombre_so = 'macOS'
            else:
                nombre_so = 'Desconocido'
    
    if total_alertas <= 3:
        accion = 'PERMITIDA'
    else:
        accion = 'ABORTAR'
    
    mensaje = '[' + nombre_so + '] Alertas críticas encontradas: ' + str(total_alertas) + '. Acción: ' + accion
    
    return mensaje

# ==========================================

# PROGRAMA PRINCIPAL (Orquestación Manual)

# ==========================================

if __name__ == "__main__":

    # 1. Datos simulados de telemetría (con algunos errores de sensor)

    lecturas_raw = [-10.5, 150.0, 200.5, -999.0, 250.0, -1.0]

    UMBRAL = 3.0

    print("=== SISTEMA DE TELEMETRÍA DE AGENTE AUTÓNOMO ===\n")

    print(f"Lecturas crudas del sensor LIDAR: {lecturas_raw}")

    lecturas_validas = limpiar_lecturas(lecturas_raw)
    print(f"Lecturas válidas (0.0 a 100.0 metros): {lecturas_validas}")

    total_alertas = calcular_alertas(lecturas_validas, UMBRAL)
    print(f"Total de alertas críticas detectadas: {total_alertas}")

    log_sistema = generar_log_sistema(total_alertas)
    print(f"Registro de log generado: {log_sistema}")

"""
1.-   "Actúa como un programador experto en Python Estructurado.
 
Escribe el código de una función llamada calcular_alertas.
 
Recibe como parámetro:
- lista_filtrada: una lista de números flotantes (ya limpia, sin valores atípicos)
- umbral_critico: un número flotante que representa la distancia mínima de 
  seguridad en metros
 
Debe retornar un número entero que indique cuántas lecturas están por debajo 
del umbral_critico (indicando riesgo de colisión inmediata).
 
Restricciones estrictas:
1. No utilices programación orientada a objetos (POO).
2. No utilices manejo de excepciones (nada de bloques try-except). Gestiona 
   los errores usando condicionales if/else tradicionales.
3. No utilices comprensión de listas ni funciones como sum() con generadores.
4. Usa un bucle for simple y una variable acumuladora.
5. Incluye la documentación de la función mediante un Docstring descriptivo 
   en formato triple comilla

2.-     lecturas_raw = [-10.5, 150.0, 200.5, -999.0, 250.0, -1.0]
        UMBRAL = 3.0
 
limpiar_lecturas([-10.5, 150.0, 200.5, -999.0, 250.0, -1.0]):
  Itera cada valor:
  - -10.5: ¿-10.5 >= 0.0 AND -10.5 <= 100.0? NO → no se añade
  - 150.0: ¿150.0 >= 0.0 AND 150.0 <= 100.0? NO → no se añade
  - 200.5: ¿200.5 >= 0.0 AND 200.5 <= 100.0? NO → no se añade
  - -999.0: ¿-999.0 >= 0.0 AND -999.0 <= 100.0? NO → no se añade
  - 250.0: ¿250.0 >= 0.0 AND 250.0 <= 100.0? NO → no se añade
  - -1.0: ¿-1.0 >= 0.0 AND -1.0 <= 100.0? NO → no se añade
  
  Retorna: [] (lista vacía)
 
calcular_alertas([], 3.0):
  total_alertas = 0
  La lista está vacía, no hay iteraciones
  Retorna: 0
 
generar_log_sistema(0):
  sys.platform = "linux" → nombre_so = "Linux"
  ¿0 <= 3? SÍ → accion = "PERMITIDA"
  mensaje_log = "[Linux] Alertas críticas encontradas: 0. Acción: PERMITIDA"
  Retorna: "[Linux] Alertas críticas encontradas: 0. Acción: PERMITIDA"
 

Lecturas originales: [-10.5, 150.0, 200.5, -999.0, 250.0, -1.0]
Lecturas limpias: []
Número de alertas: 0
Log: [Linux] Alertas críticas encontradas: 0. Acción: PERMITIDA
 
 
3. No fue necesario modificar el código. La IA comprendió 
todas las restricciones y generó correctamente el código.


"""