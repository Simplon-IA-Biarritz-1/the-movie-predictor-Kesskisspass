class NAME_BASICS():
    def __init__(self, dico):
        self._id = dico['nconst']
        self.nconst = dico['nconst']
        self.primaryName = dico['primaryName']
        self.birthYear = None if dico['birthYear'] == "\\N" else int(
            dico['birthYear'])
        self.deathYear = None if dico['deathYear'] == "\\N" else int(
            dico['deathYear'])
        self.primaryProfession = dico['primaryProfession'].split(",")
        self.knownForTitles = dico['knownForTitles'].split(",")



