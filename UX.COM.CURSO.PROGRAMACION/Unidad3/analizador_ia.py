def normalizar_mensaje(comando_de_voz):
    
    texto_limpio = comando_de_voz.lower().strip()
    return texto_limpio

def detectar_intencion(mensaje):


    if ("encender" in mensaje or 
        "activar" in mensaje or 
        "reproducir" in mensaje):
        return "COMANDO DE ACCIÓN"
    
    elif ("ayuda" in mensaje or 
          "error" in mensaje or 
          "fallo" in mensaje):
        return "REPORTE DE SOPORTE"
    
    else:
        return "CONSULTA GENERAL"
    
def main():
    comando_de_voz = input("Ingresa un comando de voz: ")
    mensaje_normalizado = normalizar_mensaje(comando_de_voz)
    categoria = detectar_intencion(mensaje_normalizado)
    longitud  = len(mensaje_normalizado)

    
    print("Mensaje procesado:", mensaje_normalizado)
    print("Categoría detectada:", categoria)
    print("Longitud del comando:", longitud)

if __name__ == "__main__":
    main()