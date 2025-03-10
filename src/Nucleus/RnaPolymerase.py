class RnaPolymerase:
    _dna = None

    def initiation(self, dna):
        self._dna = dna

    def elongation(self):
        dnaToMrnaTable = {
            "T": "A", "A": "U", "C": "G", "G": "C"
        }
        return "".join(dnaToMrnaTable.get(n, "N") for n in self._dna.sequence[:48])

    def termination(self):
        pass
