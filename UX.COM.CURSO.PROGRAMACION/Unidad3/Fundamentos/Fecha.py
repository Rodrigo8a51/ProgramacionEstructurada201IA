def validacion_fecha():
    
    DIA = int(input("Ingrese el día: "))
    
    while True:   
        MES = int(input("Ingrese el mes: "))
        if MES >= 1 and MES <= 12:
            break
        else:
            print("Ingrese un mes válido")

    while True:
        AÑO = int(input("Ingrese el año: "))   
        if AÑO > 0:
            break
        else:
            print("Ingrese un año válido")
    
    if MES in [1, 3, 5, 7, 8, 10, 12]:
        dias_mes = 31

    elif MES in [4, 6, 9, 11]:
        dias_mes = 30

    else:
        if (AÑO % 4 == 0 and AÑO % 100 != 0) or (AÑO % 400 == 0):
            dias_mes = 29

        else:
            dias_mes = 28
            
    if DIA >= 1 and DIA <= dias_mes:
        print("La fecha es VALIDA:",DIA,"/",MES,"/",AÑO)
    else:
        print("La fecha es INVALIDA")
        
def main():
    validacion_fecha()

if __name__ == "__main__":
    main()


 
