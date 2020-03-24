import pprint


class data_transform:

    
    def __init__(self):
        pass

    # On supprime les "\\N" et on transforme les string en chiffres lorsque pertinent
    def to_int(self, data, key):

        if data[key] != "\\N":
            data[key] = int(data[key])
        return data

    # On splitte les chaines en listes lorsque nécessaire
    def splitter_cell(self, data, key):

        data[key] = data[key].split(",")
        return data