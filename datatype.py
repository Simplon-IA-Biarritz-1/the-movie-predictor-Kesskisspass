# Création des différents types de classe d'objet en fonction des fichiers
#
# 1 - Vérification et gestion de présence de "\N", 
# 2 - transformation des chiffres en float ou int, 
# 3 - split de certaines chaines de caractères en tableaux de string

class NAME_BASICS():
    def __init__(self, dico):
        self._id = dico['nconst']
        self.nconst = dico['nconst']
        self.primaryName = None if dico['primaryName'] == "\\N" else dico['primaryName']
        self.birthYear = None if dico['birthYear'] == "\\N" else int(
            dico['birthYear'])
        self.deathYear = None if dico['deathYear'] == "\\N" else int(
            dico['deathYear'])
        self.primaryProfession = [] if dico['primaryProfession'] == "\\N" else dico['primaryProfession'].split(",")
        self.knownForTitles = [] if dico['knownForTitles'] == "\\N" else dico['knownForTitles'].split(",")


class TITLE_CREW():
    def __init__(self, dico):
        self._id = dico['tconst']
        self.tconst = dico['tconst']
        self.directors = None if dico['directors'] == "\\N" else dico['directors']
        self.writers = None if dico['writers'] == "\\N" else dico['writers']


class TITLE_RATINGS():
    def __init__(self, dico):
        self._id = dico['tconst']
        self.tconst = dico['tconst']
        self.averageRating = None if dico['averageRating'] == "\\N" else float(dico['averageRating'])
        self.numVotes = None if dico['numVotes'] == "\\N" else int(dico['numVotes'])



class TITLE_AKAS:
    def __init__(self, dico):
        self.titleId = dico['titleId']
        self.ordering = None if dico['ordering'] == "\\N" else int(dico['ordering'])
        self.title = None if dico['title'] == "\\N" else dico['title']
        self.region = None if dico['region'] == '\\N' else dico['region']
        self.language = None if dico['language'] == '\\N' else dico['language']
        self.types = None if dico['types'] == '\\N' else dico['types']
        self.attributes = None if dico['attributes'] == '\\N' else dico['attributes']
        self.isOriginalTitle = None if dico['isOriginalTitle'] == '\\N' else int(
            dico['isOriginalTitle'])

class TITLE_BASICS:
    def __init__(self, dico):
        self._id = dico['tconst']
        self.tconst = dico['tconst']
        self.titleType = None if dico['titleType'] == "\\N" else dico['titleType']
        self.primaryTitle = None if dico['primaryTitle'] == "\\N" else dico['primaryTitle']
        self.originalTitle = None if dico['originalTitle'] == "\\N" else dico['originalTitle']
        self.isAdult = None if dico['isAdult'] == "\\N" else int(dico['isAdult'])
        self.startYear = None if dico['startYear'] == "\\N" else int(
            dico['startYear'])
        self.endYear = None if dico['endYear'] == "\\N" else int(
            dico['endYear'])
        self.runtimeMinutes = None if dico['runtimeMinutes'] == "\\N" else int(
            dico['runtimeMinutes'])
        self.genres = [] if dico['genres'] == "\\N" else dico['genres'].split(
            ",")

class TITLE_EPISODE:
    def __init__(self, dico):
        self.tconst = dico['tconst']
        self.parentTconst = None if dico['parentTconst'] == "\\N" else dico['parentTconst']
        self.seasonNumber = None if dico['seasonNumber'] == "\\N" else int(
            dico['seasonNumber'])
        self.episodeNumber = None if dico['episodeNumber'] == "\\N" else int(
            dico['episodeNumber'])


class TITLE_PRINCIPALS:
    def __init__(self, dico):
        self.tconst = dico['tconst']
        self.ordering = None if dico['ordering'] == "\\N" else int(dico['ordering'])
        self.nconst = dico['nconst']
        self.category = dico['category']
        self.job = None if dico['job'] == '\\N' else dico['job']
        self.characters = None if dico['characters'] == '\\N' else dico['characters']