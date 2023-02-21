import numpy as np
import csv

class HistProcess:
    def __init__(self, file):
        self.csvRead = csv.reader(file)
        self.x = []
        self.y = []
        self.maxVal = 0
        self.maxIdx = 0
        self.FWHM = 0
    def __readData(self):
        idx = 0
        for row in self.csvRead:
            self.x.append(float(row[0]))
            self.y.append(float(row[1]))
            if float(row[1]) > self.maxVal:
                self.maxVal = float(row[1])
                self.maxIdx = idx
            idx += 1
    def __calFWHM(self):
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