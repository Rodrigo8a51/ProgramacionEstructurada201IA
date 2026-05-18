def acceso_biometrico():
    nombre = input("Nombre del Ingeniero:  ")
    ID = int(input("ID de Empleado:  "))
    iris = input("¿El escaneo de Iris coincide? (si/no): ").strip().lower()
    facial = input("¿El reconocimiento facial es > 95%? (si/no):  ").strip().lower()

    if ID > 0:

        if ID < 100 and facial == "si" and iris == "si":
            print(f"Bienvenido, Ingeniero {nombre}. Acceso nivel SENIOR concedido a todas las áreas.\nGenerando log de entrada para el usuario: [{ID}]...")
    
        elif ID >= 100 and facial == "si" and iris == "si":
            print(f"Bienvenido, Ingeniero {nombre}. Acceso nivel JUNIOR concedido. Áreas de servidores restringidas.\nGenerando log de entrada para el usuario: [{ID}]...")
        
        else:
            print(f"Error Biométrico: Identidad no verificada al 100%. Por favor, contacte a seguridad.")
            
    else:
        print("¡ALERTA DE SEGURIDAD! ID inválido detectado. Bloqueando accesos y notificando a la policía.")

def main():
    print("--- SISTEMA DE ACCESO BIOMÉTRICO ---")
    acceso_biometrico()
    
if __name__ == "__main__":
    main()

    

