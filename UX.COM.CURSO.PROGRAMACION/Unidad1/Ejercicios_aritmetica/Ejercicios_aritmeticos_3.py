import math

def mostrar_funciones_math(numero):

    sen_x = math.sin(numero)
    cos_x = math.cos(numero)
    
    print("El Seno de", numero, "es", sen_x)
    print("El Coseno de", numero, "es", cos_x)

    resultado = sen_x ** 2 + cos_x ** 2

    print("El resultado de sen^2(x) + cos^2(x) es", resultado)


def mostrar_tan_math(numero):
    # TANGENTE DEL NUMERO
    tan_x = math.tan(numero)
    # IMPRIMIR LA TANGENTE
    print("La Tangente de", numero, "es", tan_x)

    # RESULTADO DE LA OPERACION PERO CON TANGENTE
    resultado_tan =  tan_x ** 2
    print("El resultado de tan^2(x) ", resultado_tan)


def main():
    numero = float (input ("Ingresa un numero "))
    mostrar_funciones_math(numero)
    mostrar_tan_math(numero)

if __name__=="__main__":
    main()


