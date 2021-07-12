# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import os, sys, glob
import numpy as np
import pandas as pd
import pyranges as pr


# %%
#files = os.listdir('../data/ctcf.rad21/')
#len(files)

path = '../data/loop/ctcf.rad21/'
file = glob.glob(os.path.join(path,'*.txt'))
d1 = []
for f in file:
    d1.append(pd.read_csv(f,comment='#',header=None))
data = pd.concat(d1,axis=1)
print(data)


# %%
# lpfiles = []
# for f in files:
#     if os.path.splitext(f)[1] == '.txt':
#         #print(f)
#         lpfiles.append(f)
#print(lpfiles)


# %%
filename = []
#rep = []
for f in file:
    rep = os.path.split(f)[1].split('primed_')[1].split('.intral')[0]
    fn = os.path.split(f)[1].split('.hesc')[0].replace("_shuff", "")
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
print(peaknum)


# %%
sample = []
for f in file:
    sample.append(os.path.split(f)[1].split('_shuff')[0])
name = np.unique(sample)
print(name)


# %%
CTCF_35846 = data.iloc[:,0:10] / peaknum[0]
CTCF_36632 = data.iloc[:,10:20] / peaknum[1]
CTCF_45230 = data.iloc[:,20:30] / peaknum[2]
CTCF_46184 = data.iloc[:,30:40] / peaknum[3]
CTCF_50988 = data.iloc[:,40:50] / peaknum[4]
RAD21_45689 = data.iloc[:,50:60] / peaknum[5]
RAD21_46164 = data.iloc[:,60:70] / peaknum[6]
RAD21_91096 = data.iloc[:,70:80] / peaknum[7]
RAD21_94415 = data.iloc[:,80:90] / peaknum[8]


# %%
CTCF_35846_r1 = CTCF_35846.iloc[:,CTCF_35846.columns.str.contains('r1')].mean(axis=1)
CTCF_36632_r1 = CTCF_35846.iloc[:,CTCF_36632.columns.str.contains('r1')].mean(axis=1)
CTCF_45230_r1 = CTCF_35846.iloc[:,CTCF_45230.columns.str.contains('r1')].mean(axis=1)
CTCF_46184_r1 = CTCF_35846.iloc[:,CTCF_46184.columns.str.contains('r1')].mean(axis=1)
CTCF_50988_r1 = CTCF_35846.iloc[:,CTCF_50988.columns.str.contains('r1')].mean(axis=1)
RAD21_45689_r1 = CTCF_35846.iloc[:,RAD21_45689.columns.str.contains('r1')].mean(axis=1)
RAD21_46164_r1 = CTCF_35846.iloc[:,RAD21_46164.columns.str.contains('r1')].mean(axis=1)
RAD21_91096_r1 = CTCF_35846.iloc[:,RAD21_91096.columns.str.contains('r1')].mean(axis=1)
RAD21_94415_r1 = CTCF_35846.iloc[:,RAD21_94415.columns.str.contains('r1')].mean(axis=1)


# %%
CTCF_35846_r2 = CTCF_35846.iloc[:,CTCF_35846.columns.str.contains('r2')].mean(axis=1)
CTCF_36632_r2 = CTCF_35846.iloc[:,CTCF_36632.columns.str.contains('r2')].mean(axis=1)
CTCF_45230_r2 = CTCF_35846.iloc[:,CTCF_45230.columns.str.contains('r2')].mean(axis=1)
CTCF_46184_r2 = CTCF_35846.iloc[:,CTCF_46184.columns.str.contains('r2')].mean(axis=1)
CTCF_50988_r2 = CTCF_35846.iloc[:,CTCF_50988.columns.str.contains('r2')].mean(axis=1)
RAD21_45689_r2 = CTCF_35846.iloc[:,RAD21_45689.columns.str.contains('r2')].mean(axis=1)
RAD21_46164_r2 = CTCF_35846.iloc[:,RAD21_46164.columns.str.contains('r2')].mean(axis=1)
RAD21_91096_r2 = CTCF_35846.iloc[:,RAD21_91096.columns.str.contains('r2')].mean(axis=1)
RAD21_94415_r2 = CTCF_35846.iloc[:,RAD21_94415.columns.str.contains('r2')].mean(axis=1)


# %%
av = [CTCF_35846_r1, CTCF_35846_r2, CTCF_36632_r1, CTCF_36632_r2, CTCF_45230_r1, CTCF_45230_r2, CTCF_46184_r1, CTCF_46184_r2,
      CTCF_50988_r1, CTCF_50988_r2, RAD21_45689_r1, RAD21_45689_r2, RAD21_46164_r1, RAD21_46164_r2, RAD21_91096_r1, RAD21_91096_r2,
      RAD21_94415_r1, RAD21_94415_r2]
avs = pd.concat(av,axis=1)
avs


# %%
col_1 = []
col_2 = []
for n in name:
    col_1.append(n + '_r1')
    col_2.append(n + '_r2')
cols = col_1 + col_2
cols.sort()


# %%
avs.columns = cols
avs.columns


# %%
avs.to_csv("ctcf_rad21_meanback.txt", sep='\t', index=False)


