from src.Mitochondria import Mitochondria
from src.Ribosome import Ribosome
from src.Nucleus import Nucleus
from src.Membrane import Membrane
from src.Protein import Protein
from src.Glucose import Glucose

class Cell:
    REPRODUCTION_ENERGY_COST = 20    
    mitochondria = None
    ribosome = None
    nucleus = None
    membrane = None
    protein: Protein = None

    _energy = 0

    def __init__(self, energy):
        self._energy = energy
        self.mitochondria = Mitochondria(self)
        self.ribosome = Ribosome(self)
        self.nucleus = Nucleus()
        self.membrane = Membrane([Glucose])

    def divide(self):
        if (self._energy >= self.REPRODUCTION_ENERGY_COST):
            # не ок! Нужно возвращать новый объект этого класса. Иначе выбрасывать исключение
            print("divide")
        else:
            print("not enough energy")

    def setEnergy(self, value):
        self._energy = value
    
    def getEnergy(self):
        return self._energy
    