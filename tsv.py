import csv
import pandas as pd

class TSV:

    # On crée l'instance de notre tsv
    def __init__(self, name):
        self.fh = open(f'./tsv/{name}.tsv', 'rt')
        self.path = f'./tsv/{name}.tsv'
        self.name = name
    
    # On découpe notre fichier en chuncks
    def read_seq(self,chuncksize=1000000):
        i = 0
        for chunck in pd.read_csv(self.path,delimiter='\t', chunksize=chuncksize):
            print("Chunck",i, self.name)
            # Avec iterrows on va entrer les données en  base
            # for index, row in chunck.iterrows():
            #     print(index,row)
            i+= 1