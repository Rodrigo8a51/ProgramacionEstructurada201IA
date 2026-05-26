def arithmetic_operators(A, B):
    suma = A + B
    print(f"Suma: {A} + {B} = {suma}")

    resta = A - B
    print(f"Resta: {A} - {B} = {resta}")

    multiplicacion = A * B
    print(f"Multiplicacion: {A} * {B} = {multiplicacion}")

def main():
    print("Arithmetic Operators") 
    A = int(input("Ingrese el primer número entero: "))
    B = int(input("Ingrese el segundo número entero: "))
    arithmetic_operators(A, B)

if __name__ == "__main__":
    main()