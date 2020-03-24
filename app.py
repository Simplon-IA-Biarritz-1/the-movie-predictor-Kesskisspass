import glob
from tsv import TSV
from db import DB
import datatype

# On met le chemin vers les fichiers tsv_extract (pour test) dans une variable
data_path = "./tsv_extract/*.tsv"

# Taille découpage fichier
batch_size = 100

# Nom de la database
dbname = 'tmp_mini'

# On regarde le dossier tsv et on récupère la liste des noms
# des fichiers (pour le nom des collections MongoDB)
list_files = [glob.glob(data_path)]
list_names = []

# On liste les fichiers et on stocke le contenu dans une liste
for tsv_file in list_files[0]:
    list_names.append(tsv_file[14:-4])

# On crée notre objet tsv de notre classe tsv en lui passant le chemin
for name in list_names:
    tsv = TSV(name)

    while True:

        # On découpe nos fichiers pour les traiter sequentiellement
        lines = tsv.read_sequential(batch_size)

        if not lines:
            break
        
        list_db = []
        for line in lines:
            if (name == 'name.basics.extract'):
                dic = datatype.NAME_BASICS(line)

            elif (name == 'title.crew.extract'):
                dic = datatype.TITLE_CREW(line)
            
            elif (name == 'title.ratings.extract'):
                dic = datatype.TITLE_RATINGS(line)

            elif (name == 'title.akas.extract'):
                dic = datatype.TITLE_AKAS(line)

            elif (name == 'title.basics.extract'):
                dic = datatype.TITLE_BASICS(line)

            elif (name == 'title.episode.extract'):
                dic = datatype.TITLE_EPISODE(line)

            elif (name == 'title.principals.extract'):
                dic = datatype.TITLE_PRINCIPALS(line)
            else:
                print("File error")
            list_db.append(dic.__dict__)

        # print(len(list_db))
        # On crée une connexion à MongoDB en créant une collection identique au nom du fichier
        database = DB(dbname,name)
        database.add(list_db)
        list_db = []

print("L'import est terminé")