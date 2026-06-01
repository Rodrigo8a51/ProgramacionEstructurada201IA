# Declaración de estructuras

productos = ["Laptop", "Smartphone", "Tablet"]
ventas = [[0] * 3 for _ in range(3)]

 

# Lectura de datos
def lectura_ventas():

    for i in range(3):
        print(f"--- Registro para {productos[i]} ---")

        for j in range(3):
            ventas[i][j] = int(input(f"Ventas del día {j+1}: "))


    # Escritura y Reporte
    
def reporte_ventas():
    print("\nRESUMEN DE VENTAS")

    total_general = 0
    total_por_producto = []
    

    for i in range(3):
        suma_producto = sum(ventas[i])
        total_general += suma_producto
        total_por_producto.append(suma_producto)
        print(f"{productos[i]}: {ventas[i]} | Total: {suma_producto}")
        

    print(f"\nEl total de ventas de la semana es: {total_general}")
    print(f"El promedio de ventas es: {total_general / 9:.2f}")

    maximo_ventas_semanal = max(total_por_producto)
    print(f"El máximo de ventas en una semana es: {maximo_ventas_semanal}")

def main():
    lectura_ventas()
    reporte_ventas()

if __name__ == "__main__":
    main()