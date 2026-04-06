def impares():
    n = int(input("Ingrese cantidad de numeros impares a mostrar: "))
    contador = 0
    numero = 1
    while contador < n:
        print(numero)
        numero = numero + 2
        contador = contador + 1

def main():
    impares()

if __name__=="__main__":
    main()