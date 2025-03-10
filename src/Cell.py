from src.Organelles.Mitochondria import Mitochondria
from src.Organelles.Ribosome import Ribosome
from src.Nucleus.Nucleus import Nucleus
from src.Membrane import Membrane
from src.Substance.Glucose import Glucose
from src.Protein.Protein import Protein

class Cell:
    REPRODUCTION_ENERGY_COST = 20    
    mitochondria:Mitochondria = None
    ribosome:Ribosome = None
    nucleus:Nucleus = None
    membrane:Membrane = None
    proteins:Protein = None

    _energy = 0

    def __init__(self, energy):
        self._energy = energy
        self.mitochondria = Mitochondria(self)
        self.ribosome = Ribosome(self)
        self.nucleus = Nucleus()
        self.membrane = Membrane((Glucose))

    def divide(self):
        if (self._energy >= self.REPRODUCTION_ENERGY_COST):
            return Cell(self.getEnergy() / 2)
        else:
            raise ValueError("Not enough energy")

    def setEnergy(self, value):
        self._energy = value
    
    def getEnergy(self):
        return self._energy
    