import csv
import pandas as pd

class TSV:

    # On crée l'instance de notre tsv
    def __init__(self, name):
        self.file = open(f'./tsv_extract/{name}.tsv', 'rt')
        self.path = f'./tsv_extract/{name}.tsv'
        self.name = name
        self.header = self.file.readline()
    
    # On découpe notre fichier en chuncks
    def read_seq(self,chuncksize=100):
        i = 0
        for chunck in pd.read_csv(self.path,delimiter='\t', chunksize=chuncksize):
            print("Chunck",i, self.name)
            liste = []
            # Avec iterrows on va entrer les données en  base
            for index, row in chunck.iterrows():
                # print(len(row))
                dic = row.to_dict()
                liste.append(dic)
            i+= 1
            return liste
            