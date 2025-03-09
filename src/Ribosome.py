from typing import TYPE_CHECKING
from src.Protein import Protein

if TYPE_CHECKING:
    from src.Cell import Cell

class Ribosome:
    _cell = None

    def __init__(self, cell: "Cell"):
        self._cell = cell
    
    def generateProtein(self):
        if (self._cell.getEnergy() > 0):
            print("Generate protein")
            self._cell.setEnergy(self._cell.getEnergy() - 1)
            self._cell.protein = Protein()
    