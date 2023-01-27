#!/usr/bin/env python
# coding: utf-8

# # Ici on va importer les packages de Python

# In[4]:


from GeneralisedFormanRicci.frc import GeneralisedFormanRicci, gen_graph, n_faces
import networkx as nx
import numpy as np
import plotly.graph_objects as go
import math
import matplotlib as mpl
import matplotlib
import plotly.io as pio
import matplotlib.pyplot as plt


# # On donne les coordonnées de chaque atome 

# In[5]:


coords = {'Ti':[[5,5,5]], 'O':[[5, 5, 10], [5, 10, 5], [10, 5, 5], [5,0,5], [0, 5, 5], [5, 5, 0]]}
coords['Ca'] = [[10, 10, 0], [10, 0, 0], [10, 0, 10], [10, 10, 10], [0, 10, 0], [0, 0, 0], [0, 0, 10], [0, 10, 10]]


# In[6]:


data = []
for key, val in coords.items():
    for j in val:
        data.append(j)

def rotate_z(x, y, z, theta):
    w = x+1j*y
    return np.real(np.exp(1j*theta)*w), np.imag(np.exp(1j*theta)*w), z

def matplotlib_to_plotly(cmap, pl_entries):
    h = 1.0/(pl_entries-1)
    pl_colorscale = []

    for k in range(pl_entries):
        C = list(map(np.uint8, np.array(cmap(k*h)[:3])*255))
        pl_colorscale.append([k*h, 'rgb'+str((C[0], C[1], C[2]))])

    return pl_colorscale


# # Parametre de filtartion: f

# In[9]:


""" Normalise Colormap to unique range """ 
seismic_cmap = matplotlib.cm.get_cmap('seismic')

seismic_rgb = []
norm = mpl.colors.Normalize(vmin=0, vmax=255)

for i in range(0, 255):
    k = mpl.colors.colorConverter.to_rgb(seismic_cmap(norm(i)))
    seismic_rgb.append(k)

seismic = matplotlib_to_plotly(seismic_cmap, 255)
f = 0
sc = GeneralisedFormanRicci(points = data, epsilon=f, method="rips", p=2) 
G = gen_graph(list(n_faces(sc.S, 1)), sc.pts, sc.labels) # Get the Graph Network of Simplicial Complex
node_dict = sc.compute_forman()[0] # Get the 0-simplex FRC values
tri_dict = sc.compute_forman()[2] # Get the 2-simplex FRC values 


# # Le code pour tracer la représentation topologique de la molecule

# In[10]:


color_ref = {'Ca': 'purple', 'Ti': 'yellow', 'O': 'green'}

edge_x = []
edge_y = []
edge_z = []
for edge in G.edges():
    x0, y0, z0 = G.nodes[edge[0]]['coords']
    x1, y1, z1 = G.nodes[edge[1]]['coords']
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)
    edge_z.append(z0)
    edge_z.append(z1)
    edge_z.append(None)

traces = []
traces.append(go.Scatter3d(
    x=edge_x, y=edge_y, z=edge_z,
    line=dict(width=2, color='gray'),
    hoverinfo='none', opacity=0.5,
    mode='lines'))

for key, val in coords.items():
    node_x = []
    node_y = []
    node_z = []
    for node in G.nodes():
        x, y, z = G.nodes[node]['coords']
        if [x,y,z] in val:
            node_x.append(x)
            node_y.append(y)
            node_z.append(z)
    
    traces.append(go.Scatter3d(
        x=node_x, y=node_y, z=node_z,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            color=color_ref[key],
            size=10, opacity=1, line=dict(color='black', width=10), colorbar=dict(thickness=20, outlinewidth=2, tickfont=dict(family='Arial', size=30))
            ),
            line_width=2))

for key, val in tri_dict.items():
    s = G.nodes[key[0]]['coords']
    t = G.nodes[key[1]]['coords']
    u = G.nodes[key[2]]['coords']
    e = tri_dict[key]
    #color = mpl.cm.coolwarm(norm(e), bytes=True)
    #tri_c[key] = "rgba({},{},{},{})".format(color[0],color[1],color[2], color[3])
    traces.append(go.Mesh3d(x=[s[0], t[0], u[0]], y=[s[1], t[1], u[1]], z=[s[2], t[2], u[2]], color='lightgray', opacity=.1))


fig = go.Figure(data=traces,
             layout=go.Layout(
                showlegend=False,
                hovermode='closest',
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )
fig.update_layout(plot_bgcolor='rgba(0,0,0,0)')

vertices = list(G.nodes())

fig.update_layout(width=800,
    height=800, scene = dict(
    xaxis=dict(
    autorange=True,
    showgrid=False,
    zeroline=False,
    showline=False,
    showbackground=False,
    title='',
    ticks='',
    showticklabels=False
),
yaxis=dict(
    autorange=True,
    showgrid=False,
    zeroline=False,
    showline=False,
    showbackground=False,
    ticks='',
    title='',
    showticklabels=False
),
zaxis=dict(
    autorange=True,
    showgrid=False,
    zeroline=False,
    showline=False,
    showbackground=False,
    title='',
    ticks='',
    showticklabels=False
)))

xe, ye, ze = rotate_z(0, 0, 1.75, -.1)
camera = dict(
    up=dict(x=0, y=1, z=0),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=xe, y=ye, z=ze)
)

fig.update_layout(scene_camera=camera, scene_dragmode='orbit')
fig.write_html("ABX3_graph_{}.html".format(f))
print("c'est fait !")


# In[ ]:




