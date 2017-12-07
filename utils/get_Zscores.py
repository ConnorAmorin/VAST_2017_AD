# -*- coding: utf-8 -*-

import numpy as np

def mean_subtraction(array,means):
    
    for i in range(4):
        new_array = np.copy(array)
        new_array[np.where(new_array[:,-1] == i)][:,2:8] = new_array[np.where(new_array[:,-1] == i)][:,2:8] -  means[i]
        
    return(new_array)        
        
        