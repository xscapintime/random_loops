# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
"""

Get z-score of each row

"""

# %%
import os, sys, glob
import numpy as np
import pandas as pd
import pyranges as pr
from itertools import groupby

# %%
real_r1 = pd.read_csv('real_r1.txt', sep='\t')
real_r2 = pd.read_csv('real_r2.txt', sep='\t')

# %%
real_r1.head()
real_r2.head()


# %%
rand_r1 = pd.read_csv('random_r1.txt', sep='\t')
rand_r2 = pd.read_csv('random_r2.txt', sep='\t')



# %%
# mean of random
m_r1 = []

for i in np.linspace(0, rand_r1.shape[1]-10, int(rand_r1.shape[1]/10), dtype=int):
    #print(i)
    #print(i, i+5)
    m_r1.append(rand_r1.iloc[:,i:i+10].mean(axis=1))
mback_r1 = pd.concat(m_r1, axis=1)


m_r2 = []

for i in np.linspace(0, rand_r2.shape[1]-10, int(rand_r2.shape[1]/10), dtype=int):
    #print(i)
    #print(i, i+5)
    m_r2.append(rand_r2.iloc[:,i:i+10].mean(axis=1))
mback_r2 = pd.concat(m_r2, axis=1)


# %%
# peak number
path = '../data/'

bedfile = glob.glob(os.path.join(path,'bed/*.bed'))
bedfile += glob.glob(os.path.join(path,'encode_bed/*.bed.gz'))
bedfile += glob.glob(os.path.join(path,'bed/ctcf.rad21/*.bed'))

peaknum = []
for b in bedfile:
    bed = pr.read_bed(b)
    peaknum.append(len(bed))


# %%
normed_r1 = pd.DataFrame(real_r1.values - mback_r1.values).div(peaknum, axis=1)
normed_r2 = pd.DataFrame(real_r2.values - mback_r2.values).div(peaknum, axis=1)

normed = pd.concat([normed_r1, normed_r2], axis=1)


# %%
# calculate the z-score for each row
# z-score for each rep
# then concat together seems more resonable

rowmean_r1 = normed_r1.mean(axis=1)
rowmean_r2 = normed_r2.mean(axis=1)

rowsd_r1 = normed_r1.std(axis=1)
rowsd_r2 = normed_r2.std(axis=1)


# %%
zmat_r1 = normed_r1.sub(rowmean_r1, axis=0).div(rowsd_r1, axis=0)
zmat_r2 = normed_r2.sub(rowmean_r2, axis=0).div(rowsd_r2, axis=0)


# %%
# merge two reps together
zmat = pd.concat([zmat_r1, zmat_r2], axis=1)

zmat_merge = (zmat_r1+zmat_r2).apply(lambda x: x/2)

# %%
# exporting
zmat.columns = real_r1.columns.tolist() + real_r2.columns.tolist()
zmat.to_csv("zmat.txt", sep='\t', index=False)

normed.columns = real_r1.columns.tolist() + real_r2.columns.tolist()
normed.to_csv("normed.txt", sep='\t', index=False)


# %%
# export merged table
names = [ n.split('_r')[0] for n in real_r1.columns.tolist() ]
zmat_merge.columns = names
normed_merge.columns = names

zmat_merge.to_csv("zmat_merge.txt", sep='\t', index=False)
normed_merge.to_csv("normed_merge.txt", sep='\t', index=False)
