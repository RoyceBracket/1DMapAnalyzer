# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 23:39:06 2019

@author: rkrylov1
"""

import numpy as np
from numpy.random import randint
import matplotlib.pyplot as plt

def quadratic_map(x_n, a):
    x_n2 = a + x_n**2
    
    return x_n2

def parameterSweep(start, stop, sampling): 
    a = np.linspace(start, stop, sampling)
    x_n = randint(0, 100)/100
    x_attractor = [[] for i in range(sampling)]
    
    for a_i, x_i in zip(a, x_attractor): 
        for iterations in range(1000): 
            x_n = quadratic_map(x_n, a_i)
            
        for iterations in range(500):
            x_n = quadratic_map(x_n, a_i)
            x_i += [x_n]
    
    return (x_attractor, a)

def orbitDiagramPlot(start, stop, sampling):
    x_attractor, a = parameterSweep(start, stop, sampling)
    
    #ax = plt.subplot()
    a_axis = []
    x = []
    
    for a_i, x_i in zip(a, x_attractor):
        a_axis += [a_i for i in range(len(x_i))]
        x += x_i
    
    
        
    plt.figure(figsize=(12,8), dpi = 80)
    plt.title("Orbit Diagram for Quadratic Map")

    plt.xlabel("a")
    plt.ylabel(r"$x_n$")
    plt.plot(a_axis, x, ".")
        
    plt.show()
    
    return

orbitDiagramPlot(-2, 0.25, 1000)
