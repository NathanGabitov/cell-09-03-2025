from src.Cell import Cell
from src.Substance.Glucose import Glucose
from src.Substance.Cholesterol import Cholesterol
import random
import time

ITERATION_TIME_MS = 0

def generateSubstance():
    random.seed()
    if random.randint(0, 1):
        return Glucose()
    else:
        return Cholesterol()

cells = []

start_time = time.time()
while time.time() - start_time < 5:
    cell = Cell(1)

    while cell.getEnergy() < cell.REPRODUCTION_ENERGY_COST:
        start = time.perf_counter()
        substance = generateSubstance()

        if cell.membrane.validate(substance) == False:
            continue

        cell.ribosome.generateProtein()
        cell.protein.transportSubstanceInMitochondrion(substance)
        cell.mitochondria.generateEnergy()
        time.sleep(max(ITERATION_TIME_MS - (time.perf_counter() - start), 0))

        if cell.getEnergy() >= cell.REPRODUCTION_ENERGY_COST:
            cells.append(cell.divide())

print(len(cells))
