# -*- coding: utf-8 -*-

import numpy as np
from scipy import sqrt
def mean_subtraction(array,means):
    
    for i in range(4):
        for j in range(6):
            
            array[np.where(array[:,-1] == i),j+2] -= means[i][j]
        
    return(array) 

def covariance_division(array,covariance):
    
    for i in range(4):
        for j in range(6):
            
            array[np.where(array[:,-1] == i), j+2] /= sqrt(covariance[i])
            
    return array
        
        