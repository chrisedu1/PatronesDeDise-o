"""
PATRÓN: BRIDGE (Puente)

EL PROBLEMA QUE RESUELVE:
Evita la "Explosión de Clases". Si tienes N formas y M colores, sin este patrón 
necesitarías (N * M) clases. Con Bridge, solo necesitas (N + M) clases.
"""

from abc import ABC, abstractmethod

class Color(ABC):
    @abstractmethod
    def aplicar_color(self):
        pass

class Rojo(Color):
    def aplicar_color(self):
        return "aplicando color ROJO"

class Azul(Color):
    def aplicar_color(self):
        return "aplicando color AZUL"

class Forma(ABC):
    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def dibujar(self):
        pass

class Circulo(Forma):
    def dibujar(self):
        print(f"Dibujando un Círculo y {self.color.aplicar_color()}")

class Cuadrado(Forma):
    def dibujar(self):
        print(f"Dibujando un Cuadrado y {self.color.aplicar_color()}")

if __name__ == "__main__":
    color_rojo = Rojo()
    circulo = Circulo(color_rojo)
    circulo.dibujar()

    color_azul = Azul()
    cuadrado = Cuadrado(color_azul)
    cuadrado.dibujar()
    
    circulo_azul = Circulo(color_azul)
    circulo_azul.dibujar()