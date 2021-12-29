# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
"""
Real loop subtract random loop

"""


# %%
import os, sys, glob, re
import numpy as np
import pandas as pd
import pyranges as pr
#import glbase3


# %%
path = '../data/'
file = glob.glob(os.path.join(path,'real_loop/*.txt'))
file += glob.glob(os.path.join(path,'real_encodel/*.txt'))
file += glob.glob(os.path.join(path,'real_loop/ctcf.rad21/*.txt'))

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


# %%
# name = []
# for f in file:
#     if '.bed.gz' in f and '_r1.' in f:        
#         # if '_r1.' in f:
#         name.append(os.path.split(f)[1].split('.bed.gz')[0] + '_r1')
#     elif '.bed.gz' in f and '_r2.' in f:
#         name.append(os.path.split(f)[1].split('.bed.gz')[0] + '_r1')
#     else:
#         if '_r1' in f: 
#             name.append(os.path.split(f)[1].split('_peaks')[0] + '_r1')
#         else:
#             name.append(os.path.split(f)[1].split('_peaks')[0] + '_r2')


# print(name)

# # %%
# name1 = name[::2]
# name2 = name[1::2]

# %%
filename = [ os.path.split(f)[1].split('.intral')[0].replace('.hesc_primed','').replace('.bed','').replace('.gz','').replace('_peaks','').replace('_narrowPeak','') for f in file ]

filename_r1 = filename[::2]
filename_r2 = filename[1::2]

# %%
data_r1.columns = filename_r1
data_r2.columns = filename_r2
print(data_r1)
print(data_r2)

# %%
data_r1.to_csv("real_r1.txt", sep='\t', index=False)
data_r2.to_csv("real_r2.txt", sep='\t', index=False)

