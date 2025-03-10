from src.Substance.Substance import Substance
from src.Organelles.Mitochondria import Mitochondria
from src.Protein.Protein import Protein

class GlucoseTransporterProtein(Protein):
    def transportSubstanceInMitochondrion(self, substance:Substance, mitochondria:Mitochondria):
        mitochondria.substances.append(substance)
