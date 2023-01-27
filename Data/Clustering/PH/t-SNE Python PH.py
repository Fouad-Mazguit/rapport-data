#!/usr/bin/env python
# coding: utf-8

# # Attention! avant d'exécuter ce code, il faut executer le code matlab

# In[2]:


import numpy as np 
import matplotlib as mpl 
import matplotlib.pyplot as plt 

for ii in range(1, 7):
    file = open("tsne_Eclassdata_new_v{}.txt".format(ii))
    contents = file.readlines()
    for i in range(len(contents)):
        contents[i] = contents[i].split(",")
    values = np.array(contents, dtype=float)

    print(np.shape(values))

    frd = 1000; frs = 500
    plt.figure(figsize=(5,5), dpi=200)
    mpl.rcParams['axes.spines.right'] = False
    mpl.rcParams['axes.spines.top'] = False
    plt.scatter(values[:frd-frs+1,0], values[:frd-frs+1,1], marker='.', color='tab:blue', alpha=0.75, linewidth=0.5, s=20, label="Br-Cubic")
    plt.scatter(values[frd-frs+1:2*(frd-frs+1),0], values[frd-frs+1:2*(frd-frs+1),1], marker='.', color='tab:orange', alpha=0.75,  linewidth=0.5, s=20, label="Br-Orthorhombic")
    plt.scatter(values[2*(frd-frs+1):3*(frd-frs+1),0], values[2*(frd-frs+1):3*(frd-frs+1),1], marker='.', color='tab:green', alpha=0.75,  linewidth=0.5, s=20, label="Br-Tetragonal")

    plt.scatter(values[3*(frd-frs+1):4*(frd-frs+1),0], values[3*(frd-frs+1):4*(frd-frs+1),1], marker='.', color='tab:red', alpha=0.75,  linewidth=0.5, s=20, label="Cl-Cubic")
    plt.scatter(values[4*(frd-frs+1):5*(frd-frs+1),0], values[4*(frd-frs+1):5*(frd-frs+1),1], marker='.', color='tab:purple', alpha=0.75,  linewidth=0.5, s=20, label="Cl-Orthorhombic")
    plt.scatter(values[5*(frd-frs+1):6*(frd-frs+1),0], values[5*(frd-frs+1):6*(frd-frs+1),1], marker='.', color='tab:brown', alpha=0.75,  linewidth=0.5, s=20, label="Cl-Tetragonal")

    plt.scatter(values[6*(frd-frs+1):7*(frd-frs+1),0], values[6*(frd-frs+1):7*(frd-frs+1),1],  marker='.',color='tab:pink', alpha=0.75,  linewidth=0.5, s=20, label="I-Cubic")
    plt.scatter(values[7*(frd-frs+1):8*(frd-frs+1),0], values[7*(frd-frs+1):8*(frd-frs+1),1],  marker='.',color='tab:gray', alpha=0.75,  linewidth=0.5, s=20, label="I-Orthorhombic")
    plt.scatter(values[8*(frd-frs+1):9*(frd-frs+1),0], values[8*(frd-frs+1):9*(frd-frs+1),1],  marker='.',color='tab:olive', alpha=0.75,  linewidth=0.5, s=20, label="I-Tetragonal")

    plt.ylim(np.min(values[:, 1])-10, np.max(values[:,1])+1000)
    plt.xlim(-100, 100)
    #si vous voulez afficher les noms des 9 OHIPs, enlevez le # dans la ligne suivante:
    #plt.legend(ncol=1, loc='upper left', handlelength=0.5, borderpad=0.25, fontsize=10)
    plt.axis('equal')
    plt.xticks([])
    plt.yticks([])  
    plt.savefig("MAPbX3_Clustering_tSNE_v{}.png".format(ii), dpi=400)


# In[ ]:




