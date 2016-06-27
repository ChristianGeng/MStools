import pandas as pd
import numpy as np
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
import peakutils
from scipy.signal import argrelmax
import matplotlib.pyplot as plt

class massSpectrum():
    def __init__(self,mass=None, intensity=None):
        self.df=pd.DataFrame()
        self.df["mass"]=mass
        self.df["intensity"]=intensity

class massPeaks(massSpectrum):
    pass
    
#    def __init__(self, mass=None, intensity=None):
#        massSpectrum.__init__(self , mass=None, intensity=None) # call superclass constructor directly
