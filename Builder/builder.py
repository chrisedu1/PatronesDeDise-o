from abc import ABC, abstractmethod

class Pizza:
    def __init__(self):
        self.masa = None
        self.salsa = None
        self.ingredientes = []

    def __str__(self):
        return f"Pizza con masa {self.masa}, salsa {self.salsa} e ingredientes: {', '.join(self.ingredientes)}"

#  receta base
class PizzaBuilder(ABC):
    def __init__(self):
        self.pizza = Pizza()

    @abstractmethod
    def poner_masa(self): pass

    @abstractmethod
    def poner_salsa(self): pass

    @abstractmethod
    def poner_ingredientes(self): pass

    def obtener_pizza(self):
        return self.pizza

class PizzaHawaianaBuilder(PizzaBuilder):
    def poner_masa(self): self.pizza.masa = "suave"
    def poner_salsa(self): self.pizza.salsa = "dulce"
    def poner_ingredientes(self): self.pizza.ingredientes = ["piña", "jamón"]

class PizzaPepperoniBuilder(PizzaBuilder):
    def poner_masa(self): self.pizza.masa = "crujiente"
    def poner_salsa(self): self.pizza.salsa = "tomate picante"
    def poner_ingredientes(self): self.pizza.ingredientes = ["pepperoni", "mucho queso"]

class Cocinero:
    def __init__(self):
        self._builder = None

    def construir_pizza(self, builder: PizzaBuilder):
        self._builder = builder
        self._builder.poner_masa()
        self._builder.poner_salsa()
        self._builder.poner_ingredientes()
        return self._builder.obtener_pizza()

if __name__ == "__main__":
    chef = Cocinero()

    print("Cocinando orden 1...")
    pizza1 = chef.construir_pizza(PizzaHawaianaBuilder())
    print(pizza1)

    print("\nCocinando orden 2...")
    pizza2 = chef.construir_pizza(PizzaPepperoniBuilder())
    print(pizza2)