"""
    Algoritmo de Acumulacion Generica
"""

def acumulacion():
    suma=0
    while suma < 500:
        numero = int(input("Ingresa numero:"))
        suma += numero
    return suma

def main():
    resultado = acumulacion()
    print("La suma acumulacion es", resultado)

if __name__ == "__main__":
    main()
