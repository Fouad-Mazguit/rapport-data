#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.model_selection import LeaveOneGroupOut
from numpy import loadtxt
import scipy as sp
from sklearn import ensemble
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from math import sqrt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
import scipy.io as sio
from sklearn.model_selection import cross_val_score

kfold = 10
ndata = 1346
nrepeat = 10

coddata = np.array([[0 for i in range(nrepeat) ] for j in range(kfold)], dtype=np.float64)
maedata = np.array([[0 for i in range(nrepeat) ] for j in range(kfold)], dtype=np.float64)
msedata = np.array([[0 for i in range(nrepeat) ] for j in range(kfold)], dtype=np.float64)

cod_med = np.array([0 for i in range(kfold)], dtype=np.float64)
mae_med = np.array([0 for i in range(kfold)], dtype=np.float64)
mse_med = np.array([0 for i in range(kfold)], dtype=np.float64)


X = loadtxt("ASorted_HOIP_bg_TPfeature_S3.txt", comments="#", delimiter=",", unpack=False)
y = loadtxt("ASorted_HOIP_bg.txt", comments="#", delimiter=",", unpack=False)


n_splits = 10
kf = KFold(n_splits=10, shuffle=True)

ii=0
for train_index, test_index in kf.split(X):
    print("Fold ", ii)
    
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    
    for jj in range(nrepeat):
    # GBT
        params={'n_estimators': 20000, 'max_depth': 8, 'min_samples_split': 2,
                'learning_rate': 0.001, 'loss': 'ls','max_features':'sqrt','subsample':0.7}
        clf = ensemble.GradientBoostingRegressor(**params)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test) 

        cod = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
   

        print(cod, mae, mse)
        
        coddata[ii,jj] = cod
        maedata[ii,jj] = mae
        msedata[ii,jj] = mse
       
    ii=ii+1

for kk in range(kfold):
    
    cod_med[kk] = np.median(coddata, axis=1)[kk]
    print("CODmed :", cod_med[kk])
   
    mae_med[kk] = np.median(maedata, axis=1)[kk]
    print("MAEmed :", mae_med[kk])
    
    mse_med[kk] = np.median(msedata, axis=1)[kk]
    print("MSEmed :", mse_med[kk])
foutname = "hoip_data_10fold_random.mat"        
sio.savemat(foutname, {"CODmed": cod_med, "MAEmed": mae_med, "MSEmed": mse_med })    
        

    

     


# In[ ]:




