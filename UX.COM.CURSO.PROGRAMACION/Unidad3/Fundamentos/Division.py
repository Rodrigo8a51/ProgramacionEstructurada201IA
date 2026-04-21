def Division(dividendo, divisor):
    if divisor == 0:
        print("El divisor no puede ser cero")
    else:
        cociente = 0
        residuo = dividendo

        while residuo >= divisor:
            residuo = residuo - divisor
            cociente = cociente + 1

        return cociente, residuo

def main():
    cociente, residuo = Division(int(input("Ingrese el dividendo: ")), int(input("Ingrese el divisor: ")))
    print("El cociente es:", cociente)
    print("El residuo es:", residuo)

if __name__ == "__main__":
    main()