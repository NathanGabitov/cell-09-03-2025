from src.Nucleus.DNA import DNA
from src.Nucleus.RnaPolymerase import RnaPolymerase
from src.Nucleus.RNA import RNA

class Nucleus:
    dna = None
    rna = None

    def __init__(self):
        # ATGTTCGGAAGGCTTAA
        # ATGTTCGGAAGGCTTAG
        self.dna = DNA("ATGTTCGGAAGGCTTAA", self)

    def generateRNA(self):
        self.dna.promotor.attach()
        self.dna.rnaPolymerase.initiation(self.dna)
        rnaSequence = self.dna.rnaPolymerase.elongation()
        self.rna = RNA(rnaSequence)
    
    def generateRnaPolymerase(self):
        return RnaPolymerase()
