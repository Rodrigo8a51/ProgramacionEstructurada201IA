total = 0

def entrenamiento_lotes():
    global total
while True:
    lotes = float(input("Ingrese el tamaño de lotes tensores en MB: "))
    total = total + lotes

    if total >= 2500:
        print("Erorr OOM: Se supero el limite de memoria")
        break
    print("Total de memoria usada:", total, "MB")
        
def main():
    entrenamiento_lotes()

if __name__=="__main__":
    main()