from src.Cell import Cell
from typing import Union
from src.Glucose import Glucose
from src.Cholesterol import Cholesterol
import random

def generateSubstance():
    random.seed()
    if random.randint(0, 1):
        return Glucose()
    else:
        return Cholesterol()

cell = Cell(1)

i = 1
countBadIteration = 0
countGoodIteration = 0
while cell.getEnergy() < cell.REPRODUCTION_ENERGY_COST:
    print("--------------------------------")
    print("iteration #", i)
    i += 1
    print("Origin energy:", cell.getEnergy())
    
    substance = generateSubstance()

    if cell.membrane.validate(substance) == False:
        print("Bad substance!")
        countBadIteration += 1
        continue
    else:
        print("Good substance!")
        countGoodIteration += 1

    cell.ribosome.generateProtein()

    print("Count energy after generate protein:", cell.getEnergy())
    cell.protein.transportSubstanceInMitochondrion(substance, cell.mitochondria)
    cell.mitochondria.generateEnergy()
    print("After energy:", cell.getEnergy())

cell.divide()
print("Good:", countGoodIteration)
print("Bad:", countBadIteration)