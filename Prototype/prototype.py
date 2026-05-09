import copy

class Personaje:
    def __init__(self, nombre, vida, fuerza):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza

    def clonar(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Personaje: {self.nombre} | Vida: {self.vida} | Fuerza: {self.fuerza}"

if __name__ == "__main__":
    prototipo_orco = Personaje("Orco Guerrero", 100, 20)
    print("Original:", prototipo_orco)

    orco_clonado = prototipo_orco.clonar()
    
    orco_clonado.nombre = "Orco Jefe"
    orco_clonado.vida = 500

    print("Clon modificado:", orco_clonado)
    print("El original sigue igual:", prototipo_orco)