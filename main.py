from src.Cell import Cell
from src.Substance.Glucose import Glucose
from src.Substance.Cholesterol import Cholesterol
import random

def generateSubstance():
    random.seed()
    if random.randint(0, 1):
        return Glucose()
    else:
        return Cholesterol()

cell = Cell(1)

while cell.getEnergy() < cell.REPRODUCTION_ENERGY_COST:
    substance = generateSubstance()

    if cell.membrane.validate(substance) == False:
        continue

    cell.ribosome.generateProtein()
    cell.protein.transportSubstanceInMitochondrion(substance)
    cell.mitochondria.generateEnergy()

cell.divide()
