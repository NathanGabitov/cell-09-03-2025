from typing import TYPE_CHECKING
from src.Protein.GlucoseTransporterProtein import GlucoseTransporterProtein
from src.Protein.RibosomeAssemblyProtein import RibosomeAssemblyProtein

if TYPE_CHECKING:
    from src.Cell import Cell

class Ribosome:
    _cell = None

    def __init__(self, cell: "Cell"):
        self._cell = cell
    
    def generateProtein(self):
        if (self._cell.getEnergy() > 0):
            self._cell.nucleus.generateRNA()
            
            if self._cell.nucleus.rna.sequence == "UACAAGCCUUCCGAAUU":
                self._cell.protein = GlucoseTransporterProtein()
            elif self._cell.nucleus.rna.sequence == "UACAAGCCUUCCGAAUC":
                self._cell.protein = RibosomeAssemblyProtein()
            else:
                raise ValueError("Incorrect RNA-sequence")

            self._cell.setEnergy(self._cell.getEnergy() - 1)
        else:
            raise ValueError("Not enough energy!")
