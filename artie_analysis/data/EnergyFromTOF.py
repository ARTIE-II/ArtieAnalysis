import numpy as np

class EnergyFromTOF:

    def __init__(self, 
        L:      float
    ):
        self.L = L # need to replace with the actual length
        self.c = 299792458 #speed of light in m/s
        self.m = 1.67492749804E-27 #neutron mass in kg
        self.FWHM1 = 1.95
        self.FHWM10 = 0.65
        self.FHWM100 = 0.25
        self.FHWM1000 = 0.17
        self.FHWM10000 = 0.158
        self.FHWM30000 = 0.17
        self.FHWM100000 = 0.148

    def energy(self, tof):
        return self.m * self.c ** 2 * (1 / np.sqrt(1 - (self.L / tof / self.c) ** 2) - 1)

    def tofError(self, tof):
        energy = self.energy(tof)
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
        return tof * FWHM

    def energyError(self, tof):
        energy = self.energy(tof)
        tofError = self.tofError(tof)
        return energy, self.L ** 2 / (1 - self.L ** 2 / tof ** 2 / self.c ** 2) ** 1.5 / tof ** 3 / self.c ** 2 * self.m * self.c ** 2 * tofError

    

    
