class Membrane:
    _allowedSubstances = []

    def __init__(self, allowedSubstances):
        self._allowedSubstances = allowedSubstances
    
    def validate(self, substance):
        return isinstance(substance, self._allowedSubstances)
    