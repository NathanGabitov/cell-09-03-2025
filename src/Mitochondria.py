from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.Cell import Cell

class Mitochondria:
    _cell = None
    substances = []

    def __init__(self, cell: "Cell"):
        self._cell = cell

    def generateEnergy(self):
        self._cell.setEnergy(self._cell.getEnergy() + 2)
