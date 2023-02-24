import numpy as np
import csv

class HistProcess:
    def __init__(self, 
        input_file:   str
    ):
        self.input_file = input_file
        self.x = []
        self.y = []
        self.maxVal = 0
        self.maxIdx = 0
        with open(self.input_file, "r") as file:
            idx = 0
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                self.x.append(float(row[0]))
                self.y.append(float(row[1]))
                if float(row[1]) > self.maxVal:
                    self.maxVal = float(row[1])
                    self.maxIdx = idx
                idx += 1
        self.__calcFWHM()
    
    def __calcFWHM(self):
        i = self.maxIdx
        while self.y[i] > self.maxVal / 2:
            i -= 1
        left = self.x[i]
        i = self.maxIdx
        while self.y[i] > self.maxVal / 2:
            i += 1
        right = self.x[i - 1]
        self.FWHM = right - left

    def __getFWHM(self):
        return self.FWHM
        
    def process(self):
        self.__readData()
        self.__calFWHM()
        return self.__getFWHM()