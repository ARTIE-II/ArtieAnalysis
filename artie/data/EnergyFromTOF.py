import numpy as np

class EnergyFromTOF:
    def __init__(self, tof):
        self.L = 1 # need to replace with the actual length
        self.c = 299792458 #speed of light in m/s
        self.m = 1.67492749804E-27 #neutron mass in kg
        self.FWHM1 = 1.95
        self.FHWM10 = 0.65
        self.FHWM100 = 0.25
        self.FHWM1000 = 0.17
        self.FHWM10000 = 0.158
        self.FHWM30000 = 0.17
        self.FHWM100000 = 0.148
        self.tof = tof
    def __energy(self):
        return self.m * self.c ** 2 * (1 / np.sqrt(1 - (self.L / self.tof / self.c) ** 2) - 1)
    def __tofError(self):
        energy = self.__energy()
        FWHM = 0
        if (energy < 1) :
            FWHM = self.FWHM1
        elif (energy < 10) :
            FWHM = self.FWHM10
        elif (energy < 100):
            FWHM = self.FWHM100
        elif (energy < 1000):
            FWHM = self.FWHM1000
        elif (energy < 10000):
            FWHM = self.FWHM10000
        elif (energy < 30000):
            FWHM = self.FWHM30000
        else:
            FWHM = self.FWHM100000
        return self.tof * FWHM
    def energyError(self):
        energy = self.__energy()
        tofError = self.__tofError()
        return energy, self.L ** 2 / (1 - self.L ** 2 / self.tof ** 2 / self.c ** 2) ** 1.5 / self.tof ** 3 / self.c ** 2 * self.m * self.c ** 2 * tofError

    

    