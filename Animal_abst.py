from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        return "Guau"

class Gato(Animal):
    def sonido(self):
        return "Miau"

perro = Perro()
gato = Gato()

print(f"El perro hace: {perro.sonido()}")
print(f"El gato hace: {gato.sonido()}")