

from abc import ABC, abstractmethod

class ElementoMenu(ABC):
    @abstractmethod
    def obtener_precio(self):
        pass

class Producto(ElementoMenu):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def obtener_precio(self):
        return self.precio

class Combo(ElementoMenu):
    def __init__(self, nombre):
        self.nombre = nombre
        self.items = []

    def agregar(self, elemento: ElementoMenu):
        self.items.append(elemento)

    def obtener_precio(self):
        total = 0
        for item in self.items:
            total += item.obtener_precio()
        return total

if __name__ == "__main__":
    hamburguesa = Producto("Hamburguesa Real", 50)
    papas = Producto("Papas Fritas", 20)
    refresco = Producto("Refresco Grande", 15)

    combo_familiar = Combo("Combo Familiar")
    combo_familiar.agregar(hamburguesa)
    combo_familiar.agregar(papas)
    combo_familiar.agregar(refresco)

    super_mega_combo = Combo("Super Mega Combo")
    super_mega_combo.agregar(combo_familiar)
    super_mega_combo.agregar(Producto("Helado", 10))

    print(f"Precio Hamburguesa sola: ${hamburguesa.obtener_precio()}")
    print(f"Precio del Combo Familiar: ${combo_familiar.obtener_precio()}")
    print(f"Precio del Super Mega Combo: ${super_mega_combo.obtener_precio()}")