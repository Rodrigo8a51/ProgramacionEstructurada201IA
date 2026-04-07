"""
    Algoritmo de Acumulacion Generica
"""
def acumulacion():
    suma=0
    while True:
        numero = int(input("Ingresa numero:"))
        if numero >= 10 and numero <=50:
            suma += numero 
        else:
            break
    return suma

def main():
    resultado = acumulacion()
    print("La acumulacion es", resultado)

if __name__ == "__main__":
    main()
