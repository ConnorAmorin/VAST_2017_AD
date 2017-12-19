

# Small Module for loading in VAST 2017 image data csv files. Can load individual (and by season) or all to one data frame for analysis

import glob as glob
import pandas as pd
import numpy as np

def load_season(Spring = True, Winter = False):
    #Get all csv files 
    path = glob.glob('../data/*.csv')
    path.sort()
    #Get the months of each image
    months = [int(i.split('_')[2]) for i in path]
    years = [int(i.split('_')[1]) for i in path]
    months_set = [i for i in range(13)][1:13]
    
    df_list = []
    
    if Spring == True and Winter == False:
        
        for i in range(len(months)):
            if months[i] in [6,8,9]:
                df = pd.read_csv(path[i])
                df['Year'] = years[i]
                df['Month'] = months[i]
                df_list.append(df)
                
    if Spring == False and Winter == True:
        for i in range(len(months)):
            if months[i] in [2,3,11,12]:
                df = pd.read_csv(path[i])
                df['Year'] = years[i]
                df['Month'] = months[i]
                df_list.append(df)
                
    return df_list
                
               
      
        
    
    
    
    
    
    
    
    
    
    
    
    