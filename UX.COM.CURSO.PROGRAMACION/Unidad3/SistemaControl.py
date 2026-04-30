class ControlAcceso:
    usuarios_autorizados = {
        "2024001": "Investigador", 
        "2024002": "Estudiante", 
        "2024003": "Administrador"
    }
    
    def verificar_permisos(self,matricula):
        print("--- Sistema de Seguridad Laboratorio IA - UX ---")

        if matricula in self.usuarios_autorizados:
            rol = self.usuarios_autorizados[matricula]
            print(f"[ACCESO CONCEDIDO] Bienvenido, rol detectado: {rol}.")

        else:
            print("[ACCESO DENEGADO] Usuario no registrado en la base de datos de IA. ")
        
    def main(self):
        try:
            matricula = input("Ingrese su matrícula: ")
            self.verificar_permisos(matricula)

        except:
            print("Error. Campo vacio")
            
        finally:

            print("--- Intento de acceso registrado en el log del servidor ---")

if __name__ == "__main__":
    control = ControlAcceso()
    control.main()