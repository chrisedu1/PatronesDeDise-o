from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass

class NotificadorEmail(Notificador):
    def enviar(self, mensaje):
        print(f" Enviando Email: {mensaje}")

class NotificadorSMS(Notificador):
    def enviar(self, mensaje):
        print(f" Enviando SMS: {mensaje}")

class NotificacionFactory(ABC):
    @abstractmethod
    def crear_notificador(self):
        pass

    def enviar_alerta(self, mensaje):
        notificador = self.crear_notificador()
        notificador.enviar(mensaje)

class EmailFactory(NotificacionFactory):
    def crear_notificador(self):
        return NotificadorEmail()

class SMSFactory(NotificacionFactory):
    def crear_notificador(self):
        return NotificadorSMS()

if __name__ == "__main__":
    print("--- SISTEMA DE ALERTAS ---")
    print("1. Usar Email")
    print("2. Usar SMS")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        fabrica = EmailFactory()
    elif opcion == "2":
        fabrica = SMSFactory()
    else:
        print("Opción inválida.")
        exit()

    fabrica.enviar_alerta("¡Tu código Factory Method funciona!")