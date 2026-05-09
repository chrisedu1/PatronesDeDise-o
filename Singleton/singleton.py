"""
PATRÓN: SINGLETON

EL PROBLEMA QUE RESUELVE:
Imagina que tienes una conexión a una Base de Datos. Cada vez que haces 
"Conexion()", tu computadora gasta memoria y abre un puerto nuevo. 
Si 1,000 usuarios entran, ¡tu servidor colapsa por tener 1,000 conexiones abiertas!

"""

class ConexionBaseDatos:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            print("\n[SISTEMA]: Creando nueva conexión a la base de datos...")
            cls._instancia = super(ConexionBaseDatos, cls).__new__(cls)
            cls._instancia.datos = "Conectado a MySQL Server"
        else:
            print("\n[SISTEMA]: Ya existe una conexión. Reutilizando la actual...")
        
        return cls._instancia

if __name__ == "__main__":
    print("SOLICITUD 1 ")
    conexion1 = ConexionBaseDatos()
    print(f"Estado: {conexion1.datos}")

    print("\nSOLICITUD 2 ")
    conexion2 = ConexionBaseDatos()
    print(f"Estado: {conexion2.datos}")

    print("\n")
    if conexion1 is conexion2:
        print("RESULTADO: ¡Éxito! Ambas variables son la misma instancia física.")
    else:
        print("RESULTADO: Error. Se crearon objetos diferentes.")