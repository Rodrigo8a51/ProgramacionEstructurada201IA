"""
    Algoritmo Fondo de Ahorro
"""
def fondo():
    saldo= 0
    meta = 1000
    while saldo < meta:
        deposito = float(input("Ingrese deposito: "))
        saldo += deposito
    return saldo

def main():
    resultado = fondo()
    print("La meta ha sido superada", resultado)

if __name__ == "__main__":
    main()
    