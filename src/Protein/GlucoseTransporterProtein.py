from src.Substance.Substance import Substance
from src.Organelles.Mitochondria import Mitochondria
from src.Protein.Protein import Protein
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.Cell import Cell

class GlucoseTransporterProtein(Protein):
    cell = None
    def __init__(self, cell):
        self.cell = cell

    def transportSubstanceInMitochondrion(self, substance:Substance):
        self.cell.mitochondria.substances.append(substance)
