class NAME_BASICS():
    def __init__(self, dico):
        self.birthYear = dico['birthYear'].to_int()

    def to_int(self):
        if self != "\\N":
            self = int(self)
        else:
            self = None
        return self


