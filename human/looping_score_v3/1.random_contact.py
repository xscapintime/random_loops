# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import os, sys, glob, re
import numpy as np
import pandas as pd
import pyranges as pr
from itertools import groupby


# %%
#files = os.listdir('../data/ctcf.rad21/')
#len(files)

path = '../data/'
file = glob.glob(os.path.join(path,'random_loop/*.txt'))
file += glob.glob(os.path.join(path,'random_encodel/*.txt'))
file += glob.glob(os.path.join(path,'random_loop/ctcf.rad21/*.txt'))

d1 = [] 
d2 = []

for f in file:
    if  re.match('.*_r1.*', f) != None:
        d1.append(pd.read_csv(f,comment='#',header=None))
    else: #re.match('.*r2.*', f) != None:
        d2.append(pd.read_csv(f,comment='#',header=None))
data_r1 = pd.concat(d1,axis=1)
data_r2 = pd.concat(d2,axis=1)

print(data_r1.head())
print(data_r2.head())


# # %%
# filename_r1 = []
# filename_r2 = []
# #rep = []

# for f in file:
#     #rep = os.path.split(f)[1].split('primed_')[1].split('.intral')[0]
#     if  re.match('.*_r1.*', f) != None:
#         fn = os.path.split(f)[1].split('.hesc')[0].replace('_shuff', '').replace('.bed', '')
#         filename_r1.append(fn + '_r1')
#     else:
#         fn = os.path.split(f)[1].split('.hesc')[0].replace('_shuff', '').replace('.bed', '')
#         filename_r2.append(fn + '_r2')

# print(filename_r1)
# print(filename_r2)

# %%
filename = [os.path.split(f)[1].split('.intral')[0].replace('_shuff', '').replace('.hesc_primed','').replace('.bed','') for f in file ]


filename_r1 = filename[::2]
filename_r2 = filename[1::2]


# %%
data_r1.columns = filename_r1
data_r2.columns = filename_r2
print(data_r1.head())
print(data_r2.head())


# %%
data_r1.to_csv("random_r1.txt", sep='\t', index=False)
data_r2.to_csv("random_r2.txt", sep='\t', index=False)
