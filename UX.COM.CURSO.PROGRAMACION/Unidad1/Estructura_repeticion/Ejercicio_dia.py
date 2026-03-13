def dia():
    opcion = input("Ingrese una opcion (1-7): ")
    match opcion:
        case "1":
            print("Opcion 1 seleccionada")
            print("El dia es Lunes")
        case "2":
            print("Opcion 2 seleccionada")
            print("El dia es Martes")
        case "3":
            print("Opcion 3 seleccionada")
            print("El dia es Miercoles")
        case "4":
            print("Opcion 4 seleccionada")
            print("El dia es Jueves")
        case "5":
            print("Opcion 5 seleccionada")
            print("El dia es Viernes")
        case "6":
            print("Opcion 6 seleccionada")
            print("El dia es Sabado")
        case "7":
            print("Opcion 7 seleccionada")
            print("El dia es Domingo")
        case _:
            print("Opcion no valida")

def main():
    dia()

if __name__ == "__main__":
    main()