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
path = '../data/real_loop/'
file = glob.glob(os.path.join(path,'*.txt'))

path_ck = '../data/real_loop/ctcf.rad21/'
file += glob.glob(os.path.join(path_ck,'*.txt'))

d1 = []
d2 = []

for f in file:
    if  re.match('.*_r1.*', f) != None:
        d1.append(pd.read_csv(f,comment='#',header=None))
    else: #re.match('.*r2.*', f) != None:
        d2.append(pd.read_csv(f,comment='#',header=None))
data_r1 = pd.concat(d1,axis=1)
data_r2 = pd.concat(d2,axis=1)

print(data_r1.shape)
print(data_r2.shape)


# %%
name = []
for f in file:
    rep = os.path.split(f)[1].split('.esc_')[1].split('.bed')[0]
    fn = os.path.split(f)[1].split('_peaks')[0]
    name.append(fn + '_' + rep)
print(name)


# %%
name1 = name[::2]
name2 = name[1::2]


# %%
data_r1.columns = name1
data_r2.columns = name2
print(data_r1)
print(data_r2)


# %%
## load bed files
bedpath = '../data/bed/'
bedfile = glob.glob(os.path.join(bedpath,'*.bed'))

bedpath_ck = '../data/bed/ctcf.rad21/'
bedfile += glob.glob(os.path.join(bedpath_ck,'*.bed'))


peaknum = []
for b in bedfile:
    bed = pr.read_bed(b)
    peaknum.append(len(bed))


# %%
normed_r1 = data_r1 / peaknum
normed_r1.head()


# %%
normed_r2 = data_r2 / peaknum
normed_r2.head()


# %%
mback_r1 = pd.read_csv('meanback_r1.txt', sep='\t')
mback_r2 = pd.read_csv('meanback_r2.txt', sep='\t')


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
## need reindex because Xxxx_nnnn id
subed_r1 = normed_r1.subtract(mback_r1).reindex(columns=name1)
subed_r1.head()


# %%
subed_r2 = normed_r2.subtract(mback_r2).reindex(columns=name2)
subed_r2.head()


# %%
# subed = pd.concat([subed_r1, subed_r2], axis=1)
# subed.head()


# %%
subed_r1.to_csv("subed_r1.txt", sep='\t', index=False)
subed_r2.to_csv("subed_r2.txt", sep='\t', index=False)


