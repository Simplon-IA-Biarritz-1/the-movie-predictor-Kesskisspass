import glob
from tsv import TSV
from db import DB

# On met le chemin vers les fichiers tsv_extract (pour test) dans une variable
data_path = "./tsv_extract/*.tsv"

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

     # On découpe nos fichiers pour les traiter sequentiellement
    liste_dic = tsv.read_seq()

    # On nettoie les données avant de les envoyer en BDD

    # On crée une connexion à MongoDB en créant une collection identique au nom du fichier
    database = DB('tmp_mini',name)
    database.add(liste_dic)
    liste_dic = []