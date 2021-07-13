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
#files = os.listdir('../data/ctcf.rad21/')
#len(files)

path = '../data/real_loop/ctcf.rad21/'
file = glob.glob(os.path.join(path,'*.txt'))
d1 = [] 
d2 = []

for f in file:
    if  re.match('.*r1.*', f) != None:
        d1.append(pd.read_csv(f,comment='#',header=None))
    else: #re.match('.*r2.*', f) != None:
        d2.append(pd.read_csv(f,comment='#',header=None))
data_r1 = pd.concat(d1,axis=1)
data_r2 = pd.concat(d2,axis=1)

print(data_r1.head())
print(data_r2.head())


# %%
name = []
for f in file:
    rep = os.path.split(f)[1].split('primed_')[1].split('.bed')[0]
    fn = os.path.split(f)[1].split('_peaks')[0]
    name.append(fn + '_' + rep)
print(name)


# %%
name1 = []
name2 = []

for n in name:
    if re.match('.*r1.*', n) != None:
        #print(n)
        name1.append(n)
    else:
        name2.append(n)

name1 = np.unique(name1)
name2 = np.unique(name2)

print(name1)
print(name2)


# %%
data_r1.columns = name1
data_r2.columns = name2
print(data_r1)
print(data_r2)


# %%
## load bed files
bedpath = '../data/bed/ctcf.rad21/'
bedfile = glob.glob(os.path.join(bedpath,'*.bed'))
peaknum = []
for b in bedfile:
    bed = pr.read_bed(b)
    peaknum.append(len(bed))


# %%
# peaknum = np.repeat(peaknum, 2)
peaknum


# %%
normed_r1 = data_r1 / peaknum
normed_r1.head()


# %%
normed_r2 = data_r2 / peaknum
normed_r2.head()


# %%
mback_r1 = pd.read_csv('ctcf_rad21_meanback_r1.txt', sep='\t')
mback_r2 = pd.read_csv('ctcf_rad21_meanback_r2.txt', sep='\t')


# %%
mback_r1.head()


# %%
mback_r2.head()


# %%
print(normed_r1.shape)
print(mback_r1.shape)

print(normed_r2.shape)
print(mback_r2.shape)


# %%
# sub = []
# for x in range(0, 18):
#     sub.append(normed.iloc[:,x] - back.iloc[:,x])
# subed = pd.concat(sub, axis=1)


# %%
subed_r1 = normed_r1.subtract(mback_r1)
subed_r1.head()


# %%
subed_r2 = normed_r2.subtract(mback_r2)
subed_r2.head()


# %%
subed = pd.concat([subed_r1, subed_r2], axis=1)
subed.head()


# %%
subed_r1.to_csv("ctcf_rad21_subed_r1.txt", sep='\t', index=False)
subed_r2.to_csv("ctcf_rad21_subed_r2.txt", sep='\t', index=False)


