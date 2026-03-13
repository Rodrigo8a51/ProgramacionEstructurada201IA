def demostracion():
    print("- Ejemplo de match -")
    opcion = input("Ingrese una opcion (1-3): ")
    match opcion:
        case "1":
            print("Opcion 1 seleccionada")
            nombre = input("Ingrese su nombre: ")
            print(f"Su nombre es: {nombre}")
        case "2":
            print("Opcion 2 seleccionada")
            matricula = input("Ingrese su matricula: ")
            print(f"Su matricula es: {matricula}")
        case "3":
            print("Opcion 3 seleccionada")
            semestre = input("Ingrese su semestre: ")
            print(f"Su semestre es: {semestre}")
        case _:
            print("Opcion no valida0")

def main():
    demostracion()

if __name__ == "_main_":
    main()