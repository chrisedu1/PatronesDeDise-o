from abc import ABC, abstractmethod

class Computadora:
    def __init__(self):
        self.partes = {}

    def agregar_componente(self, llave, valor):
        self.partes[llave] = valor

    def __str__(self):
        return f"Configuración: {self.partes}"

class ComputadoraBuilder(ABC):
    def __init__(self):
        self.computadora = Computadora()

    @abstractmethod
    def configurar_cpu(self):
        pass

    @abstractmethod
    def configurar_ram(self):
        pass

    @abstractmethod
    def configurar_gpu(self):
        pass

    def obtener_computadora(self) -> Computadora:
        return self.computadora

class BuilderGamer(ComputadoraBuilder):
    def configurar_cpu(self):
        self.computadora.agregar_componente("CPU", "Intel Core i9")

    def configurar_ram(self):
        self.computadora.agregar_componente("RAM", "32GB DDR5")

    def configurar_gpu(self):
        self.computadora.agregar_componente("GPU", "NVIDIA RTX 4090")

class BuilderOficina(ComputadoraBuilder):
    def configurar_cpu(self):
        self.computadora.agregar_componente("CPU", "Intel Core i3")

    def configurar_ram(self):
        self.computadora.agregar_componente("RAM", "8GB DDR4")

    def configurar_gpu(self):
        self.computadora.agregar_componente("GPU", "Integrada")

class Director:
    def __init__(self):
        self._builder = None

    def constructor(self, builder: ComputadoraBuilder):
        self._builder = builder
        self._builder.configurar_cpu()
        self._builder.configurar_ram()
        self._builder.configurar_gpu()
        return self._builder.obtener_computadora()

 
if __name__ == "__main__":
    director = Director()

    print("Construyendo PC Gamer...")
    pc_gamer = director.constructor(BuilderGamer())
    print(pc_gamer)

    print("\nConstruyendo PC de Oficina...")
    pc_oficina = director.constructor(BuilderOficina())
    print(pc_oficina)

