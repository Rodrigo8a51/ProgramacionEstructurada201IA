def DECIMAL_ROMANOS():
    VALORES  = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]

    while True:
        numero  = int(input("Ingrese un número decimal: "))
        if numero > 0  and numero <= 3000:
            ROMANO = ""
            for valor, simbolo in VALORES:
                while numero >= valor:
                    ROMANO += simbolo
                    numero -= valor

            print("El número romano es:", ROMANO)
            break
        else:
            print("Ingrese un número entre 1 y 3000")

def main():
    DECIMAL_ROMANOS()
        
if __name__ == "__main__":
    main()

            