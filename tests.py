import unittest
from utils import *
from pprint import pprint as pp
from massSpecObjects import *
from massSpecTools import transformIntensity, smoothIntensity
from massSpecTools import removeBaseline, getSpectralPeaks

SpecNo=1
df = pd.read_csv("fiedlerData/"+"Spectrum-"+str(SpecNo).zfill(2)+".csv")
dfPeaks = pd.read_csv("fiedlerData/"+"Spectrum-"+str(SpecNo).zfill(2)+".csv")

S1=massSpectrum(mass=df['mass.s1.'], intensity=df['intensity.s1.'])
S2=transformIntensity(S1)
S3=smoothIntensity(S2)
S4=removeBaseline(S3)
pks = getSpectralPeaks(S4)


class PreProTests(unittest.TestCase):
    """ tests for Fiedler """

    def test_sqrt(self):
        return self.assertTrue(np.allclose(S2.df['intensity'] - df['intensity.s2.'],0))
    def test_savgolay(self):
        return self.assertTrue(np.allclose(S3.df['intensity'] - df['intensity.s3.'],0))
    def test_SNIP(self):
        return self.assertTrue(np.allclose(S4.df['intensity'] - df['intensity.s4.'],0))
        
class NPeaksTest(unittest.TestCase):
    """ test whether we get xxx peaks"""
    def test_npeaks(self):
        return self.assertTrue(pks.df.shape[0] == 207)


if __name__ == '__main__':
    unittest.main()
