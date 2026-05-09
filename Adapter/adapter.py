"""
PATRÓN: ADAPTER (Versión Cargador)

EL PROBLEMA QUE RESUELVE:
Tienes un objeto (iPhone) que espera una interfaz específica (Lightning).
Tienes otro objeto disponible (Cargador Viejo) que ofrece una interfaz distinta (Micro-USB).
No puedes conectar uno al otro directamente porque los "pines" no encajan.

"""

class iPhone:
    def cargar_con_lightning(self):
        return " Cargando iPhone con conector Lightning..."

class CargadorAndroidViejo:
    def conectar_micro_usb(self):
        return "Energía fluyendo por cable Micro-USB"

class AdaptadorCargador:
    def __init__(self, cargador_viejo):
        self.cargador_viejo = cargador_viejo

    def cargar_con_lightning(self):
        energia = self.cargador_viejo.conectar_micro_usb()
        return f"{energia} ---> [Adaptador haciendo magia] ---> {self.iPhone_recibiendo()}"
    
    def iPhone_recibiendo(self):
        return "iPhone cargando correctamente."

if __name__ == "__main__":
    cable_viejo = CargadorAndroidViejo()

    mi_adaptador = AdaptadorCargador(cable_viejo)
    
  
    print("Intentando cargar el teléfono...")
    resultado = mi_adaptador.cargar_con_lightning()
    print(resultado)