# Recomendador de películas basado en perfiles

def obtener_recomendacion(edad_usuario, genero_elegido):
    
    peliculas_accion = ["Mad Max", "John Wick", "Inception"]
    peliculas_comedia = ["Toy Story", "Minions", "Free Guy"]
    peliculas_terror = ["It", "The Conjuring", "Saw"]

    if edad_usuario < 13 and genero_elegido == "accion" and genero_elegido == "terror":
        print("Nota: Debido a tu edad, hemos ajustado la recomendación a contenido apto para todo público.")
        return peliculas_comedia[0]     
    
    elif edad_usuario < 13:
       return peliculas_comedia[0]  
    
    else:
        if genero_elegido == "accion":
            return peliculas_accion[0]
        elif genero_elegido == "comedia":
            return peliculas_comedia[0]
        elif genero_elegido == "terror":
            return peliculas_terror[0]
        else:
            print("Género no reconocido\nElige entre acción, comedia o terror")

def main():
    print(50 * "=")
    print("¡Bienvenido al recomendador de películas!\nEl Agente de IA de Recomendacion esta activo")
    print(50 * "=")

    edad_usuario = int(input("¿Cuál es tu edad? "))
    genero_elegido = input("¿Qué género de película prefieres? (accion/comedia/terror): ").lower()
    print(50 * "=")

    recomendacion = obtener_recomendacion(edad_usuario, genero_elegido)
    print(f"Recomendación de la IA: {recomendacion}")

if __name__ == "__main__":
    main()