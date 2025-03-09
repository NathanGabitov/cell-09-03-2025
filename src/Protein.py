from src.Mitochondria import Mitochondria
from src.Substance import Substance

class Protein:
    def transportSubstanceInMitochondrion(self, substance:Substance, mitochondria:Mitochondria):
        mitochondria.substances.append(substance)
