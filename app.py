import glob
from tsv import TSV

# On met le chemin vers les fichiers tsv dans une variable
data_path = "./tsv/*.tsv"

# On regarde le dossier tsv et on récupère la liste des noms
# des fichiers (pour le nom des collections MongoDB)
list_files = [glob.glob(data_path)]
list_names = []

# On teste que sur les deux premiers fichiers
for tsv_file in list_files[0][:2]:
    #################################
    list_names.append(tsv_file[6:-4])
print(list_names)

# On crée notre objet tsv de notre classe tsv en lui passant le chemin
for name in list_names:
    tsv = TSV(name)
    tsv.read_seq()