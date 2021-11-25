import os,glob
import pandas as pd
import numpy as np
import pyranges as pr


## zscore
zmat = pd.read_csv('zmat.txt', sep='\t')

used = set()
names = [n.split('_r')[0] for n in zmat.columns]
names = [x for x in names if x not in used and (used.add(x) or True)]

zmat_r1 = zmat.filter(regex='r1').set_axis(names, axis='columns', inplace=False)
zmat_r2 = zmat.filter(regex='r2').set_axis(names, axis='columns', inplace=False)

# merge two rep by taking mean
zmat_merge = (zmat_r1+zmat_r2).apply(lambda x: x/2)


# merge thresholds, median, more reasonable
zscore_med = zmat_merge.iloc[8:12,].median(axis=0)



## contact mean
# normed and subed loop number matrix

subed_r1 = pd.read_csv('subed_r1.txt', sep='\t')
subed_r2 = pd.read_csv('subed_r2.txt', sep='\t')

subed_r1 = subed_r1.set_axis(names, axis='columns', inplace=False)
subed_r2 = subed_r2.set_axis(names, axis='columns', inplace=False)

# %%
# merge subed matrix to one

subed_merge = (subed_r1+subed_r2).apply(lambda x: x/2)



# %%
# mean of loop number for each column
# exclude first two rows

loop_med = subed_merge.iloc[8:12,].median(axis=0)




## peak number
bedpath = '../data/bed/'
bedfile = glob.glob(os.path.join(bedpath,'*.bed'))

bedpath_ck = '../data/bed/ctcf.rad21/'
bedfile += glob.glob(os.path.join(bedpath_ck,'*.bed'))

peaknum = []
for b in bedfile:
    bed = pr.read_bed(b)
    peaknum.append(len(bed))




## table
df = pd.DataFrame()

df['zscore'] = zscore_med
df['contact_num'] = loop_med
df['peak_num'] = peaknum

df = df.sort_values('zscore',ascending=False)

df.to_csv('contact_zscore.fin.txt', sep='\t')
