def inicio_de_sesion():

    intentos = 0
    clave_correcta = "1234"

    while intentos < 3:
        contraseña = input("Ingrese su contraseña: ")

        if contraseña == clave_correcta:
            print("Acceso Concedido")
            break
        else:
            intentos += 1
            print("Contraseña Incorrecta")

    print("Cuenta bloqueada")

def main():
    inicio_de_sesion()

if __name__ == "__main__":
    main()