import pprint


class data_transform:

    
    def __init__(self):
        pass
    
    def spliter(self, data, key):

        data[key] = data[key].split(",")
        return data
        
    
    def to_integer(self, data, key):

        if data[key] != "\\N":
            data[key] = int(data[key])
        return data