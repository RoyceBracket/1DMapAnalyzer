# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:17:05 2019

@author: rkrylov1
"""
import matplotlib.pyplot as plt
import numpy as np

def quadratic_map(x_n, a):
    x_n2 = a + x_n**2
    
    return x_n2


#params - params for the map
#start - x_1, initial point
#iterations - number of iterations
    
def cobweb_points(map1d, params, x0, iterations):
    x1 = map1d(x0, params)
    points = [[x0, x1]]
    
    for i in range(iterations):
        points += [[x1, x1]]
        x2 = map1d(x1, params)
        points += [[x1, x2]]
        x1 = x2
    
    return points


def cobweb_diagram(map1d, params, x0, iterations):
    points = np.array(cobweb_points(map1d, params, x0, iterations))
    x_n = np.linspace(0, 1, 100)
    y = []
    for x in x_n:
        y += [map1d(x, params)]
        
    plt.plot(x_n, y)
    plt.plot(x_n, x_n)
    print(points[:, 0])
    plt.plot(points[:, 0], points[:, 1])
    plt.show()
    
    #print(np.array(points))
    return
    
cobweb_diagram(quadratic_map, 0.1, 0.5, 100)
