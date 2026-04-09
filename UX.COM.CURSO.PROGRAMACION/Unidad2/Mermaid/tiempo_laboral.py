def tiempo_laboral():
    total_acumulado = 0
    semanas = 0
    meta = 2500

    while total_acumulado < meta:
        salario_semanal = int(input("Ingresa el salario semanal: "))
        total_acumulado += salario_semanal
        semanas += 1
    return semanas

def main():
    semanas = tiempo_laboral()
    print("Semanas trabajadas:", semanas)

if __name__ == "__main__":
    main()