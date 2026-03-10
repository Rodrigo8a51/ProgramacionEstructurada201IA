#Ejemplo para visualizar la indentacion

def explicar_identacion():
    # Nivel 1
    mensaje ="Nivel 1 de Identacion"
    print(mensaje)

    puntos = 10

    if puntos > 0:
        # Nivel 2
        print("Entra al flujo de if")

        if puntos == 10:
            # Nivel 3
            print("Puntos igual a 10")

    # Cierre nivel 3

def main():
    explicar_identacion()

if __name__=="__main__":
    main()
