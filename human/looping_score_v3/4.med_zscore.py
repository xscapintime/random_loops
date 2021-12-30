"""
take median of all read thresholds
"""

# %%
import os, sys, glob
import numpy as np
import pandas as pd
import pyranges as pr


# %%
zmat = pd.read_csv('zmat_merge.txt', sep='\t')


# %%
# median zscore
zscore_med = zmat.median(axis=0)


# %%
# contact median
normed = pd.read_csv('normed_merge.txt', sep='\t')

contact_med = normed.median(axis=0)

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
df = pd.DataFrame()

# %%
df['zscore'] = zscore_med
df['contact'] = contact_med
df['peak'] = peaknum


# %%
df = df.sort_values('zscore',ascending=False)

df.to_csv('contact_zscore.fin.txt', sep='\t')
