import pprint


class data_transform:

    
    def __init__(self):
        pass
    
    def splitter_cell(self, data, key):

        data[key] = data[key].split(",")
        return data
        
    
    def to_int(self, data, key):

        if data[key] != "\\N":
            data[key] = int(data[key])
        return data