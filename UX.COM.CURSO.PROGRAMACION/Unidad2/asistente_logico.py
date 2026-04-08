def asistente():
    nombre_asistente = "IA-N"
    print("Hola, soy", nombre_asistente, " tu asistente")

    dato = input("¿En qué puedo ayudarte? ").lower()

    if dato == "hola" or "buenos dias":
        print("¡Hola! Soy tu asistente. Es un gusto saludarte.")

    elif dato == "clima" or "temperatura":
         print("Consultando el servicio meteorológico... Hoy en Xalapa tendremos un día nublado.")
    
    


def main():
    asistente()

if __name__ == "__main__":
    main()