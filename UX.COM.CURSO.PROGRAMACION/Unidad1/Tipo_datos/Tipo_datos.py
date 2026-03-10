#  Demostracion de tipo de datos en Python
def datos():
    entero=25
    decimal = 3.14
    cadena = "Hola Mundo"
    booleano = True

    print(entero)
    print(decimal)
    print(cadena)
    print(booleano)

def tipos_datos_compuestos():
    lista=[10,20,30,40]
    tupla=[19,29,39,49]
    diccionario = {"nombre": "Juan", "Edad": 30, "ciudad": "Madrid"}

    print(lista)
    print(tupla)
    print(diccionario)

def main():
    datos()

if __name__=="__main__":
    main()