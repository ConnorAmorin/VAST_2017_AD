# -*- coding: utf-8 -*-
import sys
sys.path.insert(0,'../utils')
import pandas as pd
import numpy as np
from load_data import load_season
from sklearn.mixture import GaussianMixture
from get_Zscores import mean_subtraction,covariance_division
#Load all spring season images
df_list = load_season(Spring = True, Winter = False)

#Gather data, fit the gausian mixture w/ 4 clusters, initialize params with KMEANS
frame = pd.concat(df_list)
data = frame.as_matrix()[:,2:8]
GMM = GaussianMixture(n_components=4,init_params='kmeans',covariance_type = 'spherical')
GMM.fit(data)
means = GMM.means_
covariances = GMM.covariances_
#Append cluster assignments to data frame
frame['Cluster'] = pd.Series(GMM.predict(data))

#Sort data, convert to float
data = frame.as_matrix()
#data = data[data[:,-1].argsort()]
data = data.astype('float64')

#subtract cluster means
mean_subtraction(data,means)
covariance_division(data,covariances)

#Create normalized data frame
norm_data = pd.DataFrame(data)
norm_data.columns = frame.columns
norm_data.Month = norm_data.Month.astype(int)
norm_data.Year = norm_data.Year.astype(int)
df_list = []

for g, df in norm_data.groupby(np.arange(len(norm_data)) // 423801):
        df_list.append(df)

for i in df_list:
    i.to_csv(path_or_buf = (str(int(i.Year.mean())) +'_'+ str(int(i.Month.mean()))+'.csv'))