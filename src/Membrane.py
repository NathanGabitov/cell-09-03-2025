class Membrane:
    _allowedSubstances = []

    def __init__(self, allowedSubstances):
        self._allowedSubstances = tuple(allowedSubstances)
    
    def validate(self, substance):
        return isinstance(substance, self._allowedSubstances)
    