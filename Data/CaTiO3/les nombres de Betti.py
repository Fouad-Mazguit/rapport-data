#!/usr/bin/env python
# coding: utf-8

# # Ici on va importer les packages de Python

# In[14]:


import gudhi as gd
import scipy.io as sio
import math
import matplotlib.pyplot as plt
import numpy as np


# # On donne les coordonnées de chaque atome 

# In[16]:



coords = {'Ti':[[5,5,5]], 'O':[[5, 5, 10], [5, 10, 5], [10, 5, 5], [5,0,5], [0, 5, 5], [5, 5, 0]]}
coords['Ca'] = [[10, 10, 0], [10, 0, 0], [10, 0, 10], [10, 10, 10], [0, 10, 0], [0, 0, 0], [0, 0, 10], [0, 10, 10]]
data = []
for key, val in coords.items():
    for j in val:
        data.append(j)

mat = np.zeros((len(data), len(data)))
for i in range(len(data)):
    for j in range(len(data)):
        dist = np.linalg.norm(np.array(data[i])-np.array(data[j]))
        mat[i][j] = dist

rips = gd.AlphaComplex(data)
st = rips.create_simplex_tree()
dgmsalpha = st.persistence()

betti0, betti1, betti2 = [], [], []
for r in dgmsalpha:
    if r[0] == 0:
        betti0.append([r[1][0], r[1][1]])
    elif r[0] == 1:
        betti1.append([r[1][0], r[1][1]])
    elif r[0] == 2:
        betti2.append([r[1][0], r[1][1]])

# Using circumradius, we take sqrt of F and multiply by 2  
betti0 = np.array(np.sqrt(betti0)*2)
betti1 = np.array(np.sqrt(betti1)*2)
betti2 = np.array(np.sqrt(betti2)*2)
betti = [betti0, betti1, betti2]

betti0 = sorted(betti[0], key=lambda x: x[0])
betti0 = np.flip(betti0, axis=0)
betti1 = sorted(betti[1], key=lambda x: x[0])
betti1 = np.flip(betti1, axis=0)
betti2 = sorted(betti[2], key=lambda x: x[0])
betti2 = np.flip(betti2, axis=0)

sio.savemat("ABX3_gdalpha.mat", {"betti0": betti0, "betti1": betti1, "betti2": betti2})
print("c'est fait !")

