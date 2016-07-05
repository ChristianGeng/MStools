# MStools - Spectral Peaks from Mass-Spectrographic Data 

A sketch of toolbox for the quantitatativa analysis of mass-spectra. They were written out of interest in spectral peak extraction approaches disciplines other than speech sciences. So my primary interest had been in the idea of incorporating ideas from  [Mass-Spectrometry](https://en.wikipedia.org/wiki/Mass_spectrometry) into [formant analysis](https://de.wikipedia.org/wiki/Formant). 

There is no installer, you would simply use git-clone , and install required dependencies manually. 

# Demo
In order to get going, there is a demo that can be found as an ipython notebook at

[https://github.com/ChristianGeng/MStools/blob/master/Demo - Extraction of Energy Peaks in Speech and Mass-Spectrometry.ipynb](https://github.com/ChristianGeng/MStools/blob/master/Demo - Extraction of Energy Peaks in Speech and Mass-Spectrometry.ipynb)

There, first, a standard approach is implemented and described as a baseline.

Second, there is an interesting paper approaching the same problem using Continuous Wavelete Transformas (CWT, see Du, Kibbe & Lin 2006). I did spend less effort in this approach, because the functionality implemented by *MassSpecWavelet* is fully covered by *the find\_peaks\_cwt* with minor changes in the API. 

## Peak Extraction from Mass-Spectrometric and Speech Data
Smoothing, Baseline Removal, Noise level Determination and Peak Picking Approach

##  Assumption(s)
* Data used in these demos are borrowed from the R packages for Mass Spec Peak Determination: *Maldiquant* and *MassSpecWavelet*.
* There is a helper script *createDatasets.r* that can convert demo data into csv's as they are used here. In order to get the script working, these R  packages have to be downloaded and installed into your R environment. Probably there are neater ways to import  data - perhaps via the rpy2 packages. 

## Files
* massSpecObjects.py - Class Definitions
* massSpecTools.py   - algorithms
* utils.py           - utilities
* tests.py           - unit tests
* createDatasets.r   - r script 

## Links
[Peak Picking Blog Eintrag](https://blog.ytotech.com/2015/11/01/findpeaks-in-python/)


# References
C.G. Ryan, E. Clayton, W.L. Griffin, S.H. Sie, and D.R. Cousens. 1988. Snip, a statis-sensitive background treatment for the quantitative analysis of pixe spectra in geoscience applications. Nuclear Instruments and Methods in Physics Research Section B: Beam Interactions with Materials and Atoms, 34(3): 396-402.
M. Morhac. 2009. An algorithm for determination of peak regions and baseline elimination in spectroscopic data. Nuclear Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors and Associated Equipment, 600(2), 478-487.
Du, P., Kibbe, W.A. and Lin, S.M. (2006) Improved peak detection in mass spectrum by incorporating continuous wavelet transform-based pattern matching, Bioinformatics, 22, 2059-2065.
