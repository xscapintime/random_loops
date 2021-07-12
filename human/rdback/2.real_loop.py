# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
"""
Real loop subtract random loop

"""


# %%
import os, sys, glob
import numpy as np
import pandas as pd
import pyranges as pr
#import glbase3


# %%
# 

path = '../data/real_loop/ctcf.rad21/'
file = glob.glob(os.path.join(path,'*.txt'))
d1 = []
for f in file:
    d1.append(pd.read_csv(f,comment='#',header=None))
data = pd.concat(d1,axis=1)
print(data)


# %%
filename = []
for f in file:
    rep = os.path.split(f)[1].split('primed_')[1].split('.bed')[0]
    fn = os.path.split(f)[1].split('_peaks')[0]
    filename.append(fn + '_' + rep)
print(filename)


# %%
data.columns = filename
print(data)


# %%
## load bed files
bedpath = '../data/bed/ctcf.rad21/'
bedfile = glob.glob(os.path.join(bedpath,'*.bed'))
peaknum = []
for b in bedfile:
    bed = pr.read_bed(b)
    peaknum.append(len(bed))


# %%
peaknum = np.repeat(peaknum, 2)
peaknum


# %%
normed = data / peaknum
normed.head()


# %%
back = pd.read_csv('ctcf_rad21_meanback.txt', sep='\t')
back.head()


# %%
print(normed.shape)
print(back.shape)


# %%
sub = []
for x in range(0, 18):
    sub.append(normed.iloc[:,x] - back.iloc[:,x])
subed = pd.concat(sub, axis=1)


# %%
subed.head()


# %%
subed.to_csv("ctcf_rad21_subed.txt", sep='\t', index=False)


