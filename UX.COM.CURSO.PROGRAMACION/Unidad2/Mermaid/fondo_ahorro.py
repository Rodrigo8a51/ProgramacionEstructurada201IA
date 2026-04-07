"""
    Algoritmo Fondo de Ahorro
"""
def fondo():
    saldo= 0
    meta = 1000
    while saldo < meta:
        deposito = int(input("Ingrese deposito: "))
        saldo += deposito
    return saldo

def main():
    resultado = fondo()
    print("El fondo de ahorro es", resultado)

if __name__ == "__main__":
    main()
    