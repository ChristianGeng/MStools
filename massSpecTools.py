# -*- coding: utf-8 -*-
"""Tools for Mass-Spectrographic Peak-Picking

Functions to process mass spectra. 
Class defintions 

Example:
    See the test files

Todo:
    * clarify the division of labor between this function and the utils


"""


import numpy as np
from scipy.signal import savgol_filter
import matplotlib
matplotlib.style.use('ggplot')
from scipy.signal import argrelmax
from  massSpecObjects import massSpectrum, massPeaks
from utils import gwl, snip, mad


def estimateNoise(data, method='MAD'):
    if (method=="MAD"):
        noise = mad(data)
        print(noise)
    return noise


def transformIntensity(msspec,method="sqrt"):
    if (method=="sqrt"):
        print ("default sqrt")
        msspec = massSpectrum (mass=msspec.df['mass'],intensity=np.sqrt(msspec.df['intensity']))
    return msspec

def savitzkyGolay(y, halfWindowSize=10 , polynomialOrder=3):
    return savgol_filter(y, window_length=gwl(halfWindowSize),polyorder=3)

def smoothIntensity(aSpectrum,method="SavitzkyGolay"):
    if (method=="SavitzkyGolay"):
        smoothed=savitzkyGolay(aSpectrum.df["intensity"])
        S=massSpectrum (mass=aSpectrum.df['mass'], intensity=smoothed)
    return S


def removeBaseline(aSpectrum,method="SNIP"):
    if (method=="SNIP"):
        baseline=snip(np.array(aSpectrum.df['intensity']))
        snipped = aSpectrum.df['intensity'] - baseline
        S=massSpectrum (mass=aSpectrum.df['mass'], intensity=snipped)
    return S

def getSpectralPeaks(aSpectrum, method="MAD",halfWindowSize=20, SNR=2):
    if (method=="MAD"):
        idx = argrelmax(np.array(aSpectrum.df['intensity']), order=halfWindowSize)[0]
        noise = estimateNoise(aSpectrum.df['intensity'])
        dfPeaksPython=aSpectrum.df.ix[idx]
        dfPeaksPythonCleaned = dfPeaksPython[dfPeaksPython['intensity'] > (SNR*noise)]
        print(dfPeaksPythonCleaned.columns)
        pks = massPeaks(mass=dfPeaksPythonCleaned['mass'], intensity=dfPeaksPythonCleaned['intensity'])
        return pks

        
