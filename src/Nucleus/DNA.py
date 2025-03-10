from src.Nucleus.Promotor import Promotor

class DNA:
    sequence = ""
    rnaPolymerase = None
    nucleus = None
    promotor = None

    def __init__(self, sequence, nucleus):
        self.sequence = sequence
        self.promotor = Promotor(self)
        self.nucleus = nucleus
