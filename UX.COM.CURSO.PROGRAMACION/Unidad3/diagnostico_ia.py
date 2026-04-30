import math
from datetime import date

def imprimir_encabezado():
    print(50 * "=")
    print("Sistema de Salud Inteligente")
    print("Fecha:", date.today())
    print(50 * "=")

def calcular_imc(peso, estatura):
    imc = peso / (estatura ** 2)
    return imc

def evaluar_presion(presion_sistolica):
    
    if presion_sistolica > 140:
        return("Alta")
    else:
        return("Normal")
    

def main():
    imprimir_encabezado()

    nombre_ususario = input("Nombre del paciente: ")
    peso = float(input("Peso (kg): "))
    estatura = float(input("Estatura (m): "))
    presion_sistolica = int(input("Presión Sistólica: "))

    IMC = calcular_imc(peso, estatura)
    PRESION = evaluar_presion(presion_sistolica)

    print("--- Resultados del Analisis ---")
    print(f"Paciente: {nombre_ususario}\nIMC Calculado: {math.ceil(IMC)}\nEstado de Presión: {PRESION}")

if __name__ == "__main__":
    main()