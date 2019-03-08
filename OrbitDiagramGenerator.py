# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 23:39:06 2019

@author: rkrylov1
"""

import numpy as np
from numpy.random import randint

def quadratic_map(x_n, a):
    x_n2 = a + x_n**2
    
    return x_n2

def parameterAttractor(a, start, stop, sampling): 
    a = np.linspace(start, stop, sampling)
    x_n = randint(0, 100)/100
    x_attractor = [[] for i in range(sampling)]
    
    for a_i, x_i in zip(a, x_attractor): 
        for iterations in range(1000): 
            x_n = map(x_n, a_i)
            
        for iterations in range(300):
            x_n = map(x_n, a_i)
            x_i += [x_n]
    
    return (x_attractor, a)

def orbitDiagramPlot(x_attractor, a):
    
    return

