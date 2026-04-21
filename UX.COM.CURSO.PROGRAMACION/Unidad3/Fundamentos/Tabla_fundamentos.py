def tabla_multiplicar(n):
    # Encabezado
    print("     ", end="")
    for i in range(1, n+1):
        print(f"{i:4}", end="")
    print()
    
    print("    " + "----" * n)  # Línea separadora
    
    # Filas de la tabla
    for fila in range(1, n+1):
        print(f"{fila:2} *", end="")  # Etiqueta de fila
        for col in range(1, n+1):
            print(f"{fila*col:4}", end="")
        print()  # Salto de línea al terminar cada fila


def main():
    # Pedir al usuario hasta qué número quiere la tabla
    limite = int(input("¿Hasta qué número quieres la tabla de multiplicar? "))
    tabla_multiplicar(limite)


if __name__ == "__main__":
    main()