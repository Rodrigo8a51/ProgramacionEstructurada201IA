def calificaciones():
    calificacion = input("Ingresar numero de calificacion")
    if calificacion > 100:
        print("Ingrese un numero valido")
    elif calificacion >= 90:
        print("Calificacion: A")
    elif calificacion >= 80:
        print("Calificacion: B")
    elif calificacion >= 70:
        print("Calificacion: C")
    elif calificacion >= 69:
        print("Calificacion: D")
    else:
        print("Calificacion: F")
            
def main():
    calificaciones()

if __name__=="__main__":
    main()