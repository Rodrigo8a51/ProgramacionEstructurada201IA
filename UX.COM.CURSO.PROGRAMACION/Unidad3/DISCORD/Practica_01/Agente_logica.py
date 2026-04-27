
""" Funcion que recibe un texto y decide que responder. Implementa Programacacion Estrucutura pura. """

def procesar_pregunta(mensasje_usuario):
    #1.Normalizacion (Paso fundamental en IA)
    mensaje = mensasje_usuario.lower().strip()

    #2.Base de conocimiento (Diccionario)
    conocimiento = {
        #Concepto de Estructura de Control
        "if": "La sentencia 'if' es una condicional. Permite que el programa tome decisiones basandose en una condicion booleana.",
        "else": "La sentencia 'else' se ejecuta cuando la condicion del 'if' es falsa.",
        "elif": "Es una combinacion de 'else' y 'if'. Permite evaluar multiples condiciones.",
        "while": "Es un ciclo que se repite mientras una condicion sea verdadera.",

        #Tipos de Datos
        "int": "Representa un numero entero (ej. 5, -10, 0). No tienen parte decimal.",
        "float": "Representa numeros con punto decimal (ej. 3.14, -2.5).",
        "str": "Representa cadenas de texto (ej. 'hola', 'python').",
        "bool": "Representa valores logicos: True o False.",

        #Funciones y modularidad
        "def": "Es la palabra reservada para definir una funcion en python",
        "parametro": "Es un valor que una funcion recibe para poder trabajar con datos de entrada.",
        "return": "Permite a una funcion devolver un resultado.",
        "modulo": "Es un archivo que contiene funciones o codigo reutilizable que se puede importar en otros programas.",

        #Operadores y Sintaxis
        "print": "Funcion que muestra informacion en la consola o salida estandar",
        "+": "Operador de suma. Tambien se usa para concatenar cadenas.",
        "==": "Operador de comparacion. Verifica si dos valores son iguales.",
        "!=": "Operador de comparacion. Verifica si dos valores son diferentes.",

        #Conceptos de Programacion Estructurada
        "algoritmo": "Es una serie de pasos ordenados y finitos para resolver un problema",
        "variable": "Es un espacio en memoria donde se almacena un valor que puede cambiar.",
        "bucle": "Estructura que permite repetir un conjunto de instrucciones varias veces.",
        "condicion": "Es una expresion que se evalua como verdadera o falsa."
    }

    #3.Logica de busqueda
    for clave in conocimiento:
        if clave in mensaje:
            return conocimiento[clave]

    return "Lo siento, aun no se que es eso. !Preguntame sobre variables, funciones o estructuras de control!"


def main():
    print("Hola! Soy tu asistente de programacion. Preguntame sobre variables, funciones o estructuras de control.")
    
    while True:
        user_input = input("Alumno -> ")
        if user_input.lower() == "salir":
            break

        respuesta = procesar_pregunta(user_input)
        print(f"Bot -> {respuesta}")


# Prueba local (Offline)
if __name__ == "__main__":
    main()

 