# -*- coding: utf-8 -*-
import sys
sys.path.insert(0,'../utils')
import pandas as pd
import numpy as np
from load_data import load_season
from sklearn.mixture import GaussianMixture

#Load all spring season images
df_list = load_season(Spring = True, Winter = False)

#Gather data, fit the gausian mixture w/ 4 clusters, initialize params with KMEANS
frame = pd.concat(df_list)
data = frame.as_matrix()[:,2:8]
GMM = GaussianMixture(n_components=4,init_params='kmeans')
GMM.fit(data)
means = GMM.means_

#Append cluster assignments to data frame
frame['Cluster'] = pd.Series(GMM.predict(data))


#Assign z-scores for each band for a given data point
data = frame.as_matrix()
data = data[data[:,-1].argsort()]

#Cluster matrices
cluster1 = data[np.where(data[:,-1] == 0)][:,2:8]
cluster2 = data[np.where(data[:,-1] == 1)][:,2:8]
cluster3 = data[np.where(data[:,-1] == 2)][:,2:8]
cluster4 = data[np.where(data[:,-1] == 3)][:,2:8]

cluster_list = [cluster1,cluster2,cluster3,cluster4]
#Subtract mean
for i in range(4):
    
    cluster_list[i] = cluster_list[i] - means[i]
    
