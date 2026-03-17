import math

def mostrar_funciones_math():
    numero = 20

    sen_x = math.sin(numero)
    cos_x = math.cos(numero)
    
    print("El Seno de", numero, "es", sen_x)
    print("El Coseno de", numero, "es", cos_x)

    resultado = sen_x ** 2 + cos_x ** 2

    print("El resultado de sen^2(x) + cos^2(x) es", resultado)

def main():
    mostrar_funciones_math()

if __name__=="__main__":
    main()


