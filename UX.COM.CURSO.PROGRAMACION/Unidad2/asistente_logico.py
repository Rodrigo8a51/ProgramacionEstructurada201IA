import datetime
hora = datetime.datetime.now()
hora_actual = hora.strftime("%H:%M")

def asistente():
    nombre_asistente = "IA-N"
    print("Hola, soy", nombre_asistente, "tu asistente")

    dato = input("¿En qué puedo ayudarte? ").lower()

    if "hola" in dato or "buenos dias" in dato:
        print("¡Hola! Soy tu asistente. Es un gusto saludarte.")
    
    elif "clima" in dato or "temperatura" in dato:
         print("Consultando el servicio meteorológico...\nHoy en Xalapa tendremos un día nublado.")
    
    elif "hora" in dato or "tiempo" in dato:
        print("La hora actual del sistema es:", hora_actual)
    
    else:
        print("Lo siento, todavía no entiendo ese comando. ¿Podrías intentar con otra palabra?")
    
    print("Proceso finalizado. Gracias por usar", nombre_asistente)


def main():
    asistente()

if __name__ == "__main__":
    main()