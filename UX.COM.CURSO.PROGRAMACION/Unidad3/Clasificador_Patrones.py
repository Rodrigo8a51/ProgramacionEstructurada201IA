
def clasificar_patron():
    puntajes_sentimiento = [0, 0, 0]
    patron = input("Ingrese una frase de 5 palabras (separada por espacios): ").split()
    for palabra in patron:
        print(f"{palabra}")
        sentimiento = int(input("¿Qué sentimiento detectas? (0: Positivo, 1: Neutral, 2: Negativo): "))
        if sentimiento == 0:
            puntajes_sentimiento[0] += 1
        elif sentimiento == 1:
            puntajes_sentimiento[1] += 1
        elif sentimiento == 2:
            puntajes_sentimiento[2] += 1
    
    return puntajes_sentimiento

def encontrar_mayor(puntajes_sentimiento):
    mayor = puntajes_sentimiento[0]
    indice_mayor = 0

    for i in range(1, 3):
        if puntajes_sentimiento[i] > mayor:
            mayor = puntajes_sentimiento[i]
            indice_mayor = i
        
    return indice_mayor



def main():
    print("--- ANALIZADOR DE SENTIMIENTOS IA ---")  
    puntajes_sentimiento = clasificar_patron()
    indice_mayor = encontrar_mayor(puntajes_sentimiento)
    print("\nEstado final del vector de características:", puntajes_sentimiento)

    if indice_mayor == 0:
        print("Resultado de IA: La frase es Positiva (Predominancia en índice 0)")
    elif indice_mayor == 1:
        print("Resultado de IA: La frase es Neutral (Predominancia en índice 1)")
    elif indice_mayor == 2:
        print("Resultado de IA: La frase es Negativa (Predominancia en índice 2)")

if __name__ == "__main__":
    main()

    


        
