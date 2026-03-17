def ejemplo_for():
    print("Estructura FOR")

    frutas = ["manzana","banana","naranja"]

    for fruta in frutas:
        print (fruta)

# FOR para iterar rangos
    for i in range(1,5):
        print(i)

# FOR iterar rangos con pasos
    for i in range(1,10,2):
        print(i)

# Ejemplo while
def ejemplo_while():
    print("Estructura while")

    contador = 0

    while contador < 5:
        print(contador)
        contador += 1

# Ejemplo DO WHILE
def ejemplo_do_while():
    print("Estructura DO WHILE")

    secreto = "python12"
    intentos = 0

    while True:
        intentos_usuario = "python12" # Simulacion la entrada usuario
        intentos += 1

        if intentos_usuario == secreto: 
            print("Acceso Concedido")
            break
        else:
            print("Acceso Denegado")
            break
        print("\n")

def main():
    ejemplo_for()
    ejemplo_while()
    ejemplo_do_while()

if __name__=="__main__":
    main()
