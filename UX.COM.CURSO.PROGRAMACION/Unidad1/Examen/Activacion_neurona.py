def activacion_neurona():
    w = float(input("Ingrese el peso de la entrada: "))
    x = float(input("Ingrese el dato de la entrada: "))

    # Z es el valor de activación de la neurona
    z = w * x
    print("El valor de activacion de la neurona es:", z)

def main():
    activacion_neurona()

if __name__=="__main__":
    main()