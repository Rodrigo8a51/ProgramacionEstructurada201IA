def asistente():
    nombre_asistente = "IA-N"
    print("Hola, soy", nombre_asistente, " tu asistente")

    dato = input("¿En qué puedo ayudarte? ").lower()

    if "hola" in dato or "buenos dias" in dato:
        print("¡Hola! Soy tu asistente. Es un gusto saludarte.")
    
    elif "clima" in dato or "temperatura" in dato:
         print("Consultando el servicio meteorológico...  \n Hoy en Xalapa tendremos un día nublado.")



    


def main():
    asistente()

if __name__ == "__main__":
    main()