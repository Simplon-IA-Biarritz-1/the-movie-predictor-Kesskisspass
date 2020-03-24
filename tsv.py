import csv
import pandas as pd

class TSV:

    
    def __init__(self, name):
        self.fh = open(f'./tsv_extract/{name}.tsv', 'rt')
        self.header = self.fh.readline()

    def read_sequential(self, number_of_lines):
        lines = []
        counter = 0
        line = self.fh.readline()
        while line and counter < number_of_lines:
            lines.append(line)
            counter += 1
            line = self.fh.readline()

        if len(lines) == 0:
            return None

        lines.insert(0, self.header)
        lines_as_dict = csv.DictReader(
            lines, delimiter='\t', quoting=csv.QUOTE_NONE)

        return lines_as_dict