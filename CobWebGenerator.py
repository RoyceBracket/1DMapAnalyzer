# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:17:05 2019

@author: rkrylov1
"""
import matplotlib.pyplot as plt
import numpy as np
import os
import imageio

def quadratic_map(x_n, params):
    a = params[0]
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


def cobweb_diagram(map1d, params, x0, iterations, xlim, ylim, figname):
    left, right = xlim
    bottom, top = ylim
    points = np.array(cobweb_points(map1d, params, x0, iterations))
    
    x_n = np.linspace(left, right, 100)
    y = []
    for x in x_n:
        y += [map1d(x, params)]
    
    plt.figure(figsize=(12,8), dpi=80)    
    plt.ylim(ylim)
    plt.xlim(xlim)
    plt.ylabel(r'$x_{n+1}$', fontsize=20)
    plt.xlabel(r'$x_n$', fontsize=20)
    plt.plot(x_n, y)
    plt.plot(x_n, x_n)
    plt.plot(points[:, 0], points[:, 1])
    plt.plot(points[80:, 0], points[80:, 1], 'r')
    #filepath = 'C:/Users/rkrylov1/Documents/GSU/Classes/Spring 2019/Hon. Applied Dynamical Systems/1D_Maps/Project/Figures'
    plt.savefig('{}_{}.png'.format(figname, params[1]))
    plt.close()
    #plt.show()
    
    #print(np.array(points))
    return

def generate_GIF(name, filenames):
    with imageio.get_writer('./Animations/{}.gif'.format(name), mode='I') as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)
            
def generate_CobWebImages(cobweb_params, iter_param_index, iter_cond, gif_name):
    map_params = cobweb_params[1]
    filename = cobweb_params[-1]
    iter_param = np.linspace(*iter_cond)
    filenames = []
    i = 0
    for param in iter_param: 
        map_params[iter_param_index] = param
        map_params[1] = i
        cobweb_params[1] = map_params
        cobweb_diagram(*cobweb_params)
        filenames.append("{}_{}.png".format(filename, i))
        i += 1
        
    print(map_params)
    generate_GIF(gif_name, filenames)
    
    return

a = -1
x0 = 0.5
iterations = 100
xlim = (-1.5, 1.5)
ylim = (-1.5, 1.5)
#figname = 'QuadraticMap_a_{}'.format(a)
figname =  './Figures/QuadraticMap_a2'
#cobweb_diagram(quadratic_map, a, x0, iterations, xlim, ylim, figname)
cobweb_params = [quadratic_map, [a, 0], x0, iterations, xlim, ylim, figname]
iter_param_index = 0
iter_cond = (-1, 0.3, 60)
gif_name = 'QuadraticMap_aVarGif3'

#generate_CobWebImages(cobweb_params, iter_param_index, iter_cond, gif_name)

filenames = [ './Figures/QuadraticMap_a2_{}.png'.format(i) for i in range(60)]
#print(filenames)
generate_GIF(gif_name, filenames)
"""
filenames = []
iter_param = np.linspace(*iter_cond)
for param in iter_param:
    filenames.append("{}_{}.png".format(figname, param))
    
generate_GIF(gif_name, filenames)
"""
