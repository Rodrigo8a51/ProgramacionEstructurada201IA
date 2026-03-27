"""
Diseñar un algoritmo que calcule la suma de todos los numeros enteros del 1 al 100 que son divisibles por 3. Imprimir el resultado en pantalla.
"""
def divisible():
    suma = 0
    i = 1

    while i <= 100:
        if i % 3 == 0 and i % 2 != 0:
            suma = suma + i
        i = i + 1
    return suma

def main():
    suma = divisible()
    print(suma)
    
if __name__=="__main__":    
    main()