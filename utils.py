import pandas as pd
import numpy as np
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')
from scipy.signal import argrelmax



def mad(dat):
    """
    median absolute deviation.
    Constante: 
    Rc = 1.4826 # aus R
    Rc = 1/qnorm(3/4) # auch aus R
    """
    c=0.67448975019608171
    return np.median(np.abs(dat - np.median(dat)) / c )





def cfor(first,test,update):
    """
    c for style iterator 
    """
    while test(first):
        yield first
        first = update(first)

def snip(data):
    """
    Python Version of the Snip algorithm 
    TODO: 
    has no forward implementation
    should be wrapped into C
    mycall 
    diff -y p.txt c.txt 
    ./loop > c.txt; python scrath.py > p.txt; 

    """
    
    niter = 100
    #decreasing=TRUE
    k = niter
    n = len(data) # n=XLENGTH(y); xy ist double von y
    #n = 20
    xo=np.empty(n)
    xy=data.astype(float)

    for i in cfor(k,lambda i:i>0,lambda i:i-1):
        for j in cfor (i, lambda j : j<n-i, lambda j:j+1  ):
            a=xy[j]
            b=(xy[j-i] +  xy[j+i]) / 2
            if (b<a): a=b
            xo[j]=a
        for j in cfor (i, lambda j : j<n-i, lambda j:j+1  ):
            xy[j]=xo[j]
            
    return xy

def gwl(hwlength):
    """
    get correct window_length for sav golay filter:
    hwlength* 2 + 1
    """
    hwlength = hwlength*2
    if hwlength %  2 == 0: hwlength += 1 
    return hwlength
