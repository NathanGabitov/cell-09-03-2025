class Promotor:
    _dna = None

    def __init__(self, dna):
        self._dna = dna

    def attach(self):
        self._dna.rnaPolymerase = self._dna.nucleus.generateRnaPolymerase()
