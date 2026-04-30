class MonitorEntrenamiento:
    historial_errores = []
    umbral_convergencia = 0.01

    def registrar_epoca(self, valor_error):
        
        if valor_error < self.umbral_convergencia:
            print("[SISTEMA] Entrenamiento completado: Se alcanzó el objetivo de precisión.")
        self.historial_errores.append(valor_error)

    def main(self):
        monitor = MonitorEntrenamiento()
        contador = 0

        while contador < 5:
            try:
                error = float(input(f"Ingrese el error de la época {contador + 1}: "))
                monitor.registrar_epoca(error)  
                contador += 1
                print("Registro exitoso.")
                
            except ValueError:
                print("[ERROR] Entrada inválida. Por favor, ingrese un número decimal.")
        
        historial = monitor.historial_errores

        print("\n--- Resumen de Entrenamiento ---")
        print(f"Historial: {historial}")
        print(f"Promedio de Error: {sum(historial) / len(historial):.3f}")
        print(f"Mejor resultado obtenido: {min(historial)}")

if __name__ == "__main__":
    monitor = MonitorEntrenamiento()
    monitor.main()