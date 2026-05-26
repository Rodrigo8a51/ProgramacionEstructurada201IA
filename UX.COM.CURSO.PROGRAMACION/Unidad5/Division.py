def division (a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    else:
        print("El resultado de la división es:", a // b)
        print("El resultado de la división con decimales es:", a / b)

def main():
    print("Division")
    a = int(input("Ingrese el primer número entero: "))
    b = int(input("Ingrese el segundo número entero: "))
    division(a, b)

if __name__ == "__main__":
    main()